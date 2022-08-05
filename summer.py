import logging
#load flask module into python script
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import gspread
#import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
#flask object named app
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

filePath= "testing_data.csv"
data = []
mostCurrent = 0

#define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('raspberry-pi-summer-25fbfce05538.json', scope)
#authorize the clientsheets
client = gspread.authorize(creds)
#get the instance of the Spreadsheet
sheet = client.open('Summer Test Data')
#get the first sheets of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

#amzn1.application.f65005977a2b4384b2e09cdb90de540b

#welcome message fxn
@ask.launch
def launchProtocol():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)
    #speech_text = 'Welcome to the Raspberry Pi alexa automation.'
    #return question(speech_text).reprompt(speech_text).simple_card(speech_text)

#current value fxn--w/ getData() and writeDataSheets()
@ask.intent("CurrentIntent")
def yesProtocol():
    global data
    global mostCurrent
    mostCurrent = 0
    data = []
    getData()
    writeDataSheets()
    bs_msg = render_template('bsprompt')
    bs_msg += getBloodSugar(data[mostCurrent-2])
    return statement(bs_msg)

def writeDataSheets():
    global filePath
    with open(filePath, 'r') as file_obj:
        content = file_obj.read()
        client.import_csv('1LlwGIEctYQeLjXCAXZwy1al0S6sBqMidS3nKpjZsNp4', data=content)
    
def getData():
    global data
    global mostCurrent
    f = open(filePath, 'r')
    line = f.readline()
    if mostCurrent == 0:
        line = f.readline()
        mostCurrent += 1
    while line:
        tempdata = [int(tempdata) for tempdata in line.split(',')]
        data.append(tempdata)
        mostCurrent += 1
        line = f.readline()

def getBloodSugar(data):
    if data[1] >= 8:
        data[1] -= 8
    else:
        data[1] = 24 + data[1] - 8
    data[3] = str(data[3])
    data[3].strip('\n')
    data[3] = int(data[3])
    message = 'Your current blood sugar level is: '
    message += str(data[3])
    message2 = 'The blood sugar monitor has been running for '
    message2 += str(data[0])
    message2 += ' days '
    message2 += str(data[1])
    message2 += ' hours and '
    message2 += str(data[2])
    message2 += ' minutes.'
    return str(data[3])
    #print(message)
    #print(message2)


if __name__ == '__main__':

    app.run(use_reloader = False)
