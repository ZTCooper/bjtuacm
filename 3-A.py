# -*- coding: UTF-8 -*-

n = int(input())

dictionary = list()
count = 0

raw_sentence = input()
sentence = raw_sentence.replace("!","").split()

for i in range(n):
    dictionary.append(input())

for d_word in dictionary:
    for s_word in sentence:
        if len(d_word) == len(s_word):
            diff_letter = 0
            for num in range(len(d_word)):
                diff_letter += not(d_word[num] == s_word[num].lower())
            if diff_letter == 1:
                count += 1
                raw_sentence = raw_sentence.replace(s_word, d_word)

print(count)
print(raw_sentence.capitalize())
