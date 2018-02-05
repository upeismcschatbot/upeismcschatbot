<?php
/*
*This if for the server (website) side.  There is a path to the python script and
*the python version as well.  These will need to be pathed to the correct locations on your computer
*Also note that this was written for a windows computer so the executable may be different depending
*on the operating system that you are using.
*
*This code sends a String to a python script called Chatbot_Server_Code.py and then receives an output from that 
*script and prints it out.
*/

$pyscript = 'C:\wamp64\www\chatbot\Chatbot_Server_Code.py';//This is the pathing to the python script.  Change the name and pathing as needed for your device.
$python = 'C:\Users\owner\AppData\Local\Programs\Python\Python36-32\python.exe';//most videos show people using the word "python" for this line, I found that it didn't work on my machine so giving it the direct access to the executable worked best
$userQuestion = 'I am asking about things for UPEI?';//The question that a user asks

exec("$python $pyscript $userQuestion", $response);//This is a windows executable code, it first runs python, and then a python script then passes it the argument of the users query.
	
print ($response[0]);//prints the output from the python script

?>