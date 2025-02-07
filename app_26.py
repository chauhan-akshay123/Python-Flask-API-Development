from flask import Flask, request, jsonify

app = Flask(__name__)

# Data 
phones = [
    {'number': '123-456-7890', 'owner': 'Alice', 'type': 'mobile'},
    {'number': '987-654-3210', 'owner': 'Bob', 'type': 'home'}
]

accounts = [
    {'number': '111122223333', 'holder': 'Charlie', 'balance': 5000},
    {'number': '444455556666', 'holder': 'Dave', 'balance': 3000}
]

licenses = [
    {'number': 'D1234567', 'name': 'Eve', 'expiryDate': '2026-04-01'},
    {'number': 'D7654321', 'name': 'Frank', 'expiryDate': '2024-11-15'}
]

employees = [
    {'id': 'E1234', 'name': 'Grace', 'department': 'Engineering'},
    {'id': 'E5678', 'name': 'Hank', 'department': 'Marketing'}
]

orders = [
    {'id': 'ORD12345', 'customerName': 'Ivy', 'totalAmount': 150},
    {'id': 'ORD67890', 'customerName': 'Jake', 'totalAmount': 200}
]

# Find Mobile Phone Number
@app.route("/phones/find", methods=["GET"])
def find_phone():
    phoneNumber = request.args.get("phoneNumber", "")
    for phone in phones:
        if phone['number'] == phoneNumber:
           return jsonify(phone)
    return jsonify(None)     

# Find Bank Account Number
@app.route("/accounts/find", methods=["GET"])
def find_account():
    accountNumber = request.args.get("accountNumber", "")
    for account in accounts:
        if account['number'] == accountNumber:
           return jsonify(account)
    return jsonify(None)  

# Find Driver's License Number
@app.route("/licenses/find", methods=["GET"])
def find_license():
    licenseNumber = request.args.get("licenseNumber", "")
    for license in licenses:
        if license['number'] == licenseNumber:
           return jsonify(license)
    return jsonify(None)

# Find Employee ID
@app.route("/employees/find", methods=["GET"])
def find_employee():
    employeeId = request.args.get("employeeId", "")
    for employee in employees:
        if employee['id'] == employeeId:
           return jsonify(employee)
    return jsonify(None)     

# Find Order ID
@app.route("/orders/find", methods=["GET"]) 
def find_order():
    orderId = request.args.get("orderId", "")
    for order in orders:
        if order['id'] == orderId:
           return jsonify(order)
    return jsonify(None)            

if __name__ == "__main__":
   app.run() 
