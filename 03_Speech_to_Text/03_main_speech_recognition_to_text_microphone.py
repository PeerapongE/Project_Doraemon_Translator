# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:21:46 2018

@author: PeerapongE
"""

# Working With Microphones

# Installation
# pip install pyaudio
# pip install SpeechRecognition

import speech_recognition as sr

r = sr.Recognizer()

# Instead of file: using microphone


mic = sr.Microphone()

# to check which microphone to use
# sr.Microphone.list_microphone_names()
# activate any mic: 
# mic = sr.Microphone(device_index=3)
# For most projects, though, you’ll probably want to use the default system microphone.

#%% record with microphone

with mic as source:
    print('please speaking') 
    audio = r.listen(source) # , duration=4

print('Speech to text in progress')
#r.recognize_google(audio) # default language is english
r.recognize_google(audio, language="th")    

#%% Listening with noise removal

with mic as source:
    print('please speaking')
    r.adjust_for_ambient_noise(source) # add this line
    audio = r.listen(source)

r.recognize_google(audio)   








