from flask import Flask, request, jsonify

app = Flask(__name__)

# welcome route
@app.route("/", methods=["GET"])
def api_welcome():
  return jsonify({"message": "Welcome to the Flask API."})

@app.route("/whisper", methods=["GET"])
def whisper():
   name = request.args.get("name", "")
   lowercase_name = name.lower()
   return lowercase_name

@app.route("/productname", methods=["GET"])
def fullproductName():
   companyName = request.args.get("companyName", "")
   productName = request.args.get("productName", "")
   return f"{companyName} {productName}"

@app.route("/date", methods=["GET"])
def properDate():
   month = request.args.get("month", "")
   year = request.args.get("year", "")
   formattedDate = f"{month}/{year}"
   return formattedDate

@app.route("/greet", methods=["GET"])
def greet():
   city = request.args.get("city", "")
   greeting = f"You live in {city}"
   return greeting

@app.route("/capital", methods=["GET"])
def capital():
   capital = request.args.get("capital", "")
   country  = request.args.get("country", "")
   countryCapital = f"{capital} is the capital of {country}"
   return countryCapital 

@app.route("/email", methods=["GET"])
def email():
   firstName = request.args.get("firstName", "")
   lastName = request.args.get("lastName", "")
   domain = request.args.get("domain", "")
   fullEmail = f"{firstName}.{lastName}@{domain}.com"
   return fullEmail

if __name__ == "__main__":
   app.run() 
