"""
This class generates the reply sentences  
written by Dongyu Yan
Winter 2018
"""

import random
import datetime
#from log import log
#Lists that received from Shuai's code
#Those four Lists are the only part of my code that connect with Shuai's code
#My reply sentences are fromed using data in those four lists.
class fs:
    def rfs(self,ints, specond, val, ans, userinput,fun):
        #slog=log()
        #Synchronize the name of those four variables before testing.
        intents=ints #["CRS_TITLE"] #intents
        speccond=specond #["Subject","Term"] #special condition
        specvalue=val #["Computer Science","Fall 2018"] # special value
        Bydatabase=ans #["CS 151","CS 151","CS 153","C.TBA","TBA"] #Target data from database

        greeting=["hello", "hi", "good morning", "good afternoon", "good evening", "nice to meet you","Hello"]
        farewell=["bye", "byebye", "good bye", "goodbye", "see you", "see you next time"]
        HowRU=["how are you","How r u?","how are u","how are you?"]

        unsolve=["what are the time and location of cs1910 at 2017 fall semester?",
                  "how many offerings of cs1910 are there in fall 2018?",
                  "what are the time and location of cs 2820 at 2017 fall?",
                   "what are the time of cs1910 and cs1920 at 2018 fall semester?",
                   "what are the time of cs1910 at 2017 fall semester and cs1920 at 2018 winter semester?",
                    "what are the time of cs1910 at 2018 fall semester and cs1920 at 2018 winter semester","time and location?",
                    "what are  the time of cs1910 at 2017 fall and 2018 winter? ","what are the time of cs1910 and cs1920 at 2018 winter semester?"]
        if "Start Date" in intents or "End Date" in intents:
          new_Bydatabase=[]
          for datetime in Bydatabase:
            new_Bydatabase.append(datetime.strftime("%B %d, %Y"))
          Bydatabase=new_Bydatabase  
        else:
          new_Bydatabase=[]
          for item in Bydatabase:
            new_Bydatabase.append(str(item))
          Bydatabase=new_Bydatabase






        if (len(Bydatabase))>1:
         new_Bydatabase=[]
         for object in Bydatabase:
            if object.find("TBA")==-1:
                new_Bydatabase.append(object)
         Bydatabase=new_Bydatabase
        #End of removing "TBA"
        
        # Removing repeatitive contents in Bydatabase
        new_Bydatabase=[]
        for object in Bydatabase:
            if object not in new_Bydatabase:
                new_Bydatabase.append(object)
        Bydatabase=new_Bydatabase
        #End of removing repeatitive contents     
        def reply (intent,localspecvalue,n):
         #replysentence=""    
         answer=""
         if len(Bydatabase)>1:
            for k in range(len(Bydatabase)):
              if k == len(Bydatabase) - 1:
                answer = answer + "and " + Bydatabase[k] + "."
              else:
                answer = answer + Bydatabase[k] + ", "
         elif len(Bydatabase)==1:
            answer=Bydatabase[0]
         else:
            answer=""   
         replysentence="Something is wrong."
         if intent=="CRS_TITLE"or intent=="Short Title":
            if "CRS_NAME" in speccond or "Section Name" in speccond:
              if "NULL" in Bydatabase: #When the course title is NULL, which means the course title is not in the database
                replysentence="Sorry, I cant't find the course title of "+localspecvalue[0]
              else:    # output the result if the course title is not NULL
                a=random.randint(0,9)
                if a<5:
                    replysentence =Bydatabase[n] + " is the course title of " + localspecvalue[0]
                else:
                    replysentence ="The course title of "+ localspecvalue[0]+" is "+Bydatabase[n]
            elif "Faculty" in speccond and "Term" in speccond:
                answer=""
                for k in range(len(Bydatabase)):
                  if len(Bydatabase)>1:
                    if k == len(Bydatabase) - 1:
                        answer = answer + "and " + Bydatabase[k] + "."
                    else:
                        answer = answer + Bydatabase[k]+","
                  elif len (Bydatabase)==1:
                    answer=Bydatabase[0]      
                if speccond[0]=="Faculty":
                    replysentence=localspecvalue[0]+" teaches "+ answer+" at "+localspecvalue[1]
                elif speccond[1]=="Faculty":
                    replysentence = localspecvalue[1] + " teaches " + answer + " at " + localspecvalue[0]
            elif "Subject" in speccond:
                if "Term" in speccond:
                  if len(Bydatabase)>1:
                    answer = ""
                    for k in range(len(Bydatabase)):
                     if k==len(Bydatabase)-1:
                      answer=answer+"and "+Bydatabase[k]+"."
                     else:
                      answer = answer + Bydatabase[k] + ", "
                  elif len(Bydatabase)==1:
                    answer=Bydatabase[0]    
                if speccond[0]=="Subject" or speccond[0]=="SUBJECT":
                 replysentence ="The courses of "+localspecvalue[0]+" major that are available in "+localspecvalue[1]+" semester are: "+answer
                elif speccond[0]=="Term":
                 replysentence ="The courses of " + localspecvalue[1] + " major that are available in " + localspecvalue[0] + " semester are: " + answer
         elif intent=="CRS_DESC" or intent=="Description":
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             replysentence =Bydatabase[n]
            else:
             replysentence ="What course's description do you want to know about?"

         #When user asking about prereqsites
         # The prereq need to be reworked.
         elif intent=="PREREQ" or intent=="Prereqsites":
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             replysentence ="The prerequsite courses for "+localspecvalue[0]+" is: "+Bydatabase[n]


         #if the user is asking a course name
         elif intent=="CRS_NAME" or intent=="Section Name":
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             replysentence ="The course name for "+localspecvalue[0]+" is "+Bydatabase[n]
           # if "Location" in speccond and "Meeting info" in speccond and "Term" in speccond:
          

         elif intent=="departments" or intent=="DEPARTMENT_1":
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             replysentence ="The department of the course "+localspecvalue[0]+" is "+Bydatabase[n]

         elif intent=="SUBJECT" or intent=="Subject":
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             replysentence ="The subject of the course "+localspecvalue[0]+" is "+Bydatabase[n]

         elif intent=="ACADEMIC_LEVEL" or intent=="Academic Level":
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             replysentence="The academic level of the course "+localspecvalue[0]+" is "+Bydatabase[n]

         elif intent=="CREDITS" or intent=="Credits":
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             replysentence ="The credits of the course "+localspecvalue[0]+" is "+Bydatabase[n]

         elif intent=="Location" or intent=="LOCATIONS":
            if "Term" in speccond:
             if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
              if len(intents)==1:
               answer=""
               if len (Bydatabase)>1:
                for k in range(len(Bydatabase)):
                    if k == len(Bydatabase) - 1:
                     answer = answer + "and " + Bydatabase[k] + "."
                    else:
                     answer = answer + Bydatabase[k] + ", "
               elif len(Bydatabase)==1:
                answer=Bydatabase[0]       
               if speccond[0]=="Term":
                if len (Bydatabase)==1:
                 replysentence ="The location of the course " +localspecvalue[1]+ " of term "+localspecvalue[0]+" is "+answer
                elif len(replysentence)>1:
                 replysentence = "The location of the course " + localspecvalue[1] + " of term " + localspecvalue[0] + " are " + answer
               elif speccond[1]=="Term":
                if len(Bydatabase)==1:
                 replysentence ="The location of the course " + localspecvalue[0] + " of term " + localspecvalue[1] + " is " + answer
                elif len(Bydatabase)>1:
                 replysentence = "The location of the course " + localspecvalue[0] + " of term " + localspecvalue[1] + " are " + answer
              elif len(intents)==2:
                answer="" 
                if intents[0]=="Location" or intents[0]=="LOCATIONS":
                  j=int(len(intents)/2)
                  for k in range(j):
                    if k==j-1:
                     answer=answer+" and "+Bydatabase[2*k]+". "
                    else:
                     answer=answer+Bydatabase[2*k]+". "
                elif intents[1]=="Location" or intents[1]=="LOCATIONS":
                  j=int(range(len(intents))/2)
                  for k in range(j):
                    if k==j-1:
                     answer=answer+" and "+Bydatabase[2*k+1]+". "
                    else:
                     answer=answer+Bydatabase[2*k+1]+", "
                if speccond[0]=="Term":
                 replysentence="The location of the course "+localspecvalue[1]+" of term "+localspecvalue[0]+" are "+answer
                elif speccond[1]=="Term":
                 replysentence="The location of the course "+localspecvalue[0]+" of term "+localspecvalue[1]+" are "+answer
            elif  "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
              if len(specvalue)==1:
               replysentence="The location of the course "+specvalue[0]+" is "+answer
              elif len(specvalue)==2:
                replysentence="The location of the course"+specvalue[0]+" and "+specvalue[1]+" are "+answer



         elif intent=="Term":
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             answer = ""
             if len(Bydatabase)>1:
              for k in range(len(Bydatabase)):
               if k==len(Bydatabase)-1:
                answer=answer+"and "+Bydatabase[k]+"."
               else:
                answer = answer + Bydatabase[k] + ", "
             elif len(Bydatabase)==1:
                answer=Bydatabase[0]
             replysentence =localspecvalue[0]+" is offered at "+ answer   

         elif intent=="Dates" :
            if "Term" in speccond:
              if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
                if speccond[0]=="Term":
                 replysentence ="The dates for the course "+localspecvalue[1]+", in "+localspecvalue[0]+" semester is "+Bydatabase[n]
                elif speccond[1]=="Term":
                 replysentence ="The dates for the course " + localspecvalue[0] + ", in " + localspecvalue[1] + " semester is " + Bydatabase[n]

         elif intent=="Meeting Info":
            if "Term" in speccond:
              if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
                if speccond[0]=="Term":
                 replysentence ="Here is the meeting info of the course "+localspecvalue[1]+" in "+specvalue[0]+": "+answer
                elif speccond[1]=="Term":
                 replysentence ="Here is the meeting info of the course " + localspecvalue[0] + " in " + localspecvalue[1] + ": " +answer
                elif speccond[2]=="Term":
                 replysentence="Here is the meeting info of the course"+localspecvalue[0]+" and "+ localspecvalue[1]+" in "+localspecvalue[2]+": "+answer
            elif "Section Name"in speccond:
              replysentence=""
              for i in range(len(specvalue)):
               replysentence=replysentence+"The meeting info of the course "+localspecvalue[i]+" is: "+answer+ "\n"    

         elif intent=="Capacity":
          if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
            answer=""
            if len(Bydatabase)>1:
                for k in range(len(Bydatabase)):
                    if k == len(Bydatabase) - 1:
                     answer = answer + "and " + Bydatabase[k] + "."
                    else:
                     answer = answer + Bydatabase[k] + ", "
            elif len(Bydatabase)==1: 
              answer=Bydatabase[0]         
            if "Term" in speccond:
                if speccond[2*n]=="Term":
                 replysentence ="The capacity of "+localspecvalue[1]+" in "+localspecvalue[0]+" semester is: "+answer
                elif speccond[2*n+1]=="Term":
                 replysentence ="The capacity of " + localspecvalue[0] + " in " + localspecvalue[1] + " semester is: " + answer
            else:
              replysentence="The capacity of "+ localspecvalue[0]+" are "+answer

         elif intent=="Faculty":
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             replysentence ="The faculty for the course "+localspecvalue[0]+" is "+answer
             
         elif intent=="Instruction Methods":
            answer=""
            if len (Bydatabase)>1:
              for k in range(len(Bydatabase)):
                if k == len(Bydatabase) - 1:
                 answer = answer + "and " + Bydatabase[k] + "."
                else:
                  answer = answer + Bydatabase[k] + ", "
            elif len(Bydatabase)==1:
                answer=Bydatabase[0] 
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
             if "Term" in speccond: 
              if speccond[0]=="Term":
               replysentence="The instruction method of the course "+localspecvalue[1]+" on "+localspecvalue[0]+" is "+answer
              elif speccond[1]=="Term":
               replysentence="The instruction method of the course "+localspecvalue[0]+" on "+localspecvalue[1]+" is "+answer 
             else:
              replysentence="The instruction method of the course "+localspecvalue[0]+" are: "+answer   
         elif intent=="Classrooms":
          if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
              answer=""
              if len(Bydatabase)>1:
                for k in range(len(Bydatabase)):
                    if k == len(Bydatabase) - 1:
                     answer = answer + "and " + Bydatabase[k] + "."
                    else:
                     answer = answer + Bydatabase[k] + ", "
              elif len(Bydatabase)==1:
                answer=Bydatabase[0]      
              if "Term" in speccond:
                if speccond[0]=="Term":
                 replysentence="The Classrooms of the course "+localspecvalue[1]+" on "+localspecvalue[0]+" is "+answer
                elif speccond[1]=="Term":
                 replysentence="The Classrooms of the course "+localspecvalue[0]+" on "+localspecvalue[1]+" is "+answer  
              else: 
               replysentence="The classrooms of the course "+localspecvalue[0]+" are "+answer
         elif intent=="Buildings":
           if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
               answer=""
               if len (Bydatabase)>1:
                 for k in range(len(Bydatabase)):
                    if k == len(Bydatabase) - 1:
                     answer = answer + "and " + Bydatabase[k] + "."
                    else:
                     answer = answer + Bydatabase[k] + ", "
               elif len(Bydatabase)==1:
                answer=Bydatabase[0]      
               if "Term" in speccond:
                if len(speccond)>1:
                 if speccond[0]=="Term":
                  replysentence="The building of the course "+localspecvalue[1]+" on "+localspecvalue[0]+" is "+answer
                 elif speccond[1]=="Term":
                   replysentence="The building of the course "+localspecvalue[0]+" on "+localspecvalue[1]+" is "+answer  
               else: 
                 replysentence="The buildings of the course "+localspecvalue[0]+" are "+answer
            


         elif intent=="Start Time":
            answer=""
            if len (Bydatabase)>1:
              for k in range(len(Bydatabase)):
                if k == len(Bydatabase) - 1:
                  answer = answer + "and " + Bydatabase[k] + "."
                else:
                  answer = answer + Bydatabase[k] + ", "
            elif len(Bydatabase)==1:
              answer=Bydatabase[0]
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
              if "Term" in speccond:
                if speccond[0]=="Term":
                 replysentence="The Start time the course "+localspecvalue[1]+" on "+localspecvalue[0]+" are "+answer
                elif speccond[1]=="Term":
                 replysentence="The start time of the course "+localspecvalue[0]+" on "+localspecvalue[1]+" are "+answer
              else:
               replysentence="The start time of the course "+localspecvalue[0]+" are "+answer 

         elif intent=="End Time":
            answer=""
            if len (Bydatabase)>1:
              for k in range(len(Bydatabase)):
                if k == len(Bydatabase) - 1:
                  answer = answer + "and " + Bydatabase[k] + "."
                else:
                  answer = answer + Bydatabase[k] + ", "
            elif len(Bydatabase)==1:
              answer=Bydatabase[0]
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
              if "Term" in speccond:
                if speccond[0]=="Term":
                 replysentence="The end time the course "+localspecvalue[1]+" on "+localspecvalue[0]+" are "+answer
                elif speccond[1]=="Term":
                 replysentence="The end time of the course "+localspecvalue[0]+" on "+localspecvalue[1]+" are "+answer
              else:
               replysentence="The end time of the course "+localspecvalue[0]+" are "+answer 

         elif intent=="Start Date":
            answer=""
            if len (Bydatabase)>1:
              for k in range(len(Bydatabase)):
                if k == len(Bydatabase) - 1:
                  answer = answer + "and " + Bydatabase[k] + "."
                else:
                  answer = answer + Bydatabase[k] + ", "
            elif len(Bydatabase)==1:
              answer=Bydatabase[0]
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
              if "Term" in speccond:
                if speccond[0]=="Term":
                 replysentence="The Start date the course "+localspecvalue[1]+" on "+localspecvalue[0]+" are "+answer
                elif speccond[1]=="Term":
                 replysentence="The start date of the course "+localspecvalue[0]+" on "+localspecvalue[1]+" are "+answer
              else:
               replysentence="The start dates of the course "+localspecvalue[0]+" are "+answer 

         elif intent=="End Date":
            answer=""
            if len (Bydatabase)>1:
              for k in range(len(Bydatabase)):
                if k == len(Bydatabase) - 1:
                  answer = answer + "and " + Bydatabase[k] + "."
                else:
                  answer = answer + Bydatabase[k] + ", "
            elif len(Bydatabase)==1:
              answer=Bydatabase[0]
            if "CRS_NAME" in speccond or "CRS_TITLE" in speccond or "Short Title" in speccond or "Section Name" in speccond:
              if "Term" in speccond:
                if speccond[0]=="Term":
                 replysentence="The end date the course "+localspecvalue[1]+" on "+localspecvalue[0]+" are "+answer
                elif speccond[1]=="Term":
                 replysentence="The end date of the course "+localspecvalue[0]+" on "+localspecvalue[1]+" are "+answer
              else:
               replysentence="The end dates of the course "+localspecvalue[0]+" are "+answer 
         else:
          replysentence="Whooops"
         return replysentence
        #End of the reply() method
        unsol=""
        print("intents:")
        print(intents)
        print("Special condition:")
        print(speccond)
        print("Special value:")
        print(specvalue)
        print("Answer:")
        print(Bydatabase)
        
        finalreply=""

        for sentence in unsolve:
         if userinput.lower().find(sentence)!=-1:
          unsol="a"
        if len(Bydatabase)==0 or len(intents)==0 or len(speccond)==0 or len(specvalue)==0 or Bydatabase[0]=="NULL":
          finalreply="SMCS BOT: "+"Sorry, I don't know the answer of the question you asked."   
        elif unsol=="a" or len(userinput)>66:
          for item in Bydatabase:
            finalreply="SMCS BOT: "+item+"\n"  
        elif userinput in greeting or userinput in farewell:
          print (userinput)
        elif userinput in HowRU:
          finalreply="SMCS BOT: "+"I'm good."
        elif len(intents)==1:
            if len(speccond)==1:
              if len(specvalue)==1:
                finalreply="SMCS BOT: "+reply(intents[0],[specvalue[0]],0)
              elif len (specvalue)>1:
               for i in range(len(specvalue)):
                finalreply="SMCS BOT: "+reply(intent[0]),[specvalue[i]],i
            elif len(speccond)==2:
              finalreply="SMCS BOT: "+reply(intents[0],[specvalue[0],specvalue[1]],0)
            elif len(speccond)==3:
              finalreply=reply(intents[0],[specvalue[0],specvalue[1],specvalue][2],0)
                   
        elif len(intents)==2:
          if len(speccond)==1:
            if len(specvalue)==1:
              finalreply="SMCS BOT: "+reply(intents[0],[specvalue[0]],0)+", and "+reply(intents[1],[specvalue[0]],1)
            elif len(specvalue)==2:
               finalreply="SMCS BOT: "+reply(intents[0],[specvalue[0]],0)+", and "+reply(intents[0],[specvalue[1]],1)+"\n"
               +"SMCS BOT: "+reply(intents[1], [specvalue[0]], 2) + ", and " + reply(intents[1], [specvalue[1]], 3)
          elif len (speccond)==2:
               j=int(len(specvalue)/2)
               for i in range(j):
                 finalreply="SMCS BOT: "+reply(intents[0],[specvalue[2*i],specvalue[2*i+1]],i)
                 finalreply="SMCS BOT: "+reply(intents[1],[specvalue[2*i],specvalue[2*i+1]],i)

        
        print finalreply             
        fun(finalreply)
        return finalreply
               
             

 

"""
New type of questions: Does/Yes or no question; "How many": scan the user's input

R
Multiple intents: 



If multiple answers, delete all items that contains TBA, (to be announced).ignorecase, if TBA in single answer, print "not decided"

"""















