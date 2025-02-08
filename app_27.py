from flask import Flask, request, jsonify

app = Flask(__name__)

# Data
watchList = [
   {
      "videoId": 1,
      "title": "Javascript Tutorial",
      "watched": False,
      "url": "https://youtube.be/shorturli1",
   },
   {
      "videoId": 2,
      "title": "Node.js Basics",
      "watched": True,
      "url": "https://youtube.be/shorturl2",
   },
   {
      "videoId": 3,
      "title": "React.js Guide",
      "watched": False,
      "url": "https://youtube.be/shorturl3",
   },
]

def updated_watched_status_by_id(watchList ,video_id, watched):
    for video in watchList:
        if video['videoId'] == video_id:
           video["watched"] = watched
           break
    return watchList

@app.route("/watchlist/update-status", methods=["GET"])
def updated_watchlist():
    video_id = int(request.args.get("videoId"))
    watched = request.args.get("watched").lower() == "true"
    result = updated_watched_status_by_id(watchList ,video_id, watched) 
    return jsonify(result)

def update_all_videos_watched_status(watch_list, watched):
    for video in watch_list:
        video["watched"] = watched
    return watch_list    

@app.route("/watchlist/update-all", methods = ["GET"])
def update_all_watchlist_status():
    watched = request.args.get("watched") == "true"
    result = update_all_videos_watched_status(watchList, watched)
    return jsonify(result)

def is_unwatched(video):
    return not video["watched"]

@app.route("/watchlist/delete-watched", methods=["GET"])
def delete_watched_videos():
    final_list = list(filter(is_unwatched, watchList))
    return jsonify(final_list)

if __name__ == "__main__":
   app.run() 
