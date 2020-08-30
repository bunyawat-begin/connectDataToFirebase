from firebase import firebase
import time
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
url = 'https://stonkfarm.firebaseio.com/'
messanger = firebase.FirebaseApplication(url)
poly = PolynomialFeatures()
a0 = 0
a1 = 1.37137677e+02
a2 = -2.65072239e-02
ac = -177253.31711047
b0 = 0
b1 = -5.93143949e+03
b2 = 3.49222871e+03
b3 = 1.18508179e+00
b4 = -1.38628172e+00
b5 = 2.75090747e-01
c = 7420894.90982285
while True:
    def predict(year):
        year = float(year)
        x_poly = poly.fit_transform([[year]])
        print(x_poly)
        result = (a0*x_poly[0][0])+(a1*x_poly[0][1])+(a2*x_poly[0][2])+ac
        print("result = ",result)
        return result
    def calculate(input_from_user):
        poly = PolynomialFeatures()
        x_poly = poly.fit_transform([[input_from_user,predict(input_from_user)]])
        result = (b0*x_poly[0][0])+(b1*x_poly[0][1])+(b2*x_poly[0][2])+(b3*x_poly[0][3])+(b4*x_poly[0][4])+(b5*x_poly[0][5])+c
        return int(result)
    time.sleep(3.0)
    last_output = messanger.get('/Output',None)
    data = messanger.get('/Input',None)
    user_input = []
    user_name = []
    user_number = []
    last = []
    last_name =[]
    last_number = []
    boy = {}
    last_user = {}
    for key,value in last_output.items():
        last.append(value)
    for i in last:
        last_name.append(i['name'])
        last_number.append(i['result'])
    i = 0
    for key,value in data.items():
        user_input.append(value)
    print('Reading Complete!!!')
    for i in user_input:
        user_name.append(i['name'])
        user_number.append(i["input"])
    print("Getting Data Complete")
    k = 0
    while k<len(user_number):
        user_number[k] = calculate(user_number[k])
        user_input[k].update(result = user_number[k])
        k+=1
    print('Editing Complete')
    a = 0
    while a<len(user_input):
        boy.update(name = user_name[a])
        boy.update(result = user_number[a])
        print(boy)
        try:
            last_user.update(name = last_name[a])
            last_user.update(result=last_number[a])
        except Exception as ex:
            print(ex)
        else:
            print(last_user)
            if boy == last_user:
                print(".....")
            else:
                user_name[a] = user_name[a].replace(".ac.th","")
                print(user_name[a])
                messanger.put('/Output',user_name[a],user_input[a])
                print("update ",user_name[a])
        finally:
            print('Done')
        a+=1

        