# Spotify-Assistant
 Assistant made in python to control your spotify via voice

# Overview
- 🚀 PLAY, PAUSE, NEXT, PREVIOUS, VOLUME COMMANDS

- 📝 Toast notifications for Windows;

- ☑️ Voice recognition by google

- 🚅 Simple code, easily modifiable

<img src="https://i.imgur.com/dGReORh.gif"> 

# Pendings
Add support for 2 languages, English and Spanish (current)

# Requirements
- Python >3.7
- Speech_Recognition
- requests
- win10toast

# Installation
- pip install requests
- pip install win10toast
- pip install pipwin
- pipwin install pyaudio
- pip install SpeechRecognition
- Change the user token in config.json you get it in: https://developer.spotify.com/console/put-pause/ (Scopes: user-modify-playback-state)
- Run: python3 assistant.py

# Proyect status:
- This project is active and waiting for improvements, any recommendations will be used to improve it!
- The current language of the voice commands are in Spanish, the sooner I have time I will upload an English version, but you can modify it by changing it in the r.recognize_google and in the ifs of the commands

