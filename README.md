# Controlling Raspberry Pi Using Alexa

## Installation

  ### Flask-Ask

```python3 -m pip install Flask-Ask
pip3 install --upgrade setuptools
pip3 install 'cryptography<2.2'
```

### Ngrok
1. Download ngrok link for Linux on https://ngrok.com/download
2. Open a new terminal, unzip the downloaded ngrok file
   ```
   unzip path/ngrok.zip
   ```
3. Start a HTTP tunnel
   ```
   ./ngrok http 5000
   ```
4. We will use the second Forwarding URL (the one starts with https://)

## Amazon Developer Console 
1. Create a new skill using "Create Skill" button
2. Assign name for the project; choose "Custom" model; click "Create skill"
3. Create ***Intents and Utterances*** for the project 
    Intent implies the action that the user request. 
    Utterance is a set of phrases that the user might say to make request to Alexa. Each intent has a set of utterances to correspondings to the user's request.
    ---Tips: The more utterances you create, the more Alexa can accurately capture what the user might request.
4. Set up ***Endpoint***
    In the "Endpoint" section, click on "HTTPS"
    Choosing the "Default Region" option
    Copy the forwarding URL from ngrok terminal and paste it in the "Default Refion" space
    Choose "My development endpoint is a sub-domain of a domain..."
    Save Endpoint
    




