from flask import Flask, request, jsonify

app = Flask(__name__)

# Welcome Route
@app.route("/", methods=["GET"])
def api_welcome():
   return jsonify({ "message": "Welcome to the Student Assignment Management System." })

def length(title):
  return len(title)   

# Assignment title length
@app.route("/title-length", methods=["GET"])
def get_length():
    title = request.args.get("title", "")
    title_length = length(title)
    return f"Assignment title length: {title_length}" 

def extract_initials(full_name):
    try:
       names = full_name.split()
       initials = "".join(name[0] for name in names)
       return initials.upper()
    except Exception as e:
       return f"Error extracting initials: {str(e)}"
        
# Extracting intials from a student name
@app.route("/extract-initials", methods=["GET"])
def extractingInitials():
    name = request.args.get("name", "")
    if not name:
       return jsonify({"error": "Name is required"}), 400
    
    initials = extract_initials(name)
    return f"Student initials: {initials}" 

def create_slug(title):
    try:
     slug = title.replace(" ","-").lower()
     return slug  
    except Exception as e:
       return f"Error creating slug: {str(e)}"     

# Assignmnt Slug
@app.route("/create-slug", methods=["GET"])
def get_slug():
    title = request.args.get("title", "")
    if not title:
       return jsonify({"error": "Title is required"}), 400
    
    slug = create_slug(title)
    return f"Assignment slug: {slug}"

def totalMarks(sub1, sub2, sub3):
    return sub1+sub2+sub3 

# Calculate total marks
@app.route("/calculate-total-marks", methods=["GET"])
def calculate():
   marks1 = int(request.args.get("marks1", 0))
   marks2 = int(request.args.get("marks2", 0))
   marks3 = int(request.args.get("marks3",0))
   if not marks1 or not marks2 or not marks3:
      return jsonify({"error": "Marks1, Marks2, Marsk3 all fields are required"}), 400
   
   result = str(totalMarks(marks1, marks2, marks3))
   return f"Total marks: {result}"

def calculateAvgMarks(sub1, sub2, sub3):
    return (sub1+sub2+sub3) / 3
    
# Calculate Average Marks
@app.route("/calculate-average-marks", methods=["GET"])
def calculateAvg():
  marks1 = int(request.args.get("marks1", 0))
  marks2 = int(request.args.get("marks2", 0))
  marks3 = int(request.args.get("marks3", 0))

  if not marks1 or not marks2 or not marks3:
     return jsonify({"error": "Marks1, Marks2, Marks3 all fields are required."}), 400

  result = round(calculateAvgMarks(marks1, marks2, marks3), 2)
  return f"Average marks: {result}" 
    
def gradeCalculation(marks):
    if marks >= 90:
       result = "A"
    elif 80 <= marks < 90:
       result = "B"
    elif 70 <= marks < 80:
       result = "C"
    elif 35 <= marks < 70:
       result = "D"
    elif marks < 35:
       result = "F"

    return result               

# Calculate grade
@app.route("/calculate-grade", methods=["GET"])
def gradeCal():
    totalMarks = int(request.args.get("totalMarks", 0))

    if not totalMarks:
       return jsonify({"error": "Total marks are required"}), 400
      
    result = gradeCalculation(totalMarks)
    return f"Grade: {result}" 

def checkPassFail(marks):
    if marks >= 40:
       reuslt = "Pass"
    elif marks <40:
       reuslt = "Fail"
    return reuslt      

# Check Pass Or Fail
@app.route("/check-pass-fail", methods=["GET"])
def check():
    marks = int(request.args.get("marks", 0))

    if not marks:
       return jsonify({"error": "Marks are required."})
    
    result = checkPassFail(marks)
    return f"{result}"

def checkScholar(marks, attendance):
    if marks >= 85 and attendance >= 90:
       result = "Eligible"
    else:
       result = "Not eligible"
    return result      

# Check eligibility for scholarship
@app.route("/check-scholarship", methods=["GET"])
def checkScholarship():
   marks = int(request.args.get("marks", 0))
   attendance = int(request.args.get("attendance", 0))

   if not marks or not attendance:
      return jsonify({"error": "All fields are required"}), 400
   
   result = checkScholar(marks, attendance)
   return f"{result} for scholarship"

def calculatePenalty(daysLate, penaltyPerDay):
   return daysLate * penaltyPerDay
   
# Calculate late submission penalty
@app.route("/calculate-late-penalty", methods=["GET"])
def penalty():
   daysLate = int(request.args.get("daysLate", 0))
   penaltyPerDay = int(request.args.get("penaltyPerDay", 0))

   if not daysLate or not penaltyPerDay:
      return jsonify({"error", "All fields are required"})
   
   result = calculatePenalty(daysLate, penaltyPerDay)
   return f"Total Penalty: {result}"

def calculateStudyHours(dailyHours, totalDays):
    return dailyHours * totalDays

# Estimate Study hours
@app.route("/estimate-study-hours", methods=["GET"])
def estimateStudy():
     dailyHours = int(request.args.get("dailyHours", 0))
     totalDays = int(request.args.get("totalDays", 0))

     if not dailyHours or not totalDays:
        return jsonify({"error": "All fields are required"}), 400

     result = calculateStudyHours(dailyHours, totalDays)
     return f"Total study hours {result}"   

# Topics Data
topics_data = {
    'AI': ['Machine Learning', 'Neural Networks', 'Natural Language Processing'],
    'Web Development': ['HTML', 'CSS', 'JavaScript', 'React'],
    'Data Science': ['Data Analysis', 'Visualization', 'Pandas', 'NumPy']
}

def recommendTopics(interest):
    recommended_topics = topics_data.get(interest, [])
    if recommended_topics:
       return f"Recommended Topics: {', '.join(recommended_topics)}"
    else:
       return "No recommended topics found for the given interest."
    
# Recommend Assignment Topics
@app.route("/recommend-topics", methods=["GET"])
def get_recommended_topics():
    interest = request.args.get("interest", "")
    if not interest:
       return "Interest field is missing", 400

    recommendations = recommendTopics(interest)
    return recommendations    

if __name__ == "__main__":
   app.run() 
