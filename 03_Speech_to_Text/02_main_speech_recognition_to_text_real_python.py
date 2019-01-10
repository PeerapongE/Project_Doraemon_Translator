# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:25:24 2018

@author: PeerapongE
"""

# The Ultimate Guide To Speech Recognition With Python
# https://realpython.com/python-speech-recognition/

# Installation
# pip install SpeechRecognition





import speech_recognition as sr
# Version checking sr.__version__ 

r = sr.Recognizer()

# =============================================================================
# Each Recognizer instance has seven methods for recognizing speech from an audio source using various APIs. These are:
# 
# recognize_bing(): Microsoft Bing Speech
# recognize_google(): Google Web Speech API
# recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
# recognize_houndify(): Houndify by SoundHound
# recognize_ibm(): IBM Speech to Text
# recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
# recognize_wit(): Wit.ai
# Of the seven, only recognize_sphinx() works offline with the CMU Sphinx engine. The other six all require an internet connection.
# =============================================================================

# default API key for the Google Web Speech API
# The other six APIs all require authentication with either an API key or a username/password combination


#%% Loading Audio file

# =============================================================================
# Supported File Types
# Currently, SpeechRecognition supports the following file formats:
# 
# WAV: must be in PCM/LPCM format
# AIFF
# AIFF-C
# FLAC: must be native FLAC format; OGG-FLAC is not supported
# =============================================================================

filename = 'harvard.wav'
#filename = 'jackhammer.wav'

harvard = sr.AudioFile(filename)

with harvard as source:
   audio = r.record(source)
   
type(audio)

r.recognize_google(audio)

#%% Capturing Segments With offset and duration

#harvard = sr.AudioFile(filename)

with harvard as source:
    audio1 = r.record(source, duration=4)
    audio2 = r.record(source, duration=4)

r.recognize_google(audio1)
r.recognize_google(audio2)
#%% with Time offset

with harvard as source:
    audio = r.record(source, offset=4, duration=3)

r.recognize_google(audio)


#%% Voice file with noise
# the stale smell of old beer lingers

jackhammer = sr.AudioFile('jackhammer.wav')
with jackhammer as source:
    audio = r.record(source)

r.recognize_google(audio)

#%% with noise removel

with jackhammer as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

r.recognize_google(audio)

# %% with adjust noise removal

with jackhammer as source:
    r.adjust_for_ambient_noise(source, duration=0.5) # default = 1
    audio = r.record(source)

r.recognize_google(audio)

# %% return all possible combination

r.recognize_google(audio, show_all=True)


