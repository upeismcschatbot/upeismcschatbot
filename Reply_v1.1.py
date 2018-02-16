"""
This class generates the reply sentences  
written by Dongyu Yan
Winter 2018
"""

import random


#Lists that received from Shuai's code
#Those four Lists are the only part of my code that connect with Shuai's code
#My reply sentences are fromed using data in those four lists.
intents=["CRS_TITLE"] #intents
speccond=["Subject","Term"] #special condition
specvalue=["Computer Science","Fall 2018"] # special value
Bydatabase=["CS 151","CS 152","CS 153"] #Target data from database
intetn=""


replysentence=""
intentcounter=0

#When user asking a course titile
#Sample user input: " "\
def reply (intent):
 if "CRS_TITLE" in intents:
    if "CRS_NAME" in speccond:
      if "NULL" in Bydatabase: #When the course title is NULL, which means the course title is not in the database
        replysentence="Sorry, I cant't find the course title of "+specvalue[0]
      elif len(specvalue)==2:
        replysentence="The course title of " +specvalue[0]+" is "+Bydatabsse[0]+", and the course title of "+specvalue[1]+" is "+Bydatabse[1]
      else:    # output the result if the course title is not NULL
        a=random.randint(0,9)
        if a<5:
            replysentence =Bydatabase[0] + " is the course title of " + specvalue[0]
        else:
            replysentence ="The course title of "+ specvalue[0]+" is "+Bydatabase[0]


    if "Subject" in speccond:
        if "Term" in speccond:
            answer = ""
            for i in range(len(Bydatabase)):
                if i==len(Bydatabase)-1:
                 answer=answer+"and "+Bydatabase[i]+"."
                else:
                 answer = answer + Bydatabase[i] + ", "
        if speccond[0]=="Subject":
            replysentence ="The courses of "+specvalue[0]+" major that are available in "+specvalue[1]+" semester are: "+answer
        elif speccond[0]=="Term":
            replysentence ="The courses of " + specvalue[1] + " major that are available in " + specvalue[0] + " semester are: " + answer

 # When user asking about course description
 #In this case, directly display the data from the database without adding anything, as the course description in the database is good enough
 if "CRS_DESC" in intents:
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
        replysentence =Bydatabase[0]
    else:
        replysentence ="What course's description do you want to know about?"

 #When user asking about prereqsites
 # The prereq need to be reworked.
 if "PREREQ" in intents:
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
     if len(Bydatabase)==3:
       a=random.randint(0,9)
       if a<5:
           replysentence ="The prerequsite courses for "+specvalue[0]+" are: "+Bydatabase[0]+", "+ Bydatabase[1]+", and "+Bydatabase[2]
       else:
           replysentence =Bydatabase[0]+", "+Bydatabase[1]+", "+Bydatabase[2]+" are the prerequsite courses for "+specvalue[0]
     elif len(Bydatabase)==2:
         a = random.randint(0, 9)
         if a < 5:
             replysentence ="The prerequsite courses for " + specvalue[0] + " are: " + Bydatabase[0] + " and " + Bydatabase[1]
         else:
             replysentence =Bydatabase[0]+" and "+Bydatabase[1]+" are the prerequsite courses for "+specvalue[0]
     elif len(Bydatabase)==1:
         replysentence ="The prerequisite course for "+speccond[0]+" is "+Bydatabase[0]
     elif len(Bydatabase)==0: #if there isnt any prereqsites
         replysentence ="There is no prerequiste courses for "+ speccond[0]

 #if the user is asking a course name
 if "CRE_NAME"in intents:
    if "CRS_TITLE" in speccpnd:
        replysentence ="The course name for"+specvalue[0]+" is "+Bydatabase[0]
   # if "Location" in speccond and "Meeting info" in speccond and "Term" in speccond:


 if "departments" in intents:
    if "CRS_NAME" in speccond or "CRS_TITLE"in speccond:
        replysentence ="The department of the course "+specvalue[0]+" is "+Bydatabase[0]

 if "SUBJECT" in intents:
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
        replysentence ="The subject of the course "+specvalue[0]+" is "+Bydatabse[0]

 if "ACADEMIC_LEVEL" in intents:
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
        replysentence="The academic level of the course "+specvalue[0]+" is "+Bydatabase[0]

 if "CREDITS" in intents:
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
        replysentence ="The credits of the course "+specvalue[0]+" is "+Bydatabase[0]

 if "Location" in intents:
    if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond and "Term" in speccond:
        if speccond[0]=="Term":
            replysentence ="The loacation of the course " +specvalue[1]+ " of term "+specvalue[0]+" is "+Bydatabase[0]
        elif speccond[1]=="Term":
            replysentence ="The loacation of the course " + specvalue[0] + " of term " + specvalue[1] + " is " + Bydatabase[0]


 if "Term" in intents:
    if "CRS_NAME" in speccond or "CRS_TITLE"in speccond:
       answer = ""
       for i in range(len(Bydatabase)):
            if i==len(Bydatabase)-1:
             answer=answer+"and "+Bydatabase[i]+"."
            else:
             answer = answer + Bydatabase[i] + ", "
       replysentence =specvalue[0]+" is offered at "+ answer


 if "Dates" in intents:
    if "term" in speccond:
      if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond:
        if speccond[0]=="term":
            replysentence ="The dates for the course"+speccond[1]+", in "+speccond[0]+" semester is "+Bydatabase[0]
        elif speccond[1]=="term":
            replysentence ="The dates for the course" + speccond[0] + ", in " + speccond[1] + " semester is " + Bydatabase[0]

 if "Meeting info" in intents:
    if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond and "Term" in speccond:
        if speccond[0]=="Term":
            replysentence ="Here is the meeting info of the course "+specvalue[1]+" in "+specvalue[0]+" semester: "+Bydatabase[0]
        elif speccond[1]=="Term":
            replysentence ="Here is the meeting info of the course " + specvalue[0] + " in " + specvalue[0] + " semester: " +Bydatabase[1]

 if "Capacity" in intents:
    if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond and "Term" in speccond:
        if speccond[0]=="Term":
            replysentence ="The capacity of "+specvalue[1]+" in "+specvalue[0]+" semester is: "+Bydatabase[0]
        elif speccond[1]=="Term":
            replysentence ="The capacity of " + specvalue[0] + " in " + specvalue[1] + " semester is: " + Bydatabase[0]
 if "Falculty" in intents:
    if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond:
        if len(Bydatabase)==1:
            replysentence ="The falculty for the course "+specvalue[0]+" is "+Bydatabase[0]
        elif len(Bydatabase)>=1:
            answer = ""
            for i in range(len(Bydatabase)):
                if i==len(Bydatabase)-1:
                  answer=answer+"and "+Bydatabase[i]+"."
                else:
                  answer = answer + Bydatabase[i] + ", "
                replysentence ="The instructors of for the course "+specvalue[0]+" are "+answer
                 
"""
 When "NULL" in intents, which means the chat bot did not understand the question
"""
if "NULL" in intents:
  replysentence ="Sorry, I don't know the answer of the question you asked"

if len(intents)==1:

 print(replysentence)

"""
New columns: Start Date, End Date, Building, Classrooms, Start time, End time 


New type of questions: Does/Yes or no question; "How many": scan the user's input

Reedit prereqsites
Reedit dates: From DD/MM/YYYY to words
Multiple intents: 
add a counter after each if, if counter > 1, add ",and" between two sentences. 
Store the sentences into variables>

If multiple answers, delete all items that contains TBA, (to be announced).ignorecase, if TBA in single answer, print "not decided"

"""















