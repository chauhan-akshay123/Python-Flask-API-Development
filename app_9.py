from flask import Flask, request, jsonify

app = Flask(__name__)

# Welcome Route
@app.route("/", methods=["GET"])
def api_welcome():
    return jsonify({ "message": "Welcome to the Flask API." })

# Check BMI category
@app.route("/check-bmi", methods=["GET"])
def check_bmi_category():
    weight = float(request.args.get("weight", 0))
    height = float(request.args.get("height", 0))
    bmi = weight / (height * height)

    if bmi < 18.5: 
       category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese" 
    return f"BMI category is {category}"    

# Check academic performance based on grades
@app.route("/check-performance", methods=["GET"])
def check_performance():
    grade = int(request.args.get("grade", 0))
    if grade >= 90:
       result = "excellent"
    elif grade >= 75:
       result = "good"
    elif grade >= 50:
       result = "average"
    else: 
       result = "poor"
    return f"Academic performance is {result}"  

# Determine age group category
@app.route("/check-age-group", methods=["GET"])
def check_age_group():
    age = int(request.args.get("age", 0))
    if age <= 12:
       result = "child"
    elif age <= 17:
       result = "teenager"
    elif age <= 64:
       result = "adult"
    else: 
       result = "senior"
    return f"Age group is {result}"                              

# Determine loan eligibilty based on credit score
@app.route("/check-loan-eligibility", methods=["GET"])
def check_eligibility():
   creditScore = int(request.args.get("creditScore", 0))
   if creditScore >= 750:
      result = "high"
   elif creditScore >= 650:
      result = "medium" 
   else:
      result = "low"
   return f"Loan eligibility is {result}"          

# Determine tax bracket based on income
@app.route("/check-tax-bracket", methods=["GET"])
def check_tax_bracket():
   income = int(request.args.get("income", ""))
   if income <= 500000:
      result = "10% tax bracket"
   elif income <= 1000000:
      result = "15% tax bracket"
   elif income <= 1500000:
      result = "20% tax bracket"
   else:
      result = "30% tax bracket"
   return f"You fall under the {result}"          

# Determine experience level based on years of work
@app.route("/check-experience", methods=["GET"])
def check_experience():
   yearsOfExperience = int(request.args.get("yearsOfExperience", 0))
   if yearsOfExperience > 5:
      result = "expert"
   else:
      result = "not expert"
   return f"Experience level is {result}"     

if __name__ == "__main__":
    app.run()
