import pandas as pd
import time
import os
import random


class log:
    def __init__(self):
        self.UI = []
        self.WI = []
        self.DO = []
        self.CO = []
        self.Err = []
        self.time = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        self.ID = str(random.randint(0,9999))
        self.name = self.time+self.ID
        self.index = -1
        self.No_err = True

    def UserInput(self,UserInput):
        self.index += 1
        self.UI.append(UserInput) 
        self.WI.append("null")
        self.DO.append("null")
        self.CO.append("null")
        self.Err.append("Pass")
        self.close()
        
    def WitOutput(self,WitInput):
        self.WI[self.index] = WitInput
        #self.close()
        
    def DatabaseOutput(self,DBOutput):
        self.DO[self.index] = DBOutput
        #self.close()
        
    def ChatbotOutput(self,CBOutput):
        self.CO[self.index] = CBOutput
        self.close()

    def close(self):
        if self.No_err:
            df = pd.DataFrame({"5.Error":self.Err,
                               "1.UserInput":self.UI,
                               "2.WitOutput":self.WI,
                               "3.DBOutput":self.DO,
                               "4.ChatBotOutput":self.CO})
            
            df.to_csv(self.name+".csv",index = True,sep = ",")
        if not self.No_err:
            df = pd.DataFrame({"5.Error":self.Err,
                               "1.UserInput":self.UI,
                               "2.WitInput":self.WI,
                               "3.DBOutput":self.DO,
                               "4.ChatBotOutput":self.CO})
            
            df.to_csv("E"+self.name+".csv",index = True,sep = ",")
            try:
                os.remove(self.name+".csv")
            except:
                pass

    def Problem(self):
        self.Err[self.index ] = "False"
        self.No_err = False
        self.close()
        
