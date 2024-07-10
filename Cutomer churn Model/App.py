import pandas as pd
import streamlit as st
import pickle as pk

data = pk.load(open('data.pkl','rb'))
model = pk.load(open('model.pkl','rb'))

st.title("Customer Churn Model")

credit_score = st.number_input("Enter the Credit Score:")
geography = st.selectbox("Geography : ",data['Geography'].unique())
Gender = st.selectbox("Gender : ",data['Gender'].unique())
age = st.number_input("Enter the Age:")
Tensure = st.slider("Year of Experience : ",0,30)
Balance = st.number_input("Enter the Balance : ")
Num_products = st.selectbox("Number of Products : ",data['NumOfProducts'].unique())
hascrcard = st.selectbox("Has Credit Card : ",['Yes','No'])
Isactive_number = st.selectbox("Active Number :",['Yes','No'])
Estimated_salary = st.number_input("Enter the Estimated Salary : ")

if hascrcard == 'Yes':
     hascrcard = 1
else:
     hascrcard = 0

if Isactive_number == 'Yes':
     Isactive_number = 1
else:
     Isactive_number = 0


if st.button('Predict'):
     predit_data = pd.DataFrame([[credit_score,geography,Gender,age,Tensure,Balance,Num_products,hascrcard,Isactive_number,Estimated_salary]],columns=['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance',
       'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary'])
     predict = model.predict(predit_data)
     if predict == 0:
          st.write("Exited")
     else:
          st.write("Not Exited")
     