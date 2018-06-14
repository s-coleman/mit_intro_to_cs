#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 13:18:26 2018

@author: scoleman

Week 1: Problem 3 of MITx: 6.00.1x
"""



#Given a string a continuous string of text, the code returns the longest substring of alphabetically ordered characters.
#No recursion or special methods allowed in the actual capturing of substrings.
#Feel like I over-did it on the print statement.
s = 'azcbobobegghakl'
longest_strings = []
for idx, elt in enumerate(s):
    substring = '' + elt
    longest_strings.append(substring)
    counter = idx
    while counter < len(s) - 1:
        if ord(s[counter + 1]) >= ord(s[counter]):
            substring += s[counter + 1]
            longest_strings.append(substring)
            counter += 1
        else:
            break
            #counter = idx
print('Longest substring in alphabetical order is: ', [x for x in longest_strings if len(x) == max([len(elt) for elt in longest_strings])][0])