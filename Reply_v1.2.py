"""
This class generates the reply sentences  
written by Dongyu Yan
Winter 2018
"""

import random


#Lists that received from Shuai's code
#Those four Lists are the only part of my code that connect with Shuai's code
#My reply sentences are fromed using data in those four lists.

#Synchronize the name of those four variables before testing.
intents=["CRS_TITLE"] #intents
speccond=["Subject","Term"] #special condition
specvalue=["Computer Science","Fall 2018"] # special value
Bydatabase=["CS 151","CS 151","CS 153","C.TBA","TBA"] #Target data from database
#Removing all objects that contains"TBA' in the Bydatabase[] list, when there is multiple objects in Bydatabase[]
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

 if intent=="CRS_TITLE"or intent=="Section Name":
    if "CRS_NAME" in speccond:
      if "NULL" in Bydatabase: #When the course title is NULL, which means the course title is not in the database
        replysentence="Sorry, I cant't find the course title of "+localspecvalue[0]
      else:    # output the result if the course title is not NULL
        a=random.randint(0,9)
        if a<5:
            replysentence =Bydatabase[n] + " is the course title of " + localspecvalue[0]
        else:
            replysentence ="The course title of "+ localspecvalue[0]+" is "+Bydatabase[n]
    elif "Falculty" in speccond and "Term" in speccond:
        for i in range(len(Bydatabase)):
            if i == len(Bydatabase) - 1:
                answer = answer + "and " + Bydatabase[i] + "."
            else:
                answer = answer + Bydatabase[i]
        if speccond[0]==Falculty:
            replysentence=localspecvalue[0]+"teaches "+ answer+" at "+localspecvalue[1]
        elif speccond[1]==Falculty:
            replysentence = localspecvalue[1] + "teaches " + answer + " at " + localspecvalue[0]
    elif "Subject" in speccond:
        if "Term" in speccond:
            answer = ""
            for i in range(len(Bydatabase)):
                if i==len(Bydatabase)-1:
                 answer=answer+"and "+Bydatabase[i]+"."
                else:
                 answer = answer + Bydatabase[i] + ", "
        if speccond[0]=="Subject":
            replysentence ="The courses of "+localspecvalue[0]+" major that are available in "+localspecvalue[1]+" semester are: "+answer
        elif speccond[0]=="Term":
            replysentence ="The courses of " + localspecvalue[1] + " major that are available in " + localspecvalue[0] + " semester are: " + answer


 # When user asking about course description
 #In this case, directly display the data from the database without adding anything, as the course description in the database is good enough
 elif intent=="CRS_DESC":
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
        replysentence =Bydatabase[n]
    else:
        replysentence ="What course's description do you want to know about?"

 #When user asking about prereqsites
 # The prereq need to be reworked.
 elif intent=="PREREQ":
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
           replysentence ="The prerequsite courses for "+localspecvalue[0]+" is: "+Bydatabase[n]


 #if the user is asking a course name
 elif intent=="CRE_NAME":
    if "CRS_TITLE" in speccond:
        replysentence ="The course name for"+localspecvalue[0]+" is "+Bydatabase[n]
   # if "Location" in speccond and "Meeting info" in speccond and "Term" in speccond:


 elif intent=="departments" :
    if "CRS_NAME" in speccond or "CRS_TITLE"in speccond:
        replysentence ="The department of the course "+localspecvalue[0]+" is "+Bydatabase[n]

 elif intent=="SUBJECT":
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
        replysentence ="The subject of the course "+localspecvalue[0]+" is "+Bydatabse[n]

 elif intent=="ACADEMIC_LEVEL":
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
        replysentence="The academic level of the course "+localspecvalue[0]+" is "+Bydatabase[n]

 elif intent=="CREDITS":
    if "CRS_NAME" in speccond or "CRS_TITLE" in speccond:
        replysentence ="The credits of the course "+localspecvalue[0]+" is "+Bydatabase[n]

 elif intent=="Location" or intent=="LOCATIONS":
    if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond and "Term" in speccond:
        for i in range(len(Bydatabase)):
            if i == len(Bydatabase) - 1:
                answer = answer + "and " + Bydatabase[i] + "."
            else:
                answer = answer + Bydatabase[i] + ", "
        if speccond[0]=="Term":
            if len (Bydatabase)==1:
             replysentence ="The loacation of the course " +localspecvalue[1]+ " of term "+localspecvalue[0]+" is "+answer
            elif len(replysentence)>1:
                replysentence = "The loacation of the course " + localspecvalue[1] + " of term " + localspecvalue[0] + " are " + answer
        elif speccond[1]=="Term":
            if len(Bydatabase)==1:
             replysentence ="The loacation of the course " + localspecvalue[0] + " of term " + localspecvalue[1] + " is " + answer
            elif len(Bydatabase)>1:
                replysentence = "The loacation of the course " + localspecvalue[0] + " of term " + localspecvalue[1] + " are " + answer


 elif intent=="Term":
    if "CRS_NAME" in speccond or "CRS_TITLE"in speccond:
       answer = ""
       for i in range(len(Bydatabase)):
            if i==len(Bydatabase)-1:
             answer=answer+"and "+Bydatabase[i]+"."
            else:
             answer = answer + Bydatabase[i] + ", "
       replysentence =localspecvalue[0]+" is offered at "+ answer


 elif intent=="Dates" :
    if "term" in speccond:
      if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond:
        if speccond[0]=="term":
            replysentence ="The dates for the course"+localspecvalue[1]+", in "+localspecvalue[0]+" semester is "+Bydatabase[n]
        elif speccond[1]=="term":
            replysentence ="The dates for the course" + localspecvalue[0] + ", in " + localspecvalue[1] + " semester is " + Bydatabase[n]

 elif intent=="Meeting info":
    if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond and "Term" in speccond:
        if speccond[0]=="Term":
            replysentence ="Here is the meeting info of the course "+localspecvalue[1]+" in "+specvalue[0]+" semester: "+Bydatabase[n]
        elif speccond[1]=="Term":
            replysentence ="Here is the meeting info of the course " + localspecvalue[0] + " in " + localspecvalue[1] + " semester: " +Bydatabase[n]

 elif intent=="Capacity":
    if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond and "Term" in speccond:
        if speccond[n]=="Term":
            replysentence ="The capacity of "+localspecvalue[1]+" in "+localspecvalue[0]+" semester is: "+Bydatabase[n]
        elif speccond[n+1]=="Term":
            replysentence ="The capacity of " + localspecvalue[0] + " in " + localspecvalue[1] + " semester is: " + Bydatabase[n]
 elif intent=="Falculty":
    if "CRS_TTTLE" in speccond or "CRS_NAME" in speccond:
        #if len(Bydatabase)==1: Assuming there is only one falculty per one class
      replysentence ="The falculty for the course "+localspecvalue[0]+" is "+Bydatabase[0]
#Unfinished: Start date, End date, Building, classroom, credit, academic level
 elif intent=="NULL":
   replysentence ="Sorry, I don't know the answer of the question you asked"
 else:
     replysentence="Whooops"
 return replysentence
#End of the reply() method


print(intents)
print(speccond)
print(specvalue)
print(Bydatabase)


if len(intents)==1:
    if len(speccond)==1:
      if len(specvalue)==1:
        print(reply(intents[0],[specvalue[0]],0))
      elif len (specvalue)>1:
       for i in range(len(specvalue)):
        print(reply(intent[0]),[specvalue[i]],i)
    elif len(speccond)>1:
       j=int(len(specvalue)/2)
       for i in range(j):
         print(reply(intents[0],[specvalue[2*i],specvalue[2*i+1]],i))
elif len(intents)==2:
  if len(speccond)==1:
    if len(specvalue)==1:
      print(reply(intents[0],[specvalue[0]],0)+", and "+reply(intents[1],[specvalue[0]],1))
    elif len(specvalue)==2:
       print (reply(intents[0],[specvalue[0]],0)+", and "+reply(intents[0],[specvalue[1]],1))
       print(reply(intents[1], [specvalue[0]], 2) + ", and " + reply(intents[1], [specvalue[1]], 3))
  elif len (speccond)==2:
        j=int(len(specvalue)/2)
       for i in range(j):
         print(reply(intents[0],[specvalue[2*i],specvalue[2*i+1]],i))
         print(reply(intents[1],[specvalue[2*i],specvalue[2*i+1]],i))
       """
       print(reply(intents[0],[specvalue[0],specvalue[1]],0))
       print(reply(intents[0], [specvalue[2], specvalue[3]], 1))
       print(reply(intents[1], [specvalue[4], specvalue[5]], 2))
       print(reply(intents[1], [specvalue[6], specvalue[7]], 3))
      """
     



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















