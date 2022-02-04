#!/bin/python
import sys

def invalid_syntax():
    with open("help.txt") as helpfile:
        h = helpfile.readlines()
        print("#####################################################\nFatal error: Invalid syntax. Printing help statement.\n#####################################################\n")
        for line in h:
            line = line[:-1]
            print(line, sep='')
        print("\n\n")


def take_input():
    args = sys.argv
    if len(args) > 3:
        invalid_syntax()
        break


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

    take_input()



if __name__ == "__main__":
    main()
