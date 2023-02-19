#
#Skrypt, który wczytuje plik z tekstem. (Moze byc "Lorem ipsum").
#Dla tekstu wygeneruj:
#- długość tekstu
#- ilość wyrazów
#- ilość znaków (bez whitespace-ów)
#- jak podasz argument "advanced" przy wywoływaniu skryptu to wypisze dodatkowe statystyki, jak:
#    - ilość lower case letters
#    - ilość upper case letters
#    - ilość digits

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-a","--advanced", help="show more stats", action="store_true")
args = parser.parse_args()


text_path = "text.txt"

def load_text(text_path: str):
        with open(text_path, "r") as stream:
            return stream.read()


def text_process(text_path):
    text = load_text(text_path)
    print(f"This is the loaded text: {text}")
    print(f"Length of the loaded text: {len(text)}.")
    text_split = text.split() 
    print(f"Number of words: {len(text_split)}")
    chars= len(text)
    whitespace = text.count(" ")
    print(f"Number of whitespaces: {whitespace}")
    clean_chars = int(chars) - int(whitespace) 
    print(f"Number of chars {clean_chars}")
    
        
def advanced_options(text_path):
    text = load_text(text_path)
    lower_case = 0
    upper_case = 0
    digit = 0
    for znak in text:
        if znak.islower():
            lower_case += 1
        elif znak.isupper():
            upper_case += 1
        elif znak.isdigit():
            digit += 1
    print(f"Number of  lower cases: {lower_case}")
    print(f"Number of upper cases: {upper_case}")
    print(f"Number of digits: {digit}")



text_process(text_path)

if args.advanced:
    advanced_options(text_path)

    


