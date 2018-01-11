from wit import Wit
access_token = "ROXAZULNLJOW2Q5QWWFD7H7Q5NSEIKPR"
client = Wit(access_token)
message_text = "who is the professof of CS481?"

resp = client.message(message_text)
entity = None
value = None

try:
	entity = list(resp['entities'])[0]
	value = resp['entities'][entity][0]['value']
except:
	pass

print(entity)
print(value)

