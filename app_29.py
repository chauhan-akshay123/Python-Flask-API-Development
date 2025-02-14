from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
   {"id": 1, "name": "Laptop", "price": 1000, "in_stock": True},
   {"id": 2, "name": "Mouse", "price": 25, "in_stock": False},
   {"id": 3, "name": "Monitor", "price": 200, "in_stock": True},
   {"id": 4, "name": "Keyboard", "price": 50, "in_stock": True},
]

users = [
   {"id": 1, "name": "Alice", "email": "alice@example.com", "role": "admin"},
   {"id": 2, "name": "Bob", "email": "bob@company.com", "role": "user"},
   {"id": 3, "name": "Charlie", "email": "charlie@example.com", "role": "admin"},
   {"id": 4, "name": "David", "email": "david@company.com", "role": "moderator"}
]

posts = [
   {"id": 1, "author": "Alice", "content": "Learning Flask is fun!"},
   {"id": 2, "author": "Bob", "content": "Python is a great programming language."},
   {"id": 3, "author": "Alice", "content": "Flask and Django are web frameworks."},
   {"id": 4, "author": "Charlie", "content": "Machine learning is the future."}
]

# Filter products
@app.route("/products/filter", methods=["GET"])
def filter_products():
    min_price = float(request.args.get("min_price", 0))
    max_price = float(request.args.get("max_price", float("inf")))

    filteredProducts = []
    for product in products:
        if min_price <= product['price'] <= max_price and product['in_stock']:
           filteredProducts.append(product)
    return jsonify(filteredProducts)        


# Filter users
@app.route("/users/find", methods=["GET"])
def find_users():
   role = request.args.get("role")
   email_domain = request.args.get("email_domain")

   matched_users = []
   for user in users:
      if user['role'] == role or user['email'].endswith(f"@{email_domain}"):
         matched_users.append(user)
   return jsonify(matched_users)     

# Filter Posts
@app.route("/posts/search", methods=["GET"])
def posts_search():
    author = request.args.get("author")
    keyword = request.args.get("keyword")

    matched_posts = []
    for post in posts:
       if post["author"] == author or keyword.lower() in post['content'].lower():
          matched_posts.append(post)
    return jsonify(matched_posts)      

if __name__ == "__main__":
   app.run() 
