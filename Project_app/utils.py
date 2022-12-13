#write a small python function and classes to make common patterns shorter and easier
#it is not a complate collections


import pickle
import json
import config
import numpy as np

class Flower():

    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        #constructor for creating instance of all the variables

        self.SepalLengthCm= SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.petalLengthCm= PetalLengthCm
        self.PetalWidthCm = PetalWidthCm


    def load_model(self):
        print("We are in load_module_function")
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

        with open (config.JSON_FILE_PATH,"r") as f:
            self.json_data= json.load(f)

    def get_predicted_species(self):
        self.load_model()

        test_array=np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.SepalLengthCm
        test_array[1] = self.SepalWidthCm 
        test_array[2] = self.petalLengthCm
        test_array[3] = self.PetalWidthCm


        print("test array is:",test_array)
        a=str(int(np.around(self.model.predict([test_array]),0)))
        predicted_species = self.json_data["Species"][a]

        return predicted_species
