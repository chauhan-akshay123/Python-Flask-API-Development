from flask import Flask, request, jsonify

app = Flask(__name__)

# Welcome
def getWelcomeMessage():
    return "We will now learn functions!"

@app.route("/welcome", methods=["GET"])
def welcome():
    return getWelcomeMessage()

# get greeting Message
def getGreetingMessage(username):
    return f"Hey, John! Are you ready to learn functions with us?"

@app.route("/greet", methods=["GET"])
def greet():
    username = request.args.get("username", "")
    return getGreetingMessage(username)

# Check Experience
def checkYearsOfExp(years):
    if years > 0:
       result = "you have some experience with functions. Great!"
    else:
       result = "No worries."    
    return result    

@app.route("/message", methods=["GET"])
def message():
    yearsOfExp = float(request.args.get("yearsOfExp", 0))
    return checkYearsOfExp(yearsOfExp)

# Available time
def getTime(days, hours):
    return days * hours

@app.route("/hours", methods=["GET"])
def hours():
    days = int(request.args.get("days", 0))
    hours = int(request.args.get("hours", 0))
    return str(getTime(days, hours))

# Module completion status
def getModuleCompletion(username, hasCompleted):
    if hasCompleted:
       result = f"{username} has completed the modules"
    else:
       result = f"{username} has not yet completed the modules." 
    return result 

@app.route("/module-completion-status", methods=["GET"])
def completion():
    username = request.args.get("username", "")
    hasCompleted = request.args.get("hasCompleted", "false") == "true"
    return getModuleCompletion(username, hasCompleted)      

# Personalized Greeting
def getPersonalizedGreeting(city, name):
    return f"Hey, {name}! What's famous about {city}?"   

@app.route("/personalized-greeting", methods=["GET"])
def pGreet():
    city = request.args.get("city", "")
    name = request.args.get("name", "")
    return getPersonalizedGreeting(city, name)

# Finding Age
def findAge(birthyear):
    return str(2025 - birthyear)

@app.route("/find-age", methods=["GET"])
def find_age():
    birthyear = int(request.args.get("birthyear", 0))
    age = findAge(birthyear)
    return age

# Is time sufficient
def findRequiredTime(days, hours):
    return days * hours 

@app.route("/is-time-sufficient", methods=["GET"])
def isTime():
    days = int(request.args.get("days", 0))
    hours = int(request.args.get("hours", 0))
    total_hours = findRequiredTime(days, hours)
    if total_hours >= 30:
       return "The time being dedicated is sufficient for learning functions."
    else:
       return "The time being dedicated is not sufficient for learning functions."  

if __name__ == "__main__":
   app.run() 
