from flask import Flask, request, jsonify

app = Flask(__name__)

# Filter temperatures
def filterHighTemperatures(temp):
    return temp > 25

@app.route("/high-temperatures", methods=["GET"])
def high_temperatures():
    temperatures = [22,26,19,30,23,28,17,31]
    result = []
    for temp in temperatures:
        if filterHighTemperatures(temp):
           result.append(temp)
    return jsonify(result)        

# Filter Low Prices
def filterLowPrices(price):
    return price <= 100

@app.route("/low-prices", methods=["GET"])
def low_prices():
    prices = [80, 120, 95, 150, 60, 110]
    result = []
    for price in prices:
        if filterLowPrices(price):
           result.append(price)
    return jsonify(result)        
    
# Filter high rating
def filterHighRatings(rating):
    return rating > 3.5

@app.route("/high-ratings", methods=["GET"])
def high_ratings():
    ratings = [4.2, 3.8, 2.5, 4.7, 3.0, 4.9, 3.6]
    result = []
    for rating in ratings:
        if filterHighRatings(rating):
           result.append(rating)
    return jsonify(result)        

# filter Long Names
def filterLongIndianName(name):
    return len(name) > 6

@app.route("/long-indian-names", methods=["GET"])
def long_indian_names():
    names = ['Akshay', 'Priyanka', 'Arjun', 'Anushka', 'Rajesh', 'Kavita']
    result = []
    for name in names:
        if filterLongIndianName(name):
           result.append(name)
    return jsonify(result)        

# filter Cheaper Products
def filterCheaperProducts(productPrice, limit):
    return productPrice < limit

@app.route("/cheaper-products", methods=["GET"])
def cheaper_products():
    prices = [10, 25, 50, 75, 100, 150, 200]
    filterParam = int(request.args.get("filterParam", 100))
    result = []
    for price in prices:
        if filterCheaperProducts(price, filterParam):
            result.append(price)
    return jsonify(result)        

if __name__ == "__main__":
   app.run() 
