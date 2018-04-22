import pickle
import os

class Prices(object):

	def predict_price(self, town_areas, flat_types, time_step, floor_area_sqm, age, floor, mrt_distance, num_mall, num_mrt, num_school):

		pkl_filename = "model.pkl"  

		des_filename = town_areas + ' ' + flat_types + '.pkl'

		directory = "/Users/jim/Desktop/price/pkl dataset"

		for file in os.listdir(directory):
		    filename = os.fsdecode(file)
		    if filename == des_filename: 
		        pkl_filename = filename
		    else:
		        continue

		if(pkl_filename==des_filename) :
			with open(directory + "/" + pkl_filename, 'rb') as file:  
			    pickle_model = pickle.load(file)

			Xtest = [[time_step,floor_area_sqm,age,floor,mrt_distance,num_mall,num_mrt,num_school]]

			#score = pickle_model.score(Xtest, Ytest)  
			#print("Test score: {0:.2f} %".format(100 * score))  
			Ypredict = pickle_model.predict(Xtest)  
			#print(Ypredict)
			return Ypredict

		else:
			return 0


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
