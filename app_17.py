from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data 
numbers = [-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter Prime numbers
def is_prime(num):
    if num <= 1:
       return False
    if num <= 3:
       return True
    if num % 2 == 0 or num % 3 == 0:
       return False 
    i = 5
    while i*i <= num:
     if num % i == 0 or num % (i + 2) == 0:
       return False
     i += 6
    return True 

def filter_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
           prime_numbers.append(num)
    return prime_numbers

@app.route("/prime-numbers", methods=["GET"])
def get_prime():
    prime_numbers = filter_prime_numbers(numbers)
    return jsonify(prime_numbers)    

# Filter Positive Numbers
def filterPositiveNumbers(num):
    return num > 0

@app.route("/positive-numbers", methods=["GET"])
def get_positive_numbers():
    result = []
    for num in numbers:
        if filterPositiveNumbers(num):
           result.append(num)
    return result

# Filter Negative Numbers
def filterNegativeNumbers(num):
    return num < 0

@app.route("/negative-numbers", methods=["GET"])
def get_negative_numbers():
    result = []
    for num in numbers:
        if filterNegativeNumbers(num):
           result.append(num)
    return result      

# Filter Odd Numbers
def filterOddNumbers(num):
    return num % 2 != 0

@app.route("/odd-numbers", methods=["GET"])
def get_odd_numbers():
    result = []
    for num in numbers:
        if filterOddNumbers(num):
           result.append(num)
    return result       

# Filter numbers greater than a given value
def filterNumberGreaterThan(num, value):
    return num > value

@app.route("/numbers-greater-than", methods=["GET"])
def get_numbers_greater_than():
    value = int(request.args.get("value", 0))
    result = []
    for num in numbers:
        if filterNumberGreaterThan(num, value):
           result.append(num)
    return result      

# Filter numbers less than a give value
def filterNumbersLessThan(num, value):
    return num < value

@app.route("/numbers-less-than", methods=["GET"])
def get_numbers_less_than():
    value = int(request.args.get("value", 0))
    result = []
    for num in numbers:
        if filterNumbersLessThan(num, value):
           result.append(num)
    return result               

if __name__ == "__main__":
   app.run()
