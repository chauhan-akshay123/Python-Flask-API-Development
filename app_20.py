from flask import Flask, request, jsonify

app = Flask(__name__)

# Array of products
products = [
  { "name": 'Product A', "inStock": True },
  { "name": 'Product B', "inStock": False },
  { "name": 'Product C', "inStock": True },
  { "name": 'Product D', "inStock": False }
]

# Array of users
users = [
  { "name": 'Alice', "age": 25 },
  { "name": 'Bob', "age": 30 },
  { "name": 'Charlie', "age": 17 },
  { "name": 'Dave', "age": 16 }
]

# Array of products with prices
productPrices = [
  { "name": 'Product A', "price": 50 },
  { "name": 'Product B', "price": 150 },
  { "name": 'Product C', "price": 200 },
  { "name": 'Product D', "price": 90 }
]

# Array of articles with word counts
articles = [
  { "title": 'Article A', "wordCount": 400 },
  { "title": 'Article B', "wordCount": 600 },
  { "title": 'Article C', "wordCount": 700 },
  { "title": 'Article D', "wordCount": 300 }
]

# Array of movies with ratings
movies = [
  { "title": 'Movie A', "rating": 8.5 },
  { "title": 'Movie B', "rating": 7.0 },
  { "title": 'Movie C', "rating": 9.0 },
  { "title": 'Movie D', "rating": 6.5 }
]

# Array of employees with experience in years
employees = [
  { "name": 'Employee A', "experience": 3 },
  { "name": 'Employee B', "experience": 6 },
  { "name": 'Employee C', "experience": 10 },
  { "name": 'Employee D', "experience": 2 }
]

# Filter In-stock products
def filterInStockProducts(product):
    return product['inStock'] == True

@app.route("/in-stock-products", methods=["GET"])
def get_in_stock_products():
    result = [product for product in products if filterInStockProducts(product)]
    return jsonify(result)

# Filter Adults from User list
def filterAdults(user):
    return user['age'] >= 18

@app.route("/adult-users", methods=["GET"])
def get_adult_users():
    result = [user for user in users if filterAdults(user)]
    return jsonify(result)
       
# Filter expensive products
def filterExpensiveProducts(product, price):
    return product['price'] > price

@app.route("/expensive-products", methods=["GET"])
def get_expensive_products():
    price = int(request.args.get("price", 0))
    result = [product for product in productPrices if filterExpensiveProducts(product, price)]
    return jsonify(result)

# Filter Articles by word count
def filterLongArticles(article, minWords):
    return article['wordCount'] > minWords

@app.route("/long-articles", methods=["GET"])
def get_long_articles():
    minWords = int(request.args.get("minWords", 0))
    result = [article for article in articles if filterLongArticles(article, minWords)]
    return jsonify(result)

# Filter movies by rating
def filterHighRatedMovies(movie, minRating):
    return movie['rating'] > minRating

@app.route("/high-rated-movies", methods=["GET"])
def get_high_rated_movies():
    rating = float(request.args.get("rating", 0))
    result = [movie for movie in movies if filterHighRatedMovies(movie, rating)]
    return jsonify(result)

# Filter Employees by Experience
def filterExperienceEmployees(employee, minYears):
    return employee['experience'] > minYears

@app.route("/experienced-employees", methods=["GET"])
def get_experienced_employees():
    years = int(request.args.get("years", 0))
    result = [employee for employee in employees if filterExperienceEmployees(employee, years)]
    return jsonify(result)

if __name__ == "__main__":
   app.run()
