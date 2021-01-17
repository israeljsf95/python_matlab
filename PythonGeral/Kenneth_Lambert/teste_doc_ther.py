# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:56:42 2020

@author: israe
"""

import random


hedges = ("Please tell me more.", "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"you",
                "we":"you", "us":"you", "mine":"yours"}


def reply(sentence):
    prob = random.randint(1,4)
    if prob == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)
    

def changePerson(sentence):
    palavras = sentence.split()
    subst_palavras = []
    for palavra in palavras:
        subst_palavras.append(replacements.get(palavra, palavra))
    return " ".join(subst_palavras)


def main():
    print("Good Morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n >> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))
        
if __name__ == "__main__":
    main()





