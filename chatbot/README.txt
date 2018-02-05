First you must donload a service to host your own server.  The service I used is called WAMP.  Dowload and install so that you may run the PHP code.  

If the WAMP server doesn't turn green once you are running it (it's either yellow or red), try changing the port Apache is running on (default is 80).  To do this open WAMP, 
located near the volume controls in the bottomright on windows.  Navigate to Apache and click on httpd.conf and find the line called ServerName localhost:80 and
change it to localhost:8080.

Once the server is running go to your web browser and type in localhost/your/saved/file/pathway/chatbot/Website_Server_Code.php and you should see the desired results.