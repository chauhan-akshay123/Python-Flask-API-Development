from flask import Flask, request, jsonify

app = Flask(__name__)

employees = [
  { "name": 'Rahul Gupta', "department": 'HR', "salary": 50000 },
  { "name": 'Sneha Sharma', "department": 'Finance', "salary": 60000 },
  { "name": 'Priya Singh', "department": 'Marketing', "salary": 55000 },
  { "name": 'Amit Kumar', "department": 'IT', "salary": 65000 }
] 

# Filter employees by department
def filterByDepartment(employee, department):
    return employee['department'] == department

@app.route("/employees/department/<string:department>", methods=["GET"])
def get_employees_by_departmet(department):
    result = [employee for employee in employees if filterByDepartment(employee, department)]
    return jsonify(result)

bikes = [
  { "make": 'Hero', "model": 'Splendor', "mileage": 80 },
  { "make": 'Bajaj', "model": 'Pulsar', "mileage": 60 },
  { "make": 'TVS', "model": 'Apache', "mileage": 70 }
]

# Filter bikes by mileage
def filterByMileage(bike, minMileage):
    return bike['mileage'] > minMileage

@app.route("/bikes/mileage/<int:minMileage>", methods=["GET"])
def filter_bikes_by_mileage(minMileage):
    result = [bike for bike in bikes if filterByMileage(bike, minMileage)]
    return jsonify(result) 

# Filter bikes by make

def filterByMake(bike, make):
    return bike['make'] == make

@app.route("/bikes/make/<string:make>", methods=["GET"])
def filter_bike_by_make(make):
    result = [bike for bike in bikes if filterByMake(bike, make)]
    return jsonify(result)

songs = [
  { "title": 'Tum Hi Ho', "genre": 'Romantic', "rating": 4 },
  { "title": 'Senorita', "genre": 'Pop', "rating": 5 },
  { "title": 'Dil Chahta Hai', "genre": 'Bollywood', "rating": 3 }
]

# Filter Songs by rating
def filterByRating(song, minRating):
    return song['rating'] > minRating

@app.route("/songs/rating/<int:minRating>", methods=["GET"])
def filter_songs_by_rating(minRating):
    result = [song for song in songs if filterByRating(song, minRating)]
    return jsonify(result)

# Filter Songs by genre
def filterByGenre(song,genre):
    return song['genre'] == genre

@app.route("/songs/genre/<string:genre>", methods=["GET"])
def filter_songs_by_genre(genre):
    result = [song for song in songs if filterByGenre(song, genre)]
    return jsonify(result) 

tasks = [
  { "taskId": 1, "taskName": 'Prepare Presentation', "status": 'pending' },
  { "taskId": 2, "taskName": 'Attend Meeting', "status": 'in-progress' },
  { "taskId": 3, "taskName": 'Submit Report', "status": 'completed' }
]

# Filter tasks by status
def filterByStatus(task, status):
    return task['status'] == status

@app.route("/tasks/status/<string:status>", methods=["GET"])
def filter_tasks_by_status(status):
    result = [task for task in tasks if filterByStatus(task, status)]
    return jsonify(result)

if __name__ == "__main__":
   app.run() 
