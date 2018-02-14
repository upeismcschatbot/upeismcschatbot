from log import log
import time
while True:
    A = log()
    start = time.clock()
    times = input("how many times: ")
    i = 1
    while i < int(times):
        A.UserInput("the "+str(i)+"User input")
        A.WitOutput("the "+str(i)+"wit output")
        A.DatabaseOutput("the "+str(i)+"DB output")
        A.ChatbotOutput("DDD")
        if(i%2 == 0):
            A.Problem()
        i+=1


    elapsed = (time.clock() - start)
    print("Time used:",elapsed)
    
