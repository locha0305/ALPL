import Essential.parser as Parser
import Essential.classes as Classes


class runtime():
    def __init__(self, code):
        self.code = code
        self.parser = Parser.parser(self.code) #get parse result
        self.code = self.parser.parse()
        print(self.code)
        #main class
        self.main = Classes.Class()
        #Class object
        self.main.add_attr("CLASS", Classes.Class)
        self.main.attributes["CLASS"].__init__(self.main.attributes["CLASS"]) #initiallize the Class class
        #Function object
        self.main.add_attr("FUNCTION", Classes.Function)
        self.main.attributes["FUNCTION"].__init__(self.main.attributes["FUNCTION"]) #initiallize the Function class
    
        self.mother = "CLASS"
        self.saved_mother = "CLASS" #save self.mother to go up
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
                if len(definition) >= 2: #when a top class exists
                    mother = self.main
                    for attr in range(len(definition) - 1):
                        mother = mother.attributes[definition[attr]] #get mother class
                    self.main.add_attr(self.daughter, self.main.attributes["CLASS"]())
                    for attr in mother.attributes:
                        self.main.attributes[self.daughter].attributes[attr] = mother.attributes[attr] #get the characteristics of it's mother class
                else:
                    self.mother = "CLASS"
                    self.main.add_attr(self.daughter, self.main.attributes["CLASS"]())
                
                
                
                
               

                self.mother = self.daughter

            elif self.current_TT == "SETATTR": #make attributes
                cursor += 1
                attr_name = self.code[cursor]
                cursor += 1
                attr_val = self.Eval(self.code[cursor])
                self.main.attributes[self.mother].attributes[attr_name] = attr_val

            elif self.current_TT == "FUNC":
                self.saved_mother = self.mother
                jump = 2
                definition = []
                while self.code[cursor + jump] != "END_DEFINE": #check for definitions
                    definition.append(self.code[cursor + jump])
                    jump += 1
                cursor += jump
                self.daughter = definition[-1] #the last thing is the name of the created Function
                self.mother = definition[0]
                if len(definition) == 2: #when a top class exists
                    pass
                else:
                    self.mother = "MAIN"

                if self.mother == "MAIN":
                    self.main.add_attr(self.daughter, self.main.attributes["FUNCTION"]())
                else:
                    self.main.attributes[self.mother].add_attr(self.daughter, self.main.attributes["FUNCTION"]())
                self.mother = self.daughter
            elif self.current_TT == "END": #when end
                self.mother = self.saved_mother
            cursor += 1
            
            
with open('Essential/test.txt', 'r') as file:
        filer = file.readlines()
        filer = ''.join(filer)
Rt = runtime(filer)
Rt.execute()
print(Rt.main.attributes)
print(Rt.main.attributes["a"].attributes)
print(Rt.main.attributes["b"].attributes)

#print(Rt.Eval('1 + 3 * 2'))
