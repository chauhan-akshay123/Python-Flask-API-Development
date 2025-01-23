from flask import Flask, request, jsonify

app = Flask(__name__)

# Welcome route
@app.route("/", methods=["GET"])
def api_welcome():
  return jsonify({ "message": "Welcome to the Flask API." })

@app.route("/custom-commit", methods=["GET"])
def customCommit():
  type = request.args.get("type", "")
  message = request.args.get("message", "")
  result = f"{type}: {message}"
  return result 

@app.route("/certificate", methods=["GET"])
def generateCertificate():
  firstName = request.args.get("firstName", "")
  lastNme = request.args.get("lastName", "")
  courseName = request.args.get("courseName", "")
  result = f"This certification is awarded to {firstName} {lastNme} for completing the course {courseName}"
  return result

@app.route("/autoreply", methods=["GET"])
def autoReply():
  startMonth = request.args.get("startMonth", "")
  endMonth = request.args.get("endMonth", "")
  result = f"Dear customer, thank you for reaching out to me. Unfortunately, I'm out of office from {startMonth} till {endMonth}. Your enquiry will be resolved by another collegue"
  return result

@app.route("/secureurl", methods=["GET"])
def helper():
  domain = request.args.get("domain", "")
  result = f"https://{domain}"
  return result

@app.route("/sendotp", methods=["GET"])
def sendOtp():
  otpCode = request.args.get("otpCode", "")
  result = f"Your OTP for account verification is {otpCode}. Do not share this with anyone"
  return result
 
@app.route("/welcome", methods=["GET"])
def welcome():
  firstName = request.args.get("firstName", "")
  email = request.args.get("email", "") 
  result = f"Hey {firstName}. We're excited to have you here, we'll send future notifications to your registered mail ({firstName}@gmail.com)"
  return result

@app.route("/github-profile", methods=["GET"])
def generateProfile():
  userName = request.args.get("userName", "")
  result = f"https://github.com/{userName}"
  return result

@app.route("/text-to-csv", methods=["GET"])
def helper_function():
  id = request.args.get("id", "")
  email = request.args.get("email", "")
  rollNumber = request.args.get("rollNumber", "")
  result = f"{id}, {email}, {rollNumber}"
  return result 

if __name__ == "__main__":
 app.run()
