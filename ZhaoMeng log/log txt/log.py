import time
import os
import random


class log:
    def __init__(self):
        self.info = []
        self.time = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        self.ID = str(random.randint(0,9999))
        self.name = self.time+self.ID
        self.index = -1
        self.No_err = True
        

    def UserInput(self,UserInput):
        self.index +=1
        self.IO = ["UserInput: "+UserInput,
                   "WitOutput: "+"null",
                   "DBOutput: "+"null",
                   "CBOutput: "+"null",
                   "          ",
                    "**********"]
        self.info.append(self.IO)
        self.done()
        
    def WitOutput(self,Witoutput):
        self.info[self.index][1] = "WitOutput: "+ Witoutput
        self.done()
        
    def DatabaseOutput(self,DBOutput):
        self.info[self.index][2] = "DBOutput: "+ DBOutput
        self.done()
        
    def ChatbotOutput(self,CBOutput):
        self.info[self.index][3] = "CBOutput: "+ CBOutput
        self.done()
        
    def Problem(self):
        self.No_err = False
        temp = self.info[self.index][3]
        temp = temp + "     False"
        self.info[self.index][3] = temp
        self.done()

    def done(self):
        if self.No_err:
            self.file = open(self.name+".txt",'w')
            i = 0
            while i < len(self.info):
                for line in self.info[i]:
                    self.file.write(line)
                    self.file.write("\n")
                i+=1
            self.file.close()
                    
        if not self.No_err:
            self.file = open("E"+self.name+".txt",'w')
            i = 0
            while i < len(self.info):
                for line in self.info[i]:
                    self.file.write(line)
                    self.file.write("\n")
                i+=1
            self.file.close()
            try:
                os.remove(self.name+".txt")
            except:
                pass

    
        
        

