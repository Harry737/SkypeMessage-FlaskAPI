# Author: Harish R
from flask import Flask, jsonify, request
from skpy import Skype

app = Flask(__name__)

@app.route("/api/SendMessage")
def Send_Message():
    try:
        args = request.args
        print(str(args["password"]))
        mail=str(args["email"])
        passwd=str(args["password"])
        _SKYPE_ID = mail
        _SKYPE_PASS = passwd

        _CONN = Skype(_SKYPE_ID, _SKYPE_PASS)
        chats=_CONN.chats.recent()
        print(str(args["groupid"]) )
        _chat_id=str(args["groupid"]) 
        _CH = _CONN.chats[_chat_id]

        # Sending Text Message
        _CH.sendMsg(str(args["message"]))

        # For Attachment
        _CH.sendFile(open("assets/example.jpg", "rb"), "example.jpg")
        return "Message Sent!"
    except Exception as e: 
        return str(e), 500
