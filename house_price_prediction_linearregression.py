from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import streamlit as st
import numpy as np

df = pd.read_csv('train.csv')

featurs = ['HouseStyle', 'OverallQual', 'RoofStyle', 'GrLivArea', 'GarageCars', 'TotalBsmtSF']
target = 'SalePrice'

x = df[featurs]
y = df[target]

cols = ['HouseStyle', 'RoofStyle']
x = pd.get_dummies(x, columns=cols)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# model 
#------------
model = LinearRegression()
# training the model
#------------
model.fit(x_train, y_train)


#-------------
# test the model
#-------------



st.title("House_price_prediction")

col1, col2 = st.columns(2)

with col1:
    oq= st.slider('OverallQual', min_value=1, max_value=10, value=7)

with col2:
    gla = st.slider('GrLivArea', min_value=100, max_value=10000, value=5000)
    
col3, col4 = st.columns(2)
with col3:
    gcs = st.slider("GarageCars", min_value=1, max_value= 10, value = 5)

with col4:
    tbs = st.slider("TotalBsmtSF", min_value=1, max_value=10000, value = 2000)

col5, col6 = st.columns(2)
with col5:
    RS = st.selectbox("RoofStyle", ['Flat', 'Gable', 'Gambrel', 'Hip', 'Mansard', 'Shed'])

with col6:
    HS = st.selectbox("HouseStyle", ['1Story', '1.5Fin', '1.5Unf', '2Story', '2.5Fin', '2.5Unf', 'SFoyer', 'SLvl'])

# gathering the data
result =  pd.DataFrame([[HS, oq, RS, gla, gcs, tbs]], columns=['HouseStyle', 'OverallQual', 'RoofStyle', 'GrLivArea', 'GarageCars', 'TotalBsmtSF'])
cols = ['HouseStyle','RoofStyle']
result = pd.get_dummies(result, columns=cols)

# adding the missing columns with zero value before sorting
#---------------------------
for col in x_train.columns:
    if col not in result.columns:
        result[col] = 0
        
# sorting the columns
#---------------------------
result = result[x_train.columns]

res = model.predict(result)[0]

def print_result():
    st.write("prediction result: ", res)
if st.button("predict"):
    print_result()
    
    