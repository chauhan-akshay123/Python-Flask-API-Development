from flask import Flask, request, jsonify

app = Flask(__name__)

# Data
movies = [
    {'id': 1, 'title': 'Inception', 'genre': 'Sci-Fi', 'available': True},
    {'id': 2, 'title': 'Titanic', 'genre': 'Romance', 'available': False},
    {'id': 3, 'title': 'The Dark Knight', 'genre': 'Action', 'available': True},
    {'id': 4, 'title': 'The Matrix', 'genre': 'Sci-Fi', 'available': True},
]

reviews = [
    {'id': 1, 'product_id': 1, 'rating': 4, 'content': 'Great laptop for work.'},
    {'id': 2, 'product_id': 2, 'rating': 5, 'content': 'Excellent sound quality.'},
    {'id': 3, 'product_id': 3, 'rating': 3, 'content': 'Works fine but feels cheap.'},
    {'id': 4, 'product_id': 4, 'rating': 4, 'content': 'Good value for money.'},
]

#  Update Movie Availability
def updateMovieAvailability(movies, id, available ):
    for movie in movies:
        if movie['id'] == id:
           movie['available'] = available
           break
    return movies

@app.route("/movies/update", methods=["GET"])
def update_movies():
    id = int(request.args.get("id"))
    available = request.args.get("available").lower() == "true"
    result = updateMovieAvailability(movies, id, available)
    return jsonify(result)      

# Delete Movie by ID
def deleteMovieById(movies ,movieId):
 return [movie for movie in movies if movie['id'] != movieId]

@app.route("/movies/delete", methods=["GET"])
def movies_delete():
    id = int(request.args.get("id"))
    result = deleteMovieById(movies, id)
    return jsonify({ "Remaining movies": result })

# Update Review Content
def updateReviewContent( reviews, id, content):
    for review in reviews:
        if review['id'] == id:
           review['content'] = content
           return review

@app.route("/reviews/update", methods=["GET"])
def reviews_update():
    id = int(request.args.get("id"))
    content = request.args.get("content", "")
    result = updateReviewContent(reviews, id, content)
    return jsonify({ "Updated Review": result })        
    
# Delete Review by Product ID
def deleteReviewsByProductId(reviews ,id):
    return [review for review in reviews if review['product_id'] != id] 

@app.route("/reviews/delete", methods=["GET"])
def reviews_delete():
    product_id = int(request.args.get("product_id"))
    result = deleteReviewsByProductId(reviews ,product_id)
    return jsonify(result)   

# Update Movie Genre
def updateMovieGenre(id, genre):
    for movie in movies:
        if movie['id'] == id:
           movie['genre'] = genre
           return movie

@app.route("/movies/update-genre", methods=["GET"])
def update_genre():
    id = int(request.args.get("id"))
    genre = request.args.get("genre", "")
    result = updateMovieGenre(id, genre)
    return jsonify({ "Upadeted Movie": result })     

# Delete Movie by Genre
def deleteMovieByGenre(genre):
    return [movie for movie in movies if movie['genre'] != genre]

@app.route("/movies/delete-by-genre", methods=["GET"])
def delete_by_genre():
    genre = request.args.get("genre")
    result = deleteMovieByGenre(genre)
    return jsonify({ "Remaining Movies": result })    

if __name__ == "__main__":
   app.run() 
