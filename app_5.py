from flask import Flask, request, jsonify

app = Flask(__name__)

# welcome route
@app.route("/", methods=["GET"])
def api_welcome():
   return jsonify({ "message": "Welcome to the Flask API" })

# total marks
@app.route("/total-marks", methods=["GET"])
def total_marks():
   marks1 = float(request.args.get("marks1", 0))
   marks2 = float(request.args.get("marks2", 0))
   totalMarks = marks1 + marks2
   return str(totalMarks)

# total weight
@app.route("/total-weight", methods=["GET"])
def total_weight():
   weight1 = float(request.args.get("weight1", 0))
   weight2 = float(request.args.get("weight2", 0))
   weight3 = float(request.args.get("weight3", 0))
   totalWeight = weight1 + weight2 + weight3
   return str(totalWeight)

# monthly salary
@app.route("/monthly-salary", methods=["GET"])
def monthly_salary():
   annualSalary = float(request.args.get("annualSalary", 0))
   monthlySalary = annualSalary / 12
   return str(monthlySalary)

# total pages
@app.route("/total-pages", methods=["GET"])
def total_pages():
   pagesPerDay = float(request.args.get("pagesPerDay", 0))
   days = float(request.args.get("days", 0))
   totalPages = pagesPerDay * days
   return str(totalPages)

# currency conversion
@app.route("/currency-conversion", methods=["GET"])
def currency_conversion():
   amount = float(request.args.get("amount", 0))
   exchangeRate = float(request.args.get("exchangeRate", 0))
   convertedAmount = amount * exchangeRate
   return str(convertedAmount)

# average sales
@app.route("/average-sales", methods=["GET"])
def average_sales():
   sales1 = float(request.args.get("sales1", 0))
   sales2 = float(request.args.get("sales2", 0))
   sales3 = float(request.args.get("sales3", 0))
   avgSales = (sales1 + sales2 + sales3) / 3
   return str(avgSales)

if __name__ == "__main__":
   app.run() 
