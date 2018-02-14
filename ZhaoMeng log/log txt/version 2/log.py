import time
import os
import random


class log:
    # construction
    def __init__(self):
        self.info = []
        self.TIMES = str(time.strftime("%Y"+"-"+"%m"+"-"+"%d"+"-"+"%H"+"-"+"%M"+"-"+"%S"+"-",
                                      time.localtime()))#get the time 
        self.ID = str(random.randint(0,9999))#get the ID
        self.name = self.TIMES+self.ID#combina ID and time
        self.No_err = True#no error signal, when user do not like the answer CB made, this will turn to false
        """self.UserInput = "Null"
        self.Witoutput = "Null"
        self.DBOutput = "Null"
        self.CBOutput = "Null"
        """
        self.temp = "null"
        
    # the argu is the user input
    def UserInput(self,UserInput):
        #self.UserInput = UserInput
        if self.No_err:#no error case
            self.file=open(self.name+".txt",'a')#open the file
            self.file.write("UserInput: "+ UserInput)#write in
            self.file.write("\n")#for the format, write in
            self.file.close()#close the file
            #self.UserInput = "Null"
        if not self.No_err:#error case
            self.file=open("E-"+self.name+".txt",'a')
            self.file.write("UserInput: "+ UserInput)
            self.file.write("\n")
            self.file.close()
            #self.UserInput = "Null"
            
    # the argu is the wit ai output    
    def WitOutput(self,Witoutput):
        #self.Witoutput = Witoutput
        if self.No_err:
            self.file=open(self.name+".txt",'a')
            self.file.write("WitOutput: "+Witoutput)
            self.file.write("\n")
            self.file.close()
            #self.Witoutput = "Null"
        if not self.No_err:
            self.file=open("E-"+self.name+".txt",'a')
            self.file.write("WitOutput: "+Witoutput)
            self.file.write("\n")
            self.file.close()
            #self.Witoutput = "Null"
            
    # the argu is the database output 
    def DatabaseOutput(self,DBOutput):
        #self.DBOutput = DBOutput
        if self.No_err:
            self.file=open(self.name+".txt",'a')
            self.file.write("DBOutput : "+DBOutput)
            self.file.write("\n")
            self.file.close()
            #self.DBOutput = "Null"
        if not self.No_err:
            self.file=open("E-"+self.name+".txt",'a')
            self.file.write("DBOutput : "+DBOutput)
            self.file.write("\n")
            self.file.close()
            #self.DBOutput = "Null"
            
    # the argu is the chatbot output 
    def ChatbotOutput(self,CBOutput):
        
        #self.CBOutput = CBOutput# when the user do not like the answer, another method will get the output of CB
        self.temp = CBOutput
        if self.No_err:# no error case
            self.file=open(self.name+".txt",'a')# open the file
            self.file.write("CBOutput : "+ CBOutput)# write the file
            self.file.write("\n")# for the format
            self.file.write("\n")
            self.file.write("**********")
            self.file.write("\n")
            self.file.close()#close the file
            
        if not self.No_err:
            self.file=open("E-"+self.name+".txt",'a')
            self.file.write("CBOutput : "+ CBOutput)
            self.file.write("\n")
            self.file.write("\n")
            self.file.write("**********")
            self.file.write("\n")
            self.file.close()
        
        
    # a method used to detect the problem
    def Problem(self):
        if self.No_err:#if this the first error case
            self.file=open(self.name+".txt",'r+')
        if not self.No_err:# if this is the second error case
            self.file=open("E-"+self.name+".txt",'r+')
            
        flist=self.file.readlines()# get what information the file have 
        self.file.close()#close the file
        flist[len(flist)-3]="CBOutput : "+ self.temp+ "   False"
        flist[len(flist)-2]="\n \n"#for the format
        flist[len(flist)-1]="**********"
        

        self.file=open("E-"+self.name+".txt",'w+')#re-open the file, write something new
        self.file.writelines(flist)# write the after-fix information to the file
        self.file.write("\n")# for the format
        self.file.close()#close the file 
        self.No_err = False#change the no-error signal to false
        
        try:
            os.remove(self.name+".txt")#remove the old version of the file
        except:
            pass#the only exception will happeed is no the old version file already be delete. so pass it
            
       


