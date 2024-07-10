import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl','rb'))
scalr = pk.load(open('scalr.pkl','rb'))

st.header("Loan Stauts:")

gender = st.selectbox("Gender:",['Male', 'Female'])
marrid = st.selectbox("Married:",['No', 'Yes'])
dep = st.selectbox("Dependents:",['0','1','2','3+'])
edu = st.selectbox('Education:',['Graduate', 'Not Graduate'])
self_emp = st.selectbox('Self_Employed:',['No', 'Yes'])
ap_income = st.slider('ApplicantIncome:',0,200000)
co_ap_in = st.slider('CoapplicantIncome',0,100000)
loanamt = st.slider('LoanAmount:',0,100000)
loam_amt_term = st.slider('Loan_Amount_Term:',0,500)
creadit_his = st.selectbox('Credit_History:',[1,  0])
property_area = st.selectbox('Property_Area:',['Urban', 'Rural', 'Semiurban'])

if gender == 'Male':
     gen = 1
else:
     gen = 0

if marrid == 'Yes':
     marrid = 1
else:
     marrid = 0

if dep == '0':
     dep_0 = 1
else:
     dep_0 = 0

if dep == '1':
     dep_1 = 1
else:
     dep_1 = 0


if dep == '2':
     dep_2 = 1
else:
     dep_2 = 0


if dep == '3+':
     dep_3 = 1
else:
     dep_3 = 0


if edu == 'Graduate':
     edu = 1
else:
     edu = 0

if property_area == 'Urban':
     ur = 1
else:
     ur = 0

if property_area == 'Rural':
     ru = 1
else:
     ru = 0

if property_area == 'Semiurban':
     su = 1
else:
     su = 0


if creadit_his == 1:
     creadit_his = 1
else:
     creadit_his = 0

if self_emp == 'Yes':
     self_emp = 1
else:
     self_emp = 0


if st.button("predict"):
     pred_data = pd.DataFrame([[ap_income,co_ap_in,loanamt,loam_amt_term,gen,marrid,dep_0,dep_1,dep_2,dep_3,edu,self_emp,creadit_his,ur,ru,su]],columns=['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Male', 'Married_yes', 'Dependents_0',
       'Dependents_1', 'Dependents_2', 'Dependents_3+', 'Graduate',
       'Self_Employed_Yes', 'Credit_History_yes', 'Urban', 'Rural',
       'Semiurban'])
     pred_data = scalr.transform(pred_data)
     predict = model.predict(pred_data)
     st.markdown(predict)

