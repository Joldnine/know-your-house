import os
import pickle
import json
import sklearn
import numpy
import scipy


class Prices(object):
    def predict_price(self, town_area, flat_type, time_step, floor_area_sqm, age, floor, mrt_distance, num_mall, num_mrt,
                      num_school):
        pkl_filename = "model.pkl"
        des_filename = town_area + ' ' + flat_type + '.pkl'
        directory = "./pkl dataset"

        for file in os.listdir(directory):
            filename = file  # os.fsdecode(
            if filename == des_filename:
                pkl_filename = filename
            else:
                continue

        if pkl_filename == des_filename:
            with open(directory + "/" + pkl_filename, 'rb') as file:
                pickle_model = pickle.load(file)
            Xtest = [[time_step, floor_area_sqm, age, floor, mrt_distance, num_mall, num_mrt, num_school]]
            #score = pickle_model.score(Xtest, Ytest)
            #print("Test score: {0:.2f} %".format(100 * score))
            Ypredict = pickle_model.predict(Xtest)
            return Ypredict[0][0]
        else:
            return 0


def post(event, context):
    # event = json.loads(event['body'])  # comment this line if it is in aws
    town_area = event['town_area']
    flat_type = event['flat_type']
    time_step = 0
    floor_area_sqm = event['area_sqm']
    age = event['age']
    floor = event['floor']
    mrt_distance = event['mrt_distance']
    num_mall = event['num_mall']
    num_mrt = event['num_mrt']
    num_school = event['num_school']

    predict = Prices().predict_price(town_area, flat_type, time_step, floor_area_sqm, age, floor, mrt_distance,
                                     num_mall, num_mrt, num_school)
    print(predict)
    return {
        "body": json.dumps({
            "price": predict
        }),
        "statusCode": 200
    }

if __name__ == "__main__":
    town_areas = "ANG MO KIO"
    flat_types = "3 ROOM"

    time_step = 0
    floor_area_sqm = 122.0
    age = 19
    floor = 3.0
    mrt_distance = 0.7
    num_mall = 3
    num_mrt = 2
    num_school = 2

    predict = Prices().predict_price(town_areas,flat_types,time_step,floor_area_sqm,age,floor,mrt_distance,num_mall,num_mrt,num_school)
    print(predict)
