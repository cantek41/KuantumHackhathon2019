import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel(r'model/rr.xls')



#h=0 x=1 z=2 y=3

sonuclar=data.cikis
data = data.drop(['kapilar'], axis = 1)
data = data.drop(['cikis'], axis = 1)
    
                                   

data = pd.DataFrame(data = data, index = range(2000))


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(data,sonuclar, test_size = 0.25, shuffle = False)

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(n_estimators = 20, random_state = 0)
rfr.fit(x_train,y_train)

tt=rfr.predict(x_test)


import pickle


filename = 'model/finalized_model.sav'
pickle.dump(rfr, open(filename, 'wb'))

#h=0 x=1 z=2 y=3

rfr.predict([[1,3,0,2,1]])






    
