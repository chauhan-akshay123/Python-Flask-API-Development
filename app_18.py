from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
   {"name": "Laptop", "price": 50000, "category": "Electronics"},
   {"name": "Mobile", "price": 20000, "category": "Electronics"},
   {"name": "Shirt", "price": 1500, "category": "Apparel"},
   {"name": "Mixer Grinder", "price": 4000, "category": "Home Appliances"},
]

cars = [
   {"make": "Maruti", "model": "Swift", "mileage": 15000},
   {"make": "Hyundai", "model": "i20", "mileage": 25000},
   {"make": "Tata", "model": "Nexon", "mileage": 30000},
]

movies = [
   {"title": "3 Idiots", "genre": "Comedy", "rating": 9},
   {"title": "Dangal", "genre": "Drama", "rating": 10},
   {"title": "Bahubali", "genre": "Action", "rating": 8}
]

orders = [
   {"orderId": 1, "customerName": "Rahul", "status": "shipped"},
   {"orderId": 2, "customerName": "Sita", "status": "pending"},
   {"orderId": 3, "customerName": "Amit", "status": "shipped"},
]

# Filtering Products by Category

def filter_by_category(product, category):
    return product['category'] == category

@app.route("/products/category/<string:category>", methods=["GET"])
def get_products_by_category(category):
    result = [product for product in products if filter_by_category(product, category)]
    return jsonify(result)

# Filter cars by mileage

def filter_cars_by_mileage(car, max_mileage):
    return car['mileage'] < max_mileage

@app.route("/cars/mileage/<int:max_mileage>", methods=["GET"])
def get_cars_by_mileage(max_mileage):
    result = [car for car in cars if filter_cars_by_mileage(car, max_mileage)]
    return jsonify(result)

# Filter movies by rating

def filter_by_rating(movie, min_rating):
    return movie['rating'] > min_rating

@app.route("/movies/rating/<int:min_rating>", methods=["GET"])
def get_movies_by_rating(min_rating):
    result = [movie for movie in movies if filter_by_rating(movie, min_rating)]
    return jsonify(result)

# Filter orders by status

def filter_by_status(order, status):
    return order['status'] == status

@app.route("/orders/status/<string:status>", methods=["GET"])
def get_orders_by_status(status):
    result = [order for order in orders if filter_by_status(order, status)]
    return jsonify(result)

if __name__ == "__main__":
   app.run() 
