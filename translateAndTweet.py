import twitter, os
import json, requests, urllib
from random import randrange


def postStatus( tweet ):
    print "tweeting..."
#user = "testingOtesting"
#password = "supersecure"
    myInfo = {
        "access_token_key" : ,#YOU FILL THIS IN
        "access_token_secret" : ,#THIS TOO
        "consumer_key" : ,#dont forget that it's a good idea to keep
        "consumer_secret" : #your secrets seperate from your program
        }
    api = twitter.Api(**myInfo)

    status = api.PostUpdate(tweet)
    print status

def translate( someString, sourceLang, destLang):
    args = {
        'client_id': ,#your client id here
        'client_secret': ,#your azure secret here
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
        }
    oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    oauth_junk = json.loads(requests.post(oauth_url,data=urllib.urlencode(args)).content)
    translation_args = {
        'text': someString,
        'to': destLang,
        'from': sourceLang
        }
    headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
    translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
    translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
    translated =  translation_result.content.replace("\u000a","")
    translated = translated.replace('"', "")
    translated = translated.replace("'", "")
    translated = translated.replace("\\", "")
    translated = translated.replace("\ufeff", "")
    return translated

def getLine():#in case you prefer to retrive from a file of canned sentences
    f = open('paresdText.txt', 'r')
    
    rand = randrange(72000)
    f.seek(rand)
    f.readline()
    retString = f.readline()
    while len(retString) < 20 or len(retString) > 140 :
        retString = f.readline()
    f.close()
    return retString

def main():
    langs = ["en", "ar", "bg", "ca", "zh-CHS", "zh-CHT", "cs", "da", "nl", "et", "fa", "fi", "fr", "de", "ht", "he", "hi", "hu", "id", "it", "ja", "ko", "lv", "lt", "mww", "no", "pl", "pt", "ro", "ru", "sk", "sl", "es", "sv", "th", "tr", "uk", "vi", "en"]
    
    toTranslate = raw_input("enter something to be modified and tweeted: ")#getLine()
    print toTranslate

    print "\n"
    print "translating... \n"

    for i in range(1,39):
        toTranslate = translate( toTranslate, langs[i-1] , langs[i] )
        print toTranslate

        
    if len(toTranslate) > 140:
        toTranslate = toTranslate[0:140]
    postStatus( toTranslate.decode('utf-8') )




main()

