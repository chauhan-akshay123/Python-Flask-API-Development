from flask import Flask, request, jsonify

app = Flask(__name__)

# Welcome route
@app.route("/", methods=["GET"])
def get_welcome():
    return "Welcome to the Flask API."

ages = [25, 30, 18, 22, 27]
students = [
    {'name': 'Rahul', 'rollNo': 101, 'marks': 85},
    {'name': 'Sita', 'rollNo': 102, 'marks': 95},
    {'name': 'Amit', 'rollNo': 103, 'marks': 70},
]
cars = [
    {'make': 'Maruti', 'model': 'Swift', 'mileage': 15},
    {'make': 'Hyundai', 'model': 'i20', 'mileage': 18},
    {'make': 'Tata', 'model': 'Nexon', 'mileage': 20},
]

# Sort ages in ascending order
@app.route("/ages/sort-ascending", methods=["GET"])
def sort_ages_ascending():
    ages_copy = ages.copy()
    ages_copy.sort()
    return jsonify(ages_copy)

# Sort ages in descending order
@app.route("/ages/sort-descending", methods=["GET"])
def sort_ages_descending():
    ages_copy = ages.copy()
    ages_copy.sort(reverse=True)
    return jsonify(ages_copy)

# Sort students by marks descending

def get_marks(student):
    return student['marks']

@app.route("/students/sort-by-marks-descending", methods=["GET"])
def sort_students_by_marks_descending():
    students_copy = students.copy()
    students_copy.sort(key=get_marks, reverse=True)
    return jsonify(students_copy)

# Sort students by marks ascending

@app.route("/students/sort-by-marks-ascending", methods=["GET"])
def sort_students_by_marks_ascending():
    students_copy = students.copy()
    students_copy.sort(key=get_marks)
    return jsonify(students_copy)

# Sort cars by mileage descending

def get_mileage(car):
    return car['mileage']

@app.route("/cars/sort-by-mileage-descending", methods=["GET"])
def sort_cars_by_mileage_descending():
    cars_copy = cars.copy()
    cars_copy.sort(key=get_mileage, reverse=True)
    return jsonify(cars_copy)

# Sort cars by mileage in ascending order

@app.route("/cars/sort-by-mileage-ascending", methods=["GET"])
def sort_cars_by_mileage_ascending():
    cars_copy = cars.copy()
    cars_copy.sort(key=get_mileage)
    return jsonify(cars_copy)

if __name__ == "__main__":
   app.run() 
