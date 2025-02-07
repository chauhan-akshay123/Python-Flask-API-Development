from flask import Flask, request, jsonify

app = Flask(__name__)

# Data
numbers = [1,2,3,4,5,6,7,8,9,10]
names = ["Rahul", "Sita", "Amit", "Vikram", "Priya"]
employees = [
   {"employeeId": 1, "name": "Rahul"},
   {"employeeId": 2, "name": "Sita" },
   {"employeeId": 3, "name": "Amit"}
]
contacts = [
   {"phoneNumber": "1234567890", "name": "Rahul", "address": "123 Street, City"},
   {"phoneNumber": "0987654321", "name": "Sita", "address": "456 Avenue, City"},
   {"phoneNumber": "1112223334", "name": "Amit", "address": "789 Boulevard, City"}
]

# Finding a number in Numbers
@app.route("/numbers/find/<int:number>", methods=["GET"])
def get_number(number):
    for ele in numbers:
        if ele == number:
           return jsonify(ele) 
    return jsonify(None)

# Finding a name in names
@app.route("/names/find/<string:name>", methods=["GET"])
def get_name(name):
    for ele in names:
        if ele == name:
           return jsonify(name)
    return jsonify(None)

# Finding an employee in employees
@app.route("/employees/find/<int:id>", methods=["GET"])
def get_employee_id(id):
    for ele in employees:
        if ele['employeeId'] == id:
           return jsonify(ele)
    return jsonify(None)     

# Finding a conatct in cotacts
@app.route("/contacts/find/<int:phoneNumber>", methods=["GET"])
def get_conatact_by_phoneNumber(phoneNumber):
    for contact in contacts:
        if contact.get('phoneNumber') == phoneNumber:
           return jsonify(contact)
    return jsonify(None)     

if __name__ == "__main__":
   app.run() 
