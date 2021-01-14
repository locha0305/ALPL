import Essential.parser as Parser


class runtime():
    def __init__(self, code):
        self.code = code
        self.parser = Parser.parser(self.code) #get parse result
        self.code = self.parser.parse()
        self.globals = {}
        #tokens
        self.TT_RETURN = "RETURN"
        self.TT_DEFINE = "DEFINE"
        self.TT_END = "END"
        self.TT_SETATTR = "SETATTR"
        print(self.Eval('Return self init{input : Return void{input:Return void{input:k;};};}'))
    def execute(self): #this executes the code
        cursor = 0
        while cursor < len(self.code):
            self.current_TT = self.code[cursor]
            if self.current_TT == "CLASS":
                pass
            cursor += 1
    def Eval(self, statement):
        cursor = 0
        word = ""
        result = []
        while cursor < len(statement):
            letter = statement[cursor]
            if letter == " ":
                if word == "Return":
                    jump = 0
                    definition = ""
                    while statement[jump + cursor] != "{":
                        jump += 1
                        definition += statement[jump + cursor]
                    cursor += jump
                    definition = definition.split(" ")
                    #put tokens in parse result
                    result.append(self.TT_RETURN) 
                    result.append(self.TT_DEFINE)
                    for attributes in definition:
                        result.append(attributes.strip("{")) #used strip to put '{' out of the names
                    result.append(self.TT_END)
                    word = ""
                else:
                    pass
            elif letter == "}": #checks when a Class or a Function ends and return the certain token
                result.append(self.TT_END)
                word = "" #reset the word just in case
            elif letter == ":": #checks the define of attributes
                attr_name = word
                result.append(self.TT_SETATTR)
                result.append(attr_name)
                jump = 0
                value = ""
                while statement[jump + cursor] != ";":
                    if statement[jump + cursor] == "}":
                        jump -= 1 #therefore to check for '}'
                        break
                    else:
                        jump += 1
                        value += statement[jump + cursor]
                try:
                    if statement[cursor + jump + 1] == "}": #just therefore to handle Functions
                        result.append(self.Eval(value.strip(";") + "}")) #used strip to put ';' out of the names/also strip '}' just in case to define attributes in just one line
                    else:
                        result.append(self.Eval(value.strip(";").strip("}")))
                except IndexError:
                    result.append(self.Eval(value.strip(";").strip("}")))
                cursor += jump
                
                result.append(self.TT_END)
                word = ""
            else:
                word += letter
            cursor += 1
        return result
        
Rt = runtime("")
