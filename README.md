# 🤖 BaustellRoboter

## Components used
![Pin Doc](./ReadmeFiles/PinDoc.svg)
### Waveshare Pico-Audio (Inital Version)
Uses pins GP26, GP27 and GP28. See more info [here](https://www.waveshare.com/wiki/Pico-Audio)
### L293D
Uses pins GP10 - 12 and GP19-21

# Development

## Audio
Make sure you have [ffmpeg](https://formulae.brew.sh/formula/ffmpeg#default) installed
To compress any audio file down to 400kb use the Makefile in /Audio folder by running:

```
make input="yourAudioFile.mp3"   
```
## Website
Website is made with  [CRA](https://create-react-app.dev/) 
To deploy you must have [Firebase CLI](https://formulae.brew.sh/formula/firebase-cli) installed and be logged in with an account that has access to [this Firebase project](https://console.firebase.google.com/u/0/project/baustellrobots/database/baustellrobots-default-rtdb/data). 
Then inside the websites folder (/websitecra) run:
```
yarn run deploy
```
It will be deployed to: https://baustellrobots.web.app/
# Naming
- Bella -> Helm: Rot, oranger Punkt
- Bianca -> Helm: Gelb, oranger Punkt
- Fiona -> Helm: Orange, jsp label hinten
- Cosimo -> Helm: Orange, grüner Sticker
- Schorsch -> Helm: Gelb, FCK SVP Sticker
- Adonis -> Helm: Orange, Implenia Sticker
- Jochen -> Helm: Gelb, baby
- + currently unnamed extra, should it be named?
