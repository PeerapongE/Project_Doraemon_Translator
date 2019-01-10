# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:40:57 2018

@author: PeerapongE
"""
# Main library
# Translator
# https://pypi.org/project/googletrans/
# API main documentation
# https://py-googletrans.readthedocs.io/en/latest/
# https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group
# pip install git+https://github.com/BoseCorp/py-googletrans.git --upgrade
#from googletrans import Translator

# Optional library
# working library
# https://pypi.org/project/py-translator/
# pip3 install py_translator==2.1.8
from py_translator import Translator

#%% Create object from Translator

translator = Translator()

#%% Translate from string
print('-----------Translator from string --------------')

# English to Thai
translations = translator.translate(text = 'hello my friend', src='en', dest = 'th')

# Thai to English
translations = translator.translate(text = 'ลมอ่อนพัดโชยมาน้ำตาก็ไหลรินเหลือเพียงกลิ่นหัวใจฟุ้งไปกับความเหงา',
                                    src  = 'th',
                                    dest = 'en')


print('Original Text :')
print(translations.origin)

print('Translated Text :')
print(translations.text)


#%% language detection 
print('----------- Language Detection --------------')

LangDetectObj = translator.detect('이 문장은 한글로 쓰여졌습니다.')
LangDetectObj = translator.detect('ไปกับพี่มั๊ยจ๊ะน้องสาว')


LangDetect = LangDetectObj.lang
LangConf   = LangDetectObj.confidence

print('Detect language is : %s with confident : %.3f'%(LangDetect,LangConf))

#%% Translate from list
print('-----------Translator from list --------------')


translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')

for translation in translations: # since the text is list, translations become list (iterable object)
    print(translation.origin, ' -> ', translation.text)
