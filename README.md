# 🤖 BaustellRoboter

## Components used
![Pin Doc](./ReadmeFiles/PinDoc.svg)
### Waveshare Pico-Audio (Inital Version)
Uses pins GP26, GP27 and GP28. See more info [here](https://www.waveshare.com/wiki/Pico-Audio)
### L293D
Uses pins GP10 - 12 and GP19-21

# Development
## Prerequisites
Have [ffmpeg](https://formulae.brew.sh/formula/ffmpeg#default) installed

## Audio
To compress any audio file down to 400kb use the Makefile in /Audio folder by running:

```
make input="yourAudioFile.mp3"   
```