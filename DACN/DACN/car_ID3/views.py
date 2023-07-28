from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.preprocessing import scale
import math
import pickle
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth.hashers import check_password
from .models import Car, User
import pandas as pd
import json
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
import graphviz
import numpy as np
from sklearn import tree



# Create your views here.

def index(request):
    request.session['islogin'] = False
    if request.method =='POST':
        user_from_post = json.load(request)['user']
        user = User.objects.get(username=user_from_post['username'])
        if (check_password(user_from_post['password'],user.password)):
            request.session['islogin'] = True
            return HttpResponse('')
    return render(request, 'login/index.html')

# def write_db(request):
#     file = staticfiles_storage.path("CarPrice_Assignment.csv")
#     df = pd.read_csv(file)
#     for row in df.itertuples():
#         car = Car(symboling=row[2], carname=row[3], fueltype=row[4], aspiration=row[5], doornumber=row[6], carbody=row[7], drivewheel=row[8], enginelocation=row[9], wheelbase=row[10], carlength=row[11], carwidth=row[12], carheight=row[13], curbweight=row[14], enginetype=row[15], cylindernumber=row[16], enginesize=row[17], fuelsystem = row[18], boreratio=row[19], stroke=row[20], compressionratio=row[21], horsepower=row[22], peakrpm=row[23], citympg=row[24], highwaympg=row[25], price=row[26])
#         car.save()
    

def adminPage(request):
    islogin = request.session.get('islogin', False)
    request.session.set_expiry(300)
    if islogin:
        if request.method =="POST":
            date_from_post = json.load(request)['date']
            date = date_from_post['date'].split('-')
            list_car = Car.objects.filter(create_date__gte=datetime(int(date[0]),int(date[1]),int(date[2])))
            car_df = pd.DataFrame.from_records([car.to_dict() for car in list_car])

            car_df['symboling'] = car_df['symboling'].astype('object')
            carnames = car_df['CarName'].apply(lambda x: x.split(" ")[0])
            # Sửa lại tên của 1 số hãng xe bị sai
            #volkswagen
            car_df['car_company']=carnames

            car_df.loc[(car_df['car_company']=="vw")|(car_df['car_company']=="vokswagen"),"car_company"]="volkswagen"
            #porsche
            car_df.loc[(car_df['car_company']=="porcshce"),"car_company"]="porsche"
            #toyota
            car_df.loc[(car_df['car_company']=="toyouta"),"car_company"]="toyota"
            # nissan
            car_df.loc[car_df['car_company'] == "Nissan", 'car_company'] = 'nissan'
            # mazda
            car_df.loc[car_df['car_company'] == "maxda", 'car_company'] = 'mazda'
            # sử dụng hàm numpy log1p áp dụng log (1 + x) cho tất cả các phần tử của cột
            car_df["price"] = np.log1p(car_df["price"])
            car_df["SalePrice_log"] = np.log(car_df.price)

            
            X=car_df.drop(columns=['price','SalePrice_log'])
            y=car_df['SalePrice_log']

            # tạo biến giả cho các biến phân loại
            cars_categorical = X.select_dtypes(include=['object'])
            cars_categorical.head(2)
            # Tạo biến giả
            cars_dummies = pd.get_dummies(cars_categorical)

            X=X.drop(columns=cars_categorical)
            X=pd.concat([X,cars_dummies],axis=1)

            cols=X.columns
            X=pd.DataFrame(scale(X))
            X.columns=cols
            # tách dữ liệu ra thành bộ tranning (70%) và test (30%) và độ ngẫu nhiên là 100
            X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        train_size=0.7,
                                                        test_size = 0.3, random_state=100)
            
            lm=DecisionTreeRegressor()
            lm.fit(X_train,y_train)

            y_pred_test=lm.predict(X_test)

            score = round(r2_score(y_true=y_test, y_pred=y_pred_test),2)
            # dot_data = tree.export_graphviz(lm,out_file=None, feature_names=X_train.columns, class_names=['uacc', 'acc', 'vgood', 'good'], filled=True, rounded=True, special_characters=True)
            # graph = graphviz.Source(dot_data)
            # file = staticfiles_storage.path("tree")
            # graph.render(file, format='png', view=False)
            return HttpResponse(score)
        return render(request,'home/admin.html')  
    return render(request, 'home/404error.html')  
    

def homePage(request):
    if request.method =='POST':
        data_from_post = json.load(request)['car']
        data_from_post['car_company'] = data_from_post['CarName'].split(' ')[0]
        df=pd.DataFrame(data_from_post, columns=['symboling','CarName','fueltype','aspiration',
        'doornumber','carbody','drivewheel','enginelocation','wheelbase','carlength','carwidth',
        'carheight','curbweight','enginetype','cylindernumber','enginesize','fuelsystem','boreratio',
        'stroke','compressionratio','horsepower','peakrpm','citympg','highwaympg','car_company'], index=[0])

        df['symboling'] = df['symboling'].astype('object')

        test_categorical = df.select_dtypes(include=['object'])
        list_test = []
        for col in test_categorical.columns:
            list_test.append((col+'_'+test_categorical[col].astype(str)).to_string().split('  ')[2])

        file = staticfiles_storage.path("Cars_dummy.csv")
        df2 = pd.read_csv(file, sep='\t')
        for col in list_test:
            df2[col]+=1
        
        df=df.drop(columns=test_categorical)
        df=pd.concat([df,df2],axis=1)
        cols=df.columns
        df=pd.DataFrame(scale(df))
        df.columns=cols
        file = staticfiles_storage.path("modelPredictCar")
        with open(file, 'rb') as file:
            lm = pickle.load(file)

        y_pred=lm.predict(df)
        car_pred = round(math.exp(math.exp(y_pred))-1, 2)
        car = Car(symboling=data_from_post['symboling'], carname=data_from_post['CarName'], fueltype=data_from_post['fueltype'], aspiration=data_from_post['aspiration'], 
            doornumber=data_from_post['doornumber'], carbody=data_from_post['carbody'], drivewheel=data_from_post['drivewheel'], enginelocation=data_from_post['enginelocation'], wheelbase=data_from_post['wheelbase'], 
            carlength=data_from_post['carlength'], carwidth=data_from_post['carwidth'], carheight=data_from_post['carheight'], curbweight=data_from_post['curbweight'], enginetype=data_from_post['enginetype'], 
            cylindernumber=data_from_post['cylindernumber'], enginesize=data_from_post['enginesize'], fuelsystem = data_from_post['fuelsystem'], boreratio=data_from_post['boreratio'], 
            stroke=data_from_post['stroke'], compressionratio=data_from_post['compressionratio'], horsepower=data_from_post['horsepower'], peakrpm=data_from_post['peakrpm'], citympg=data_from_post['citympg'], 
            highwaympg=data_from_post['highwaympg'])
        car.save()
        return HttpResponse(car_pred)

    return render(request, 'home/index.html')

