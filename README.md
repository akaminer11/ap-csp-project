# AP Computer Science Principles Final Project
A very bad "translation tool" using python and literally zero reasonable 
thinking. I whipped it up in basically a day. Getting the wordlist was the 
hardest part.

## Description
This is a tool that takes a wordlist of the 10000 most popular english words,
uses an external tool to translate those words, stores them in a file, and then
accesses them to translate. It can translate from english into Spanish, German,
or French.

## Documentation
There doesn't need to be much documentation. This is pretty self explanatory.
Function names make it pretty obvious what they do, and they have docstrings.
Use -h or --help if to see all of the arguments. Translation.py is the main 
file, use arguments on that one. Everything else is a tool to get the wordlist
up and running.

## Sources
Original wordlist: https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-no-swears.txt

Translation Library: google translator through deep-translator library
