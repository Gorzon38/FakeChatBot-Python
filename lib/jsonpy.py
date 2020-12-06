from pathlib import Path
from random import choice
import json

source_path = Path('AI\lib\data\word.json')
documents = json.loads(source_path.read_text())

def cjson(choix,choixw): #choix d'emote
    return choice(choix(choixw))

def interact(word):
    doc_interact = documents['interact'][0]
    interact = doc_interact[word]
    return interact

def answ(word):
    doc_answ = documents['answ'][0]
    answ = doc_answ[word]
    return answ

def feel(word):
    doc_feel = documents['feel'][0]
    feel = doc_feel[word]
    return feel

def emote(word):
    doc_emote = documents['emote'][0]
    emote = doc_emote[word]
    return emote
