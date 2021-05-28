# -*- coding: utf-8 -*-
"""
Created on Tue May  4 06:46:53 2021

@author: Rimjhim Dubey
"""

import re
def isparsed(x,l):
    if x in l:
        return True
    else:
        return False

f=open('InputProg.c',mode='r')
s=f.read()
ids=[]
keywords=[]
spch=[]
operators=[]
digits=[]
opsl=["+","-","/","*","<",">","<<",">>","=","==","&","|","&&","||"]
keysl=["int","char","float","bool","true","false","cout","cin","void","iostream","main","endl","if","else","include","using","namespace","std"]
spchl=["#","(",")","{","}",";"]
l=re.split("(\W+)",s)
for i in l:
       if "(){" in i:
         l.remove(i)
         spch.append("(")
         spch.append(")")
         spch.append("{")
       elif "){" in i:
         l.remove(i)
for i in l:
    lx=re.split("\t|\n| |,|;",i)
    for j in lx:
            if(j==''):
                continue
            if (isparsed(j,keysl)):
                if (j not in keywords):
                    keywords.append(j)
                else:
                    continue
            elif (isparsed(j,opsl)):
                if (j not in operators):
                    operators.append(j)
                else:
                    continue
            elif (isparsed(j,spchl)):
                if (j not in spch):
                    spch.append(j)
                else:
                    continue
            elif re.match('[0-9]+',j):
                if(j not in digits):
                    digits.append(j)
                else:
                    if j not in ids:
                        ids.append(j)
print("Keywords:",keywords)
print("Special Characters:",spch)
print("Operators:",operators)
print("Identifiers:",ids)
print("Numbers used:",digits)