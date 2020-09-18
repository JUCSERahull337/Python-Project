import os
from gtts import gTTS
f=open("spech.txt")
x=f.read()
lan="en"
audio=gTTS(text=x, lang=lan,slow=False)
audio.save("test3.wav")
os.system("test3.wav")
print("file created")