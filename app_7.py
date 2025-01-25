from flask import Flask, request, jsonify

app = Flask(__name__)

# welcome route
@app.route("/", methods=["GET"])
def api_welcome():
  return jsonify({ "message": "Welcome to the Flask API." })

# Chek Number
@app.route("/check-number", methods=["GET"])
def check_number():
    number = float(request.args.get("number", 0))
    if number >= 0:
       result = "positive"
    else:
       result = "negative"
    return f"Number is {result}"       

# check login
@app.route("/check-login", methods=["GET"])
def check_login():
    is_logged_in = request.args.get("isLoggedIn", "false") == "true"
    if is_logged_in: 
       result = "user is logged in"
    else: 
       result = "user is not logged in"
    return result    

# Check Temperature
@app.route("/check-temperature", methods=["GET"])
def check_temperature():
   temperature = float(request.args.get("temperature", 0))
   if temperature < 15:
      result = "cold"
   elif temperature <= 25:
      result = "warm"
   else: 
      result = "hot"
   return f"Temperature is {result}"     

# Check engagement
@app.route("/check-engagement", methods=["GET"])
def check_engagement():
   likes = int(request.args.get("likes", 0))
   if likes < 100:
      result = "low"
   elif likes <= 500:
      result = "medium"
   else:
      result = "high"    
   return f"Engagement level is {result}"           

if __name__ == "__main__":
  app.run()  
