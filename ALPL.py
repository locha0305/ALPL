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
                self.daughter = definition[-1] #the last thing is the name of the created Class
                self.mother = definition[0]
                if len(definition) == 2: #when a top class exists
                    pass
                else:
                    self.mother = "CLASS"
                self.main.add_attr(self.daughter, self.main.attributes["CLASS"]())
                self.main.attributes[self.daughter].attributes = self.main.attributes[self.mother].attributes #get the characteristics of it's mother class
                self.main.attributes["b"].attributes = {"Y" : 1, "X" : 12 ** 3}
                print(self.main.attributes)
            cursor += 1

        
Rt = runtime("Class b{}\nClass a{}")
Rt.execute()
print(Rt.main.attributes["a"].attributes)


