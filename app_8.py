from flask import Flask, request, jsonify

app = Flask(__name__)

# welcome route
@app.route("/", methods=["GET"])
def api_welcome():
    return jsonify({ "message": "welcome to the Flask API." })

# Check whole number
@app.route("/check-whole-number", methods=["GET"])
def check_whole_number():
  number = int(request.args.get("number", 0))
  if number >= 0:
     result = "whole"
  else:
     result = "not whole"
  return f"Number is {result} number"

# Check Equal
@app.route("/check-equal", methods=["GET"])
def check_equal():
  num1 = int(request.args.get("num1", 0))
  num2 = int(request.args.get("num2", 0))
  if num1 == num2:
     result = "equal"
  else: 
     result = "not equal"   
  return f"Numbers are {result}"     

# Check Active
@app.route("/check-active", methods=["GET"])
def check_active():
   isActive = request.args.get("isActive", "false") == "true"
   if isActive:
      result = "User is Active"
   else:
      result = "User is not active"
   return result     

# Check Discount
@app.route("/check-discount", methods=["GET"])
def check_discount():
   cost = float(request.args.get("cost", 0))
   if cost > 1000:
      result = "User is eligible for a discount."
   else: 
      result = "User is not eligible for a discount."   
   return result   

# Check Experience
@app.route("/check-experience", methods=["GET"])
def check_exp():
   years = int(request.args.get("years", 0))
   if years > 0:
      result = "experienced"
   else: 
      result = "fresher"
   return f"User is {result}"      

# Check Result
@app.route("/check-result", methods=["GET"])
def check_result():
   result = int(request.args.get("result", 0))
   if result > 80:
      grade = "A"
   elif result > 50 and result < 80:
      grade = "B"
   else:
      grade = "Fail"
   return f"The grade is {grade}"    

# Check Attendance
@app.route("/check-attendance", methods=["GET"])
def check_attendance():
   attendance = int(request.args.get("attendance", 0))
   if attendance < 50:
      result = "low"
   elif attendance < 90:
      result = "moderate"
   else:
      result = "high"       
   return f"Attendance is {result}"  

# Check rating
@app.route("/check-rating", methods=["GET"])
def check_rating():
   stars = int(request.args.get("stars", 0))
   if stars < 3:
      result = "low"
   elif stars <= 4:
      result = "moderate"
   else:
      result = "high" 
   return f"Restaurant rating is {result}"

if __name__ == "__main__":
    app.run()
