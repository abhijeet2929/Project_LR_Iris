
from flask import Flask, jsonify,render_template,request

#importing the required function from flask

#import our flower class from utils.py and Project_app folder
from Project_app.utils import Flower
#Creates the Flask instance.
# __name__ is the name of the current python module.
#the app needs to know where it's located to set up some paths.
#__name__ is a convenient way to tell it that.

app= Flask(__name__)

########################## BASE API #############################
@app.route("/")
def Hello_Flask():
    print("Welcome to the base API")
    return "HI THIS BASE API"

@app.route("/predict_species")
def get_predicted_species():

    SepalLengthCm = 6.3
    SepalWidthCm  = 3.3
    PetalLengthCm = 6
    PetalWidthCm  = 2.5

    #creating instance of class
    f1 = Flower(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    species= f1.get_predicted_species()

    return jsonify({"Result":f"The Logistic Model has Predicted the Soecies of the test data as :{species}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)

    # it allows you to execute code when the file runs as a script,
    # but not when its imported as a module.
        
