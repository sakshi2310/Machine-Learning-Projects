import pickle as pk
import pandas as pd
import streamlit as st


data = pk.load(open('data.pkl','rb'))
model = pk.load(open('model.pkl','rb'))

print(data)



st.header("Laptop Price Prestion")

company = st.selectbox("Select company Name:", data['Company'].unique())

typename = st.selectbox("Select TypeName :",data['TypeName'].unique())

ram = st.selectbox('Ram :',data['Ram'].unique())

opsys = st.selectbox("Opsys : ",data['OpSys'].unique())

weight = st.number_input("Weight of Laptop[KG]")

touchscreen = st.selectbox("Tousch Screen : ",['Yes','No'])

hd = st.selectbox("Full HD : ",['Yes','No'])

cpu = st.selectbox("Cpu",data['cpu brand'].unique())

gpu = st.selectbox("Cpu",data['GPU_type'].unique())

Inch = st.number_input("Inch")
resolution = st.selectbox("Resolution",['1366x768','1600x900','1920x1080','1920x1200','2560x1440','2560x1600','2304x1440','3200x1800','3840x2160','4096x2160'])

ssd = st.selectbox("SSD[GB]",[0,8,16,32,64,128,256,512,1024])

hdd = st.selectbox("HDD[GB]",[0,64,128,264,512,1024,2048])



if st.button("Predict"):

    if hd == "Yes":
        hd = 1
    else:
        hd = 0

    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0    

    X_res = int(resolution.split("x")[0])
    Y_res = int(resolution.split("x")[1])
    screen_size = float(Inch)

    if Inch != 0:
        ppi = ((X_res**2)+(Y_res**2))**0.5/Inch
    else:
        ppi = 0

    predict_data = pd.DataFrame([[company,typename,ram,opsys,weight,touchscreen,hd,ppi,cpu,gpu,ssd,hdd]],columns=['Company', 'TypeName', 'Ram', 'OpSys', 'Weight', 'Touchscreen',
       'Full HD', 'ppi', 'cpu brand', 'GPU_type', 'SSD', 'HDD'],)   
    print(predict_data)
    predict = model.predict(predict_data)
    st.markdown(predict)
  