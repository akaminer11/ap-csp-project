# https://raw.githubusercontent.com/first20hours/google-10000-english

from deep_translator import GoogleTranslator

with open("eng-words.txt", "r") as file:
    li = file.readlines()

li.sort()

with open("new-words.txt", "r") as es:
    es_li = es.readlines()
    es_length = len(es_li)

translatores = GoogleTranslator(source='en', target='es')
translatorfr = GoogleTranslator(source='en', target='fr')
translatorde = GoogleTranslator(source='en', target='de')


to_sp = []
for i in range(es_length, len(li)):
    w = li[i].strip('\n') + "-" + translatores.translate(li[i]) + "-" + translatorfr.translate(li[i]) + '-' + translatorde.translate(li[i])
    to_sp.append(w)
    print(f"{i}/{len(li)}")
    if i % 100 == 0 or i % 9999 == 0:
        with open("new-words.txt", "a") as es:
            for word in to_sp:
                es.write(word + "\n")
        to_sp = []
        print("#### WRITE SUCCESSFUL ####")

