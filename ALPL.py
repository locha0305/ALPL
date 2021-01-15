import Essential.parser as Parser
import Essential.classes as Classes


class runtime():
    def __init__(self, code):
        self.code = code
        self.parser = Parser.parser(self.code) #get parse result
        self.code = self.parser.parse()
        self.globals = {"CLASS" : Classes.Class, "FUNCTION" : Classes.Function}
    def execute(self): #this executes the code
        cursor = 0
        while cursor < len(self.code):
            self.current_TT = self.code[cursor]
            if self.current_TT == "CLASS": #handle the classes
                jump = 2
                definition = []
                while self.code[cursor + jump] != "END": #check for definitions
                    definition.append(self.code[cursor + jump])
                    jump += 1
                cursor += jump
                self.mother = definition[-1] #the last thing is the name of the created Class
                self.globals[self.mother] = self.globals["CLASS"]() #create a Class
                print(self.globals)
            elif self.current_TT == "FUNC": #handles the functions
                jump = 2
                definition = []
                while self.code[cursor + jump] != "END": #check for definitions
                    definition.append(self.code[cursor + jump])
                    jump += 1
                cursor += jump
                self.mother = definition[-1] #the last thing is the name of the created Function
                self.globals[self.mother] = self.globals["FUNCTION"]() #create a Function
                print(self.globals)
            
            cursor += 1
    
        
Rt = runtime("Class a b c d{\nFunc f{\n}\n}")
Rt.execute()

