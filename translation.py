#!/bin/python




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


if __name__ == "__main__":
    main()
