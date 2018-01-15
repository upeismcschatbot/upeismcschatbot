from wit import Wit
TK = "NRWGCXJR3JCF4BYZZN2LAGNKNZ7A4XEZ"
Client = Wit(access_token = TK)

while True:
    Print("Greeting, How can I help you")
    userInput = input("User: ")
    resp = Client.message(userInput)

   	while True:
            try:
   			resp['entities']['pizza']['value']
	   		except Exception as e:
	   			raise
	   		else:
	   			pass
	   		finally:
	   			pass
	print("Your ordered pizza is " + resp['entities']['pizza']['value'])