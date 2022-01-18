'''
    change port to the port thats not in use 
    run this code
    
    enter url as 127.0.0.1 or your ip address
'''


from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    a=["hello ","how ","are ","u"]
    return "".join(a)

app.run(port=8000)