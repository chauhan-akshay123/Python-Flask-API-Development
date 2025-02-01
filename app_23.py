from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
   { "title": 'Moby Jonas', "author": 'Herman Melville', "publication_year": 2023 },
   { "title": '1984', "author": 'George Orwell', "publication_year": 1984 },
   { "title": 'A Tale of Two Cities', "author": 'Charles Jonas', "publication_year": 2000 },
]

# Array of employees
employees = [
  { "name": 'John', "salary": 75000 },
  { "name": 'Doe', "salary": 30000 },
  { "name": 'Jane',"salary": 50000 }
]

# Array of products
products = [
  { "name": 'Product A', "price": 15 },
  { "name": 'Product B', "price": 25 },
  { "name": 'Product C', "price": 10 }
]

# Array of events
events = [
  { "name": 'Event A', "date": '2023-05-01' },
  { "name": 'Event B', "date": '2023-01-01' },
  { "name": 'Event C', "date": '2023-12-01' }
]

# Array of movies
movies = [
  { "title": 'Movie A', "rating": 9.0 },
  { "title": 'Movie C', "rating": 7.0 },
  { "title": 'Movie B', "rating": 8.5 }
]

# Array of customers
customers = [
  { "name": 'Customer A', "lastPurchase": '2023-06-15' },
  { "name": 'Customer B', "lastPurchase": '2023-11-01' },
  { "name": 'Customer C', "lastPurchase": '2023-03-10' }
]

# Sort books by year in ascending order
def sortBooksByYear(book):
    return book['publication_year']

@app.route("/books/sort-by-year", methods=["GET"])
def books_sort_by_year():
    books_copy = books.copy()
    books_copy.sort(key=sortBooksByYear)
    return jsonify(books_copy) 

# Sort employees by salary in descending order
def sortEmployeesBySalary(employee):
    return employee['salary']

@app.route("/employees/sort-by-salary", methods=["GET"])
def employees_sort_by_salary():
    employees_copy = employees.copy()
    employees_copy.sort(key=sortEmployeesBySalary, reverse=True)
    return jsonify(employees_copy)

# Sort products by price in Ascending order
def sortProductsByPrice(product):
    return product['price']

@app.route("/products/sort-by-price", methods=["GET"])
def products_sort_by_price():
    products_copy = products.copy()
    products_copy.sort(key=sortProductsByPrice)
    return jsonify(products_copy)

# Sort events by Date in ascending order
def sortEventsByDate(event):
    return event['date']

@app.route("/events/sort-by-date", methods=["GET"])
def events_sort_by_date():
    events_copy = events.copy()
    events_copy.sort(key=sortEventsByDate)
    return jsonify(events_copy)

# Sort movies by rating in descending order
def sortMoviesByRating(movie):
    return movie['rating']

@app.route("/movies/sort-by-rating", methods=["GET"])
def movies_sort_by_rating():
    movies_copy = movies.copy()
    movies_copy.sort(key=sortMoviesByRating, reverse=True)
    return jsonify(movies_copy)

# Sort customers by last purchase date in descending order
def sortCustomerByLastPurchase(customer):
    return customer['lastPurchase']

@app.route("/customers/sort-by-last-purchase", methods=["GET"])
def customers_sort_by_last_purchase():
    customers_copy = customers.copy()
    customers_copy.sort(key=sortCustomerByLastPurchase, reverse=True)
    return jsonify(customers_copy)

if __name__ == "__main__":
   app.run() 
