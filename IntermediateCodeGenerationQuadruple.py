# -*- coding: utf-8 -*-
"""
Created on Tue May  4 07:50:15 2021

@author: Rimjhim Dubey
"""

OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}


def infix_to_postfix(formula):
    stack = []
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack: 
    	output += stack.pop()
    #print(f'POSTFIX: {output}')
    return output


def generate3ACG(pos,type):
    k = 1
    e_stack = []
    for i in pos:
        if i not in OPERATORS:
            e_stack.append(i)
        else:
            if type == "Quad":
                print(i,e_stack[-2], e_stack[-1],"l{}".format(k))
                e_stack = e_stack[:-2]
                e_stack.append("l{}".format(k))
            elif type =="Trip":
                print(i,e_stack[-2], e_stack[-1],"------->","({})".format(k))
                e_stack = e_stack[:-2]
                e_stack.append("({})".format(k))
            else:
                print(i,e_stack[-2], e_stack[-1],"------->","({})".format(k))
                e_stack = e_stack[:-2]
                e_stack.append("({})".format(k))
            k += 1

print()
expres = input("Enter Expression: ")
print()
pos = infix_to_postfix(expres)
print("3 Address Code Generation:-")
print()
print("Quadruple:")
generate3ACG(pos,"Quad")
print()
print("Triple:")
generate3ACG(pos,"Trip")
print()
print("Indirect Triple:")
generate3ACG(pos,"InTrip")
print()