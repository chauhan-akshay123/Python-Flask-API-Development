from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/total-distance", methods=["GET"])
def total_distance():
    distance1 = float(request.args.get("distance1", 0))
    distance2 = float(request.args.get("distance2", 0))
    total_distance = distance1 + distance2
    return str(total_distance)

@app.route("/total-time", methods=["GET"])
def total_time():
  time1 = float(request.args.get("time1", ""))
  time2 = float(request.args.get("time2", ""))
  time3 = float(request.args.get("time3", ""))
  total_time = time1 + time2 + time3
  return str( total_time)

@app.route("/average-speed", methods=["GET"])
def average_speed():
   totalDistance = float(request.args.get("totalDistance", 0))
   totalTime = float(request.args.get("totalTime", 1))
   average_speed = totalDistance / totalTime
   return str(average_speed)

@app.route("/interest-earned", methods=["GET"])
def interest_earned():
    principal = float(request.args.get("principal", 0))
    rate = float(request.args.get("rate", 0))
    time = float(request.args.get("time", 0))
    
    interest_earned = (principal * rate * time) / 100
    return str(interest_earned)

if __name__ == "__main__":
  app.run()  
