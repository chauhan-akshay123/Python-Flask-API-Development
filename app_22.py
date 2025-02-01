from flask import Flask, request, jsonify

app = Flask(__name__)

# Welcome route
@app.route("/", methods=["GET"])
def get_welcome():
    return "Welcome to the Flask API"

heights = [160, 175, 180, 165, 170]

# Sort heights in ascending order
@app.route("/heights/sort-ascending", methods=["GET"])
def heights_sort_ascending():
    heights_copy = heights.copy()
    heights_copy.sort()
    return jsonify(heights_copy)

# Sort heights in descending order
@app.route("/heights/sort-descending", methods=["GET"])
def heights_sort_descending():
    heights_copy = heights.copy()
    heights_copy.sort(reverse=True)
    return jsonify(heights_copy)

employees = [
  { "name": 'Rahul', "employeeId": 101, "salary": 50000 },
  { "name": 'Sita', "employeeId": 102, "salary": 60000 },
  { "name": 'Amit', "employeeId": 103, "salary": 45000 }
]

# Sort employees by salary in descending order
def sortEmployeesBySalary(employee):
    return employee['salary']

@app.route("/employees/sort-by-salary-descending", methods=["GET"])
def employees_by_salary_descending():
    employees_copy = employees.copy()
    employees_copy.sort(key=sortEmployeesBySalary, reverse=True)
    return jsonify(employees_copy)

# Sort employees by salary in ascending order
@app.route("/employees/sort-by-salary-ascending", methods=["GET"])
def employees_by_salary_ascening():
    employees_copy = employees.copy()
    employees_copy.sort(key=sortEmployeesBySalary)
    return jsonify(employees_copy)

books = [
  { "title": 'The God of Small Things', "author": 'Arundhati Roy', "pages": 340 },
  { "title": 'The White Tiger', "author": 'Aravind Adiga', "pages": 321 },
  { "title": 'The Palace of Illusions', "author": 'Chitra Banerjee', "pages": 360 }
]

# Sort books by pages in Ascending order
def sortBooksByPages(book):
    return book['pages']

@app.route("/books/sort-by-pages-ascending", methods=["GET"])
def books_by_pages():
    books_copy = books.copy()
    books_copy.sort(key=sortBooksByPages)
    return jsonify(books_copy)

# Sort books by pages in descending order
@app.route("/books/sort-by-pages-descending", methods=["GET"])
def books_by_pages_descending():
    books_copy = books.copy()
    books_copy.sort(key=sortBooksByPages, reverse=True)
    return jsonify(books_copy)

if __name__ == "__main__":
   app.run() 
