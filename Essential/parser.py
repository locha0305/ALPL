#developed by locha
#parser for ALPL


#imports
import sys
import os
import random
import math

#this is a parser class
#parse ALPL file to normal list
class parser():
    def __init__(self, code): #input code
        self.code = code
        self.code = self.code.split("\n")
        self.code = [line + ";" for line in self.code]
        self.code = ''.join(self.code)
        self.parse_result = []
        #tokens to define
        self.TT_CLASS = "CLASS"
        self.TT_FUNC = "FUNC"
        self.TT_SETATTR = "SETATTR"
        self.TT_DEFINE = "DEFINE"
        self.TT_END_DEFINE = "END_DEFINE"
        self.TT_END_SETATTR = "END_SETATTR"
        self.TT_END = "END"
        self.TT_CALL = "CALL"
    def parse(self): #this parses the code
        cursor = 0
        word = ""
        while cursor < len(self.code):
            letter = self.code[cursor]
            if letter == ";": #checks the end of line
                pass
            elif letter == ":": #checks the define of attributes
                attr_name = word
                self.parse_result.append(self.TT_SETATTR)
                self.parse_result.append(attr_name)
                jump = 0
                value = ""
                while self.code[jump + cursor] != ";":
                    if self.code[jump + cursor] == "}":
                        jump -= 1 #therefore to check for '}'
                        break
                    else:
                        jump += 1
                        value += self.code[jump + cursor]
                

                self.parse_result.append(value.strip(";").strip("}"))
                cursor += jump
                self.parse_result.append(self.TT_END_SETATTR)
                word = ""
            elif letter == "}": #checks when a Class or a Function ends and return the certain token
                self.parse_result.append(self.TT_END)
                word = "" #reset the word just in case
            elif letter == " ": #checks the word
                if word == "Class": #when the word is Class
                    jump = 0
                    definition = ""
                    while self.code[jump + cursor] != "{":
                        jump += 1
                        definition += self.code[jump + cursor]
                    cursor += jump
                    definition = definition.split(" ")
                    #put tokens in parse result
                    self.parse_result.append(self.TT_CLASS) 
                    self.parse_result.append(self.TT_DEFINE)
                    for attributes in definition:
                        self.parse_result.append(attributes.strip("{")) #used strip to put '{' out of the names
                    self.parse_result.append(self.TT_END_DEFINE)
                    word = ""
                elif word == "Func": #when the word is Func
                    jump = 0
                    definition = ""
                    while self.code[jump + cursor] != "{":
                        jump += 1
                        definition += self.code[jump + cursor]
                    cursor += jump
                    definition = definition.split(" ")
                    #put tokens in parse result
                    self.parse_result.append(self.TT_FUNC) 
                    self.parse_result.append(self.TT_DEFINE)
                    for attributes in definition:
                        self.parse_result.append(attributes.strip("{")) #used strip to put '{' out of the names
                    self.parse_result.append(self.TT_END_DEFINE)
                    word = ""
                elif word == "Call": #when the word is Call
                    jump = 0
                    definition = ""
                    while self.code[jump + cursor] != "{":
                        jump += 1
                        definition += self.code[jump + cursor]
                    cursor += jump
                    definition = definition.split(" ")
                    #put tokens in parse result
                    self.parse_result.append(self.TT_CALL) 
                    self.parse_result.append(self.TT_DEFINE)
                    for attributes in definition:
                        self.parse_result.append(attributes.strip("{")) #used strip to put '{' out of the names
                    self.parse_result.append(self.TT_END_DEFINE)
                    word = ""
                else: #basically do nothing
                    pass
            
            else:
                word += letter
            cursor += 1
        return self.parse_result
    
    
if __name__ == "__main__":
    with open('Essential/test.txt', 'r') as file:
        filer = file.readlines()
        filer = ''.join(filer)


    Parser = parser(filer)
    print(Parser.parse())

            




            




            




            



            


