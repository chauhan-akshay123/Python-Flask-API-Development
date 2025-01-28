from flask import Flask, request, jsonify

app = Flask(__name__)

person = {
   "firstname": "Ajay",
   "lastname": "Sharma",
   "gender": "male",
   "age": 30,
   "isMember": True
}

def get_full_name(person):
   return f"{person['firstname']} {person['lastname']}"

@app.route("/person/fullname", methods=["GET"])
def get_person_full_name():
    full_name = get_full_name(person)
    return jsonify({"fullname": full_name})

def get_first_name_and_gender(person):
    return {"firstname": person['firstname'], "gender": person['gender']}

@app.route("/person/firstname-gender", methods=["GET"])
def get_person_first_name_and_gender():
    firstname_and_gender = get_first_name_and_gender(person)
    return jsonify(firstname_and_gender)

def increment_age(person):
    person['age'] += 1
    return person

@app.route("/person/increment-age", methods=["GET"])
def increment_person_age():
    updated_person = increment_age(person)
    return jsonify(updated_person)

male_image_url = "https://via.placeholder.com/150/0000FF?text=Male"
female_image_url = "https://via.placeholder.com/150/0000FF?text=Male"
unkown_image_url = "https://via.placeholder.com/150/0000FF?text=Unknown"

def get_profile_image(person):
    if person["gender"].lower() == "male":
     return male_image_url
    elif person["gender"].lower() == "female":
     return female_image_url
    else: 
     return unkown_image_url

@app.route("/person/profile-image", methods=["GET"])
def get_person_profile_image():
    profile_image = get_profile_image(person)
    return jsonify({"profileImage": profile_image})         

def get_final_price(cart_total, is_member):
    discount = 0.10
    if is_member:
       final_price = cart_total * (1-discount)
    else:
       final_price = cart_total
    return final_price 

@app.route("/person/final-price", methods=["GET"])
def get_person_final_price():
    cart_total = float(request.args.get("cartTotal", 0))
    final_price = get_final_price(cart_total, person['isMember'])
    return jsonify(final_price)    
   
if __name__ == "__main__":
   app.run() 
