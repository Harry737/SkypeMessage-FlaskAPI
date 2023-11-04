from flask import Flask, jsonify, request
from skpy import Skype

try:
     
    mail=str('test@mail.com') # Skype Mail
    passwd=str('skype-password') # Skype Password
    _SKYPE_ID = mail
    _SKYPE_PASS = passwd

    _CONN = Skype(_SKYPE_ID, _SKYPE_PASS)
    
    chats=_CONN.chats.recent() # Get the groupid or chat id(person or group you want to send message) by printing chats or debugging it

    _chat_id='8:live:.cid.e7843...' # Example Chat ID

    # Example Group ID _group_id = 19:3df56f2a2a...@thread.skype

    _CH = _CONN.chats[_chat_id]

    # Sending Text Message
    _CH.sendMsg('Test123') # Message To be Sent

    # For Attachment
    _CH.sendFile(open("assets/example.jpg", "rb"), "example.jpg")
    print("Message Sent!")     
except Exception as e: 
    print(str(e)) 