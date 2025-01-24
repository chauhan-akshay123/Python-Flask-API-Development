from flask import Flask, request, jsonify

app = Flask(__name__)

# welcome route
@app.route("/", methods=["GET"])
def api_welcome():
 return jsonify({ "message": "Welcome to the flask API" })

# BMI Calculator
@app.route("/bmi", methods=["GET"])
def bmi():
 weight = float(request.args.get("weight"))
 height = float(request.args.get("height"))
 bmi = weight / (height * height)
 bmi = round(bmi, 2) 
 return f"Your BMI is: {bmi}" 

# Grocery Checkout Price
@app.route("/checkout", methods=["GET"])
def checkout():
 product = request.args.get("product", "")
 units = float(request.args.get("units", 0))
 price = float(request.args.get("price", 0))
 totalPrice = units * price
 return f"Your total for {product} is {totalPrice}"

# Grade Percentage
@app.route("/grade", methods=["GET"])
def grade():
 maths = int(request.args.get("maths", 0))
 science = int(request.args.get("science", 0))
 english = int(request.args.get("english", 0))
 
 if maths < 0 or maths > 100 or science < 0 or science > 100 or english < 0 or english > 100:
  return "Scores must be between 0 and 100.", 400

 grade_percentage = round(((maths + science + english) / 300) * 100, 2)
 return f"Your grade in percentage is {grade_percentage}%"

# Return bill after applying discount
@app.route("/discounted-price", methods=["GET"])
def discountedPrice():
 cartTotal = float(request.args.get("cartTotal", 0))
 discount = float(request.args.get("discount", 0))

 discounted_amount = cartTotal * (discount / 100)
 final_price = cartTotal - discounted_amount

 return f"Result: Your bill amount is {final_price:.2f}"

# Split bill among friends
@app.route("/split-bill", methods=["GET"])
def biil():
 billAmount = float(request.args.get("billAmount", 0))
 numberOfFriends = int(request.args.get("numberOfFriends", 0))
 splitAmount = billAmount / numberOfFriends
 return f"Result: Each friend owes Rs. {splitAmount} againts the bill"

# Covert Celsius to Fahrenheit
@app.route("/celsius-to-fahrenheit", methods=["GET"])
def conversion():
 temperature = int(request.args.get("temperature", 0))
 fahrenheitTemp = (temperature * (9/5) + 32)
 return f"Result: {fahrenheitTemp} Fahrenheit"

# Calculate monthly Salary
@app.route("/monthly-salary", methods=["GET"])
def calculate_monthly_salary():
 hourly_wage = float(request.args.get("hourlyWage"))
 total_hours = float(request.args.get("totalHours"))
 if hourly_wage <= 0 or total_hours <= 0:
  return jsonify({"error": "Hourly wage and total hours must be positive values."}), 400

 monthly_salary = hourly_wage * total_hours
 return f"Result: Your monthly salary is ₹.{monthly_salary}"

if __name__ == "__main__":
 app.run()
