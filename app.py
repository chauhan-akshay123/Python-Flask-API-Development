from flask import Flask, request, jsonify

app = Flask(__name__)

# welcome route
@app.route("/", methods=["GET"])
def api_welcome():
  return jsonify({"message": "Welcome to the Flask API."})

@app.route("/shout", methods=["GET"])
def shout():
  name = request.args.get("name", "")
  uppercase_name = name.upper()
  return uppercase_name

@app.route("/fullname", methods=["GET"])
def fullname():
  first_name = request.args.get("firstname", "")
  last_name = request.args.get("lastname", "")
  fullname = f"{first_name} {last_name}"
  return fullname
  
@app.route("/date", methods=["GET"])
def formatDate():
    month = request.args.get("month", "")
    year = request.args.get("year", "")
    formattedDate = f"{month} {year}"
    return formattedDate

@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "")
    greeting = f"Namaste, {name}"
    return greeting

@app.route("/address", methods=["GEt"])
def address():
    street = request.args.get("street", "")
    city = request.args.get("city", "")
    state = request.args.get("state", "")
    formattedAdress = f"{street}, {city}, {state}"
    return formattedAdress

if __name__ == "__main__":
  app.run()  
