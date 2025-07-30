from flask import Flask 
import os 

appp=Flask(__name__)

@appp.route("/")
def hello():
    return  "HELLO WORLD"

if __name__=="__main__":
    port=int(os.envron.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
