from flask import Flask, request, jsonify

app = Flask(__name__)

# Data
users = [
    {'id': 1, 'username': 'ankit', 'fullName': 'Ankit Kumar'},
    {'id': 2, 'username': 'dhananjit', 'fullName': 'Dhananjit Singh'},
]

credit_cards = [
    {'number': '1234567890123456', 'holder': 'John Doe', 'expiry': '12/24'},
    {'number': '9876543210987654', 'holder': 'Jane Smith', 'expiry': '01/25'},
]

users_details = [
    {'email': 'johndoe@example.com', 'name': 'John Doe', 'age': 30},
    {'email': 'janesmith@example.com', 'name': 'Jane Smith', 'age': 25},
]

books = [
    {'isbn': '9783161484100', 'title': 'Example Book', 'author': 'John Author'},
    {'isbn': '9781234567897', 'title': 'Another Book', 'author': 'Jane Writer'},
]

people = [
    {'ssn': '123-45-6789', 'name': 'John Doe', 'birthDate': '1990-01-01'},
    {'ssn': '987-65-4321', 'name': 'Jane Smith', 'birthDate': '1985-05-05'},
]

# Check username availability
@app.route("/username/find/<string:name>", methods=["GET"])
def get_name(name):
    for user in users:
        if user['username'] == name:
            return jsonify({'result': "Username is unavailable"})
    return jsonify({'result': "Username is available"})

# Find credit card number
@app.route("/credit-cards/find", methods=["GET"])
def get_credit_card():
    cardNumber = request.args.get("cardNumber")
    for ele in credit_cards:
        if ele['number'] == cardNumber:
           return jsonify(ele)
    return jsonify(None)     

# Find Email Address
@app.route("/emails/find", methods=["GET"])
def find_email():
    email = request.args.get("email", "")
    for ele in users_details:
        if ele['email'] == email:
           return jsonify(ele)
    return jsonify(None)    

# Find ISBN Number
@app.route("/books/find", methods=["GET"])
def find_book():
    isbn = request.args.get("isbn", "")
    for book in books:
        if book['isbn'] == isbn:
           return jsonify(book)
    return jsonify(None)         

# Find social security number
@app.route("/ssn/find", methods=["GET"])
def find_ssn():
    ssn = request.args.get("ssn", "")
    for person in people:
        if person['ssn'] == ssn:
           return jsonify(person)
    return jsonify(None)     

if __name__ == "__main__":
   app.run() 
