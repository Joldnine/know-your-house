import pandas as pd
import sklearn
import json
import time
import googlemaps
import Places
import numpy as np

from Places import Places

from sklearn import linear_model

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import pickle ## for saving weights of models


##def query_dist(list_address):
##    conn = http.client.HTTPSConnection("xwyk10og58.execute-api.ap-southeast-1.amazonaws.com")
##
##    payload = "{\n\t\"street\": [\"5 Dover Crescent\", \"ANG MO KIO AVE 4\"]\n}"
##    
##    payload = "{\n\t\"street\": "+ json.dumps(list_address) +"\n}" 
##    headers = {
##        'content-type': "application/json"
##    }
##
##    conn.request("POST", "/develop", payload, headers)
##
##    res = conn.getresponse()
##    data = res.read()
##    #print data
##    # (data.decode("utf-8"))
##    b =  data.decode("utf-8")
##    while 'message' in json.loads(b):
##        print 'Sigh'
##        ret = query_dist(list_address)
##    #if json.loads(b)['message']== "Endpoint request timed out":
##        #query_dist(list_address)
##    
##    a = json.loads(json.loads(b)['body'])
##    ret = [e['direction']['distance']['text'] for e in a]
##    return ret
##

if __name__ == "__main__":
    df1 = pd.read_csv("resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv")

    df2 = pd.read_csv("resale-flat-prices-based-on-registration-date-from-jan-2015-onwards.csv")
    df2 = df2.drop('remaining_lease',axis=1)
    print(df1)

    df3 = pd.read_json("address_type_num.json")
    print(df3)

    #combine df1 and df2 together
    df = pd.concat([df1,df2]).infer_objects()

    #df = pd.concat

    #Get all town areas in singapore
    town_areas =  df.town.unique()

    #filter transactions for the 3 types pf flats
    flat_types = ['3 ROOM','4 ROOM','5 ROOM']
    df = df.loc[df['flat_type'].isin(flat_types)]

    datasets = []

    df['time_step'] = df['month'].map(lambda x: int(x[0:4])-2012)
    df['age'] = df['month'].map(lambda x: int(x[0:4])) - df['lease_commence_date']
    df['floor'] = (df['storey_range'].map(lambda x: int(x[0:2])) + df['storey_range'].map(lambda x: int(x[-2:])))/2
    df['address'] = df['block']+" "+df['street_name']

    df = pd.merge(df, df3, on='address')

    addresses = df.address.unique()
    n = len(addresses)

    with open('addresses.txt', 'w') as f_addresses:
        f_addresses.write(json.dumps(list(addresses)))
    f_addresses.close()

    f_mrt = open('mrt_dist.txt', 'r')
    data_dist_mrt = f_mrt.read()
    data_dist_mrt = [(e1).split('\t') for e1 in data_dist_mrt.split('\n')][:-1]
    for i in range(len(data_dist_mrt)):
        metric = data_dist_mrt[i][1].split(' ')[1]
        if metric == 'm':
            data_dist_mrt[i][1] = float(data_dist_mrt[i][1].split(' ')[0])/1000.0
        else:
            data_dist_mrt[i][1] = float(data_dist_mrt[i][1].split(' ')[0])
    f_mrt.close()

    
    ##dict_mrt_dist =  dict([tuple((e1).split('\t')) for e1 in data_dist_mrt.split('\n')][:-1])
    dict_mrt_dist =  dict([tuple(e1) for e1 in data_dist_mrt])

##    place = Places('AIzaSyBtoWfKhyiLdLrv_6VfkvTyNi0lzEWofRU')
##    place = Places('AIzaSyCxEmfvdo2fiGIZ7zJVsH-QDGJ8Oz3GwBk')
##    place = Places('AIzaSyDX_p3RqFd88q9nHHzg3AkmDvuSUJ8McSs')
##    place = Places('AIzaSyD3EMLApQNuEP3iCXnfUClBpGrqx30gUq4')
##    place = Places('AIzaSyBFh1fMOhG_Y7-1p2qq07-dEBIrNs0tMws')
##    place = Places('AIzaSyBPVMnvgNrhJUK5dYkSygm322ZA4Ot0mbU')
##    place = Places('AIzaSyBw4zq1tBIpqivS9ziZsZj9WRpl-oOnCh8')
##    place = Places('AIzaSyDD0hFpX1F5cqXh1U6Q_LaZOhwkXOUWPqw')
##    place = Places('AIzaSyBhLErngBmgDAkEjFpfoH1veMYEeZfqkBE')
##    
##    for i in range(7003,n):
##        tmp_key = addresses[i]
##        if "C'WEALTH" in tmp_key:
##            tmp_key = tmp_key.replace("'","").replace("CWEALTH","COMMONWEALTH")
##        print tmp_key
##        try:
##            tmp_val = place.mrt_dist(tmp_key)
##        except IndexError:
##            tmp_val = '0.0 km'
##        f_mrt_dist =  open('mrt_dist.txt', 'a')
##        f_mrt_dist.write( tmp_key + '\t' + tmp_val + '\n')
##        f_mrt_dist.close()
##        
##        print i+1
        
##    with open('mrt_dist.txt', 'w') as f_mrt:
##        f_mrt.write(json.dumps(mrt_dists))
##    f_mrt.close()

    #df['mrt_distance'] = df['address'].map(dict_mrt_dist).map(lambda x: float(x[:-2]) if x[-2:]=='km' else float(x[:-2])/1000.0)
    df['mrt_distance'] = df['address'].map(dict_mrt_dist).map(lambda x: float(x))

    df = df.reset_index()
    df.to_csv('populated_dataset.csv', sep=',')
    for ta in town_areas:
        dataset_place = []
        for ft in flat_types:
            df1 = df.loc[(df['month']!='0') & (df['town'] == ta) & (df['flat_type']== ft) ]
            df2 = df1[['time_step','floor_area_sqm','age','resale_price','mrt_distance','floor','num_mall','num_mrt','num_school']]
            print(df2)
            df2 = df2.dropna(axis=0, how='any')
            dataset_place += [df2]
        datasets += [dataset_place]


    for i in range(len(datasets)):      #Region in Singapore
        for j in range(3):              #Flat-type
            if (datasets[i][j]).shape[0]!=0:
                X = datasets[i][j][['time_step','floor_area_sqm','age','floor','mrt_distance','num_mall','num_mrt','num_school']] ## need to include more factors such as school_distance? ## X usually means our input variables (or independent variables)
                y = datasets[i][j][['resale_price']] ## Y usually means our output/dependent variable
                lm = linear_model.LinearRegression()

                train_x,test_x,train_y,test_y = train_test_split( X, y, test_size = 0.8, random_state = 26)
                #np.any(np.isnan(X))
                # print(X)
                #np.any(np.isnan(y))
                # print(y)
                model = lm.fit(train_x,train_y)


                #saving trained model to file
                pkl_filename = open(town_areas[i].replace('/',' or ')+' '+flat_types[j]+'.pkl','wb')
                pickle.dump(model, pkl_filename)
                pkl_filename.close()

                #opening trained model 
                pkl_filename = open(town_areas[i].replace('/',' or ')+' '+flat_types[j]+'.pkl','rb')
                pickle_model = pickle.load(pkl_filename)
                pkl_filename.close()
                
                #use for predicting prices using inputs
                predictions = lm.predict(X)

                test = lm.predict(test_x)
                print(r2_score(test,test_y))

                
                #print (pickle_model.score(X,y))
    