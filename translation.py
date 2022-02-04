#!/bin/python
import sys


def print_help():
    with open("help.txt", "r") as helpfile:
        h = helpfile.readlines()
    for line in h:
        line = line[:-1]
        print(line, sep='')
    print("\n\n")



def invalid_syntax():
    print("#####################################################\nFatal error: Invalid syntax. Printing help statement.\n#####################################################\n")
    print_help()


def invalid_lang():
    print("#######################################################\nFatal error: Invalid language. Printing help statement.\n#######################################################\n")
    print_help()


def word_not_found():
    print("###########################################################\nError: Word not found in wordlist. Printing help statement.\n###########################################################")
    print_help()



def take_input(words):
    acceptable_helps = ["-h", "--help"]
    acceptable_langs = ["-s", "-f", "-g", "--german", "--french", "--spanish"]
    german = ["-g", "--german"]
    french = ["-f", "--french"]
    spanish = ["-s", "--spanish"]
    args = sys.argv
    if len(args) == 2:
        h = args[1]
        if h not in acceptable_helps:
            invalid_syntax()
        else:
            print_help()
    elif len(args) == 3:
        lang = args[1]
        word = args[2]
        if lang not in acceptable_langs:
            invalid_lang()
        else:
            if lang in german:
                lang_num = 2
            elif lang in french:
                lang_num = 1
            else:
                lang_num = 0
            translate(word, words, lang_num)
    else:
        invalid_syntax()



def translate(word, words, lang):
    if word in words:
        print(words[word][lang])
    else:
        word_not_found()


def parse(phrase):
    '''
    Word line format:
    english-spanish-french-german
    '''
    words = phrase.split("-")
    eng = words[0]
    langs = words[1:]
    langs[2] = langs[2][:-1]
    return eng, langs
   


def main():
    with open("words.txt", "r") as w:
        lines = w.readlines()
    words = {}
    for phrase in lines:
        eng, langs = parse(phrase)
        words[eng] = langs
    take_input(words)
    


if __name__ == "__main__":
    main()
