from flask import Flask, request, jsonify

app = Flask(__name__)

# Book data
book = {
    'title': 'The God of Small Things',
    'author': 'Arundhati Roy',
    'publicationYear': 1997,
    'genre': 'Novel',
    'isAvailable': True,
    'stock': 5,
}

# Get Book Details
@app.route("/book", methods=["GET"])
def getBook():
   return jsonify(book)

# Get full title and Author
def getFullTitleAuthor(book):
    return {
        "title": book['title'],
        "author": book['author']
    }

@app.route("/book/fulltitle-author", methods=["GET"])
def get_full_title():
    bookObj = getFullTitleAuthor(book)
    result = f"fullTitleAndAuthor: {bookObj['title']} by {bookObj['author']}"
    return jsonify({'fullTitleAndAuthor': result})
   
# Access genre and availability
def getGenreAndAvailability(book):
    return {
        "genre": book['genre'],
        "isAvailable": book['isAvailable']
    }

@app.route("/book/genre-availability")
def get_genre_and_availability():
    info = getGenreAndAvailability(book)
    return jsonify(info)

# Calculate Book age
def calculateBookAge(book):
    return {
        'age': 2025 - book['publicationYear']
    }

@app.route("/book/age", methods=["GET"])
def book_age():
    info = calculateBookAge(book)
    return jsonify(info)

# Book Summary
def getBookSummary(book):
    return {
        'title': book['title'],
        'author': book['author'],
        'genre': book['genre'],
        'publicationYear': book['publicationYear']
    }

@app.route("/book/summary", methods=["GET"])
def get_book_summary():
    info = getBookSummary(book)
    result = f"Title: {info['title']}, Author: {info['author']}, Genre: {info['genre']}, Published: {info['publicationYear']}"
    return jsonify({ "summary": result })

# Stock Status
def checkStockAndOrder(book):
    return {
        'isAvailable': book['isAvailable'],
        'stock': book['stock']
    }

@app.route("/book/stock-status", methods=["GET"])
def stock_status():
    info = checkStockAndOrder(book)
    return jsonify({
        'status': info['isAvailable'],
        'stock': info['stock']
    })

if __name__ == "__main__":
   app.run()


