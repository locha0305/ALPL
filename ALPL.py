import Essential.parser as Parser
import Essential.classes as Classes


class runtime():
    def __init__(self, code):
        self.code = code
        self.parser = Parser.parser(self.code) #get parse result
        self.code = self.parser.parse()
        #Class
        self.main = Classes.Class()
        #Class object
        self.main.add_attr("CLASS", Classes.Class)
        self.main.attributes["CLASS"].__init__(self.main.attributes["CLASS"]) #initiallize the Class class
    def Eval(self, statement):
        statement += " " #just in case to check the last value
        self.operator = ['+', '-', '*', '^', '%', ' ']
        eval_result = []
        cursor = 0
        word = ""
        while cursor < len(statement):
            letter = statement[cursor]
            if letter in self.operator:
                if word in self.main.attributes[self.mother].attributes: #when attribute
                    attr_value = self.main.attributes[self.mother].attributes[word]
                    eval_result.append(str(attr_value)) #str to eval
                    eval_result.append(letter) #append operator
                else:
                    eval_result.append(word) #append the number
                    eval_result.append(letter) #append operator
                word = ""
                    
            else:
                word += letter
            cursor += 1
        return eval(''.join(eval_result))

    def execute(self): #this executes the code
        cursor = 0
        while cursor < len(self.code):
            self.current_TT = self.code[cursor]
            if self.current_TT == "CLASS": #handle the classes
                jump = 2
                definition = []
                while self.code[cursor + jump] != "END_DEFINE": #check for definitions
                    definition.append(self.code[cursor + jump])
                    jump += 1
                cursor += jump
                self.daughter = definition[-1] #the last thing is the name of the created Class
                self.mother = definition[0]
                if len(definition) == 2: #when a top class exists
                    pass
                else:
                    self.mother = "CLASS"
                self.main.add_attr(self.daughter, self.main.attributes["CLASS"]())
                self.main.attributes[self.daughter].attributes = self.main.attributes[self.mother].attributes #get the characteristics of it's mother class
                self.mother = self.daughter
                self.main.attributes["b"].attributes = {"Y" : 1, "X" : 12 ** 3}
                print(self.main.attributes, self.mother)
            elif self.current_TT == "SETATTR": #make attributes
                cursor += 1
                attr_name = self.code[cursor]
                cursor += 1
                attr_val = self.Eval(self.code[cursor])
                self.main.attributes[self.mother].add_attr(attr_name, attr_val)
                
            cursor += 1

        
Rt = runtime("Class b{c : 2\nd : 2 + 4 * 2}\nClass a{x : 12.1 * 2\ny : 12 * 2\nz: x+3}")
Rt.execute()
print(Rt.main.attributes["b"].attributes, Rt.main.attributes["a"].attributes)
#print(Rt.Eval('1 + 3 * 2'))



