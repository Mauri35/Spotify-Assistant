import speech_recognition as sr
import requests
import json 
from win10toast import ToastNotifier
import time


with open('config.json') as file:
    data = json.load(file)
    token = data['token']

r = sr.Recognizer() 

try:
    toaster = ToastNotifier()
    toaster.show_toast("Spotify Assistant","Spotify Assistant Starting", duration=1)

    def main():
        with sr.Microphone() as source:
            print('Speak Anything : ')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='es-UY')
            print('You said: {}'.format(text))
            if text == "siguiente":
                SiguienteCancion()
                print('You said: {}'.format(text))
            elif text == "atrás":
                AnteriorCancion()
                print('You said: {}'.format(text))
            elif text == "pausa":
                PausarCancion()
                print('You said: {}'.format(text))
            elif text == "reproducir":
                Reproducir()
                print('You said: {}'.format(text))
            elif text == "salir asistente":
                quit()
            elif text == "volumen diez":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=10"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 10", duration=2)
                main()
            elif text == "volumen 20":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=20"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 20", duration=2)
                main()
            elif text == "volumen 30":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=30"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 30", duration=2)
                main()
            elif text == "volumen 40":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=40"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 40", duration=2)
                main()
            elif text == "volumen 50":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=50"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 50", duration=2)
                main()
            elif text == "volumen 60":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=60"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 60", duration=2)
                main()
            elif text == "volumen 70":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=70"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 70", duration=2)
                main()
            elif text == "volumen 80":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=80"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 80", duration=2)
                main()
            elif text == "volumen 90":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=90"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 90", duration=2)
                main()
            elif text == "volumen 100":
                url = "https://api.spotify.com/v1/me/player/volume?volume_percent=100"
                payload={}
                headers = {
                'Authorization': 'Bearer {}'.format(token)
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                toaster = ToastNotifier()
                toaster.show_toast("Spotify Assistant","Volumen 100", duration=2)
                main()
            main()
        except:
            print('Sorry could not hear')
            main()
except:
    main()

def SiguienteCancion():
    url = "https://api.spotify.com/v1/me/player/next"
    payload={}
    headers = {
      'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    time.sleep(.3)
    
    url = "https://api.spotify.com/v1/me/player?market=ES"
    payload={}
    headers = {
    'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.get(url, headers=headers, data=payload)
    xd = json.loads(response.text)
    toaster = ToastNotifier()
    toaster.show_toast("Spotify Assistant","Skipped Now playing: {}".format(xd["item"]["name"]), duration=1)
    main()




def AnteriorCancion():
    url = "https://api.spotify.com/v1/me/player/previous"
    payload={}
    headers = {
      'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    time.sleep(.3)
    
    url = "https://api.spotify.com/v1/me/player?market=ES"
    payload={}
    headers = {
    'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.get(url, headers=headers, data=payload)
    xd = json.loads(response.text)
    toaster = ToastNotifier()
    toaster.show_toast("Spotify Assistant","Previous Now playing: {}".format(xd["item"]["name"]), duration=1)
    main()

def PausarCancion():
    url = "https://api.spotify.com/v1/me/player/pause"
    payload={}
    headers = {
      'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    toaster = ToastNotifier()
    toaster.show_toast("Spotify Assistant","Paused", duration=1)
    main()

def Reproducir():
    url = "https://api.spotify.com/v1/me/player/play"
    payload={}
    headers = {
      'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.request("PUT", url, headers=headers, data=payload)


    url = "https://api.spotify.com/v1/me/player?market=ES"
    payload={}
    headers = {
    'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.get(url, headers=headers, data=payload)
    xd = json.loads(response.text)
    toaster = ToastNotifier()
    toaster.show_toast("Spotify Assistant","Now playing: {}".format(xd["item"]["name"]), duration=1)
    main()

main()