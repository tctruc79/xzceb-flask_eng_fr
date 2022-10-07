"""
Machine translator
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']


authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)


def english_to_french(english_text):
    """
    Translates english to french
    """
    if (english_text != None):
        french_trans=language_translator.translate(text=english_text, model_id='en-fr').get_result()
        french_text=french_trans['translations'][0]['translation']
        return french_text
    else:
        return None


def french_to_english(french_text):
    """
    Translates french to english
    """
    if (french_text != None):
        english_trans=language_translator.translate(text=french_text, model_id='fr-en').get_result()
        english_text=english_trans['translations'][0]['translation']
        return english_text
    else:
        return None
