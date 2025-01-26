from flask import Flask, request, jsonify

app = Flask(__name__)

# Generate Github Profile
def generateProfileUrl(userName):
    return f"https://github.com/{userName}"

@app.route("/github-profile", methods=["GET"])
def profile():
    userName = request.args.get("userName", "")
    return generateProfileUrl(userName)

# Generate Certificate
def generateCertificate(firstName, lastName, courseName):
    return f"This certification is awarded to {firstName} {lastName} for completing the course {courseName}"

@app.route("/certificate", methods=["GET"])
def certificate():
    firstName = request.args.get("firstName", "")
    lastName = request.args.get("lastName", "")
    courseName = request.args.get("courseName", "")
    return generateCertificate(firstName, lastName, courseName)

# Calculate Grade
def calculateGrade(maths, science, english):
    percentage = round(((maths + science + english)/300) *100, 1)
    return str(percentage)

@app.route("/grade", methods=["GET"])
def grade():
    maths = int(request.args.get("maths", 0))
    science = int(request.args.get("science", 0))
    english = int(request.args.get("english", 0))
    grade = calculateGrade(maths, science, english)
    return f"Your grade in percentage is %{grade}"

# Split bill with friend
def spliBill(billAmount, numberOfFriends):
    splitAmount = billAmount / numberOfFriends
    return str(splitAmount)

@app.route("/split-bill", methods=["GET"])
def spli():
    billAmount = int(request.args.get("billAmount", ""))
    numberOfFriends = int(request.args.get("numberOfFriends", 0))
    result = spliBill(billAmount, numberOfFriends)
    return f"Result: Each friend owes Rs. {result} against the bill"

# Calculate monthly salary
def calculateSalary(hourlyWage, totalHours):
    monthlySalary = hourlyWage * totalHours
    return str(monthlySalary)

@app.route("/monthly-salary", methods=["GET"])
def salary():
    hourlyWage = int(request.args.get("hourlyWage", 0))
    totalHours = int(request.args.get("totalHours", 0))
    result = calculateSalary(hourlyWage, totalHours)
    return f"Result: Your monthly salary is ₹{result}"

if __name__ == "__main__":
   app.run() 
