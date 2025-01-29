from flask import Flask, request, jsonify

app = Flask(__name__)

# Filtering Even numbers

def is_even(number):
   return number % 2 == 0

@app.route("/even-numbers", methods=["GET"])
def even_numbers():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    result = []
    for num in numbers:
       if is_even(num):
          result.append(num) 
    return jsonify(result)      

# Filtering Age

def is_adult(age):
    return age > 18

@app.route("/adult-ages", methods=["GET"])
def adult_ages():
    ages = [10, 20, 30, 40, 50]
    result = []
    for age in ages:
       if is_adult(age):
          result.append(age)
    return jsonify(result)  

# filter file size

def is_smaller_than_file_size(size, limit):
    return size < limit

@app.route("/small-files", methods=["GET"])
def small_files():
   file_sizes = [25, 50, 75, 120, 90, 150]
   filter_param = int(request.args.get("filter_param", 50))
   result = []
   for size in file_sizes:
       if is_smaller_than_file_size(size, filter_param):
          result.append(size)
   return jsonify(result)            

if __name__ == "__main__":
   app.run() 
