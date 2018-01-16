'''
Created on Jan 8, 2018

@author: owner
'''
from wit import Wit

access_token = "DGWEZ6EIADXQ6CTMRR3XAZIJUIDAFWOJ"

client = Wit(access_token = access_token)

message_text = "i want cool news"

resp = client.message(message_text)

print(resp)