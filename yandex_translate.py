import requests
import json
key = 'trnsl.1.1.20190810T120830Z.6a818d641975acd7.7b759f840552a061735768d37db6b50020747699'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
def translate_me(mytext):
    '''https://translate.yandex.net/api/v1.5/tr.json/translate
 ? [key=<API-ключ>]
 & [text=<переводимый текст>]
 & [lang=<направление перевода>]
 & [format=<формат текста>]
 & [options=<опции перевода>]
 & [callback=<имя callback-функции>]'''
    params = {
        'key':key,
        'text':mytext,
        'lang':'ru-en',
    }
#https://translate.yandex.net/api/v1.5/tr.json/translate?key=
   # response = requests.post(url,params = params)
   # return response.json()


#json = translate_me('привет, друг')
#print(json)
#print(json['text'])
f = open('for_ya_tr')

def new_file_translator(f):
    text = f.read()
    params = {
        'key': key,
        'text': text,
        'lang': 'ru-en',
    }
    response = requests.post(url, params = params)
    return response.json()
json = new_file_translator(f)
print(json)
print(json['text'])
