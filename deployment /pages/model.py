import streamlit as st
import pandas as pd 
import pickle
import ast 
import numpy as np

# memanggil model yang sudah di simpan
with open('pipeline.pkl', 'rb') as file_1:
  pipeline = pickle.load(file_1)


with open('model_svc_best.pkl', 'rb') as file_2:
  model_svc = pickle.load(file_2)

with open('list_num_columns.txt', 'r') as file_3:
  list_num_columns = file_3.read()

with open('list_cat_columns.txt', 'r') as file_4:
  list_cat_columns = file_4.read()


# merubah nama-nama column menjadi list agar mudah dalam pemanggilan
list_num_columns = ast.literal_eval(list_num_columns)
list_cat_columns = ast.literal_eval(list_cat_columns)


st.header('Predcit your loyalty of your employees !!')
gender = st.selectbox(label='Gender',options=['Male','Female','Other'])
relevent_experience = st.selectbox(label='Relevent Experience',options=[ 'Has relevent experience', 'No relevent experience'])
enrolled_university = st.selectbox(label='Enrolled University',options=['no_enrollment' , 'Part time course', 'Full time course'])
education_level =  st.selectbox(label='Education Level',options=['Primary School', 'High School' ,'Graduate' ,'Masters' ,'Phd' ])
major_discipline = st.selectbox(label='Major Discipline',options=['STEM' ,'Business Degree' ,'Arts' ,'Humanities','Other'  ,'No Major'])
company_size = st.selectbox(label='Company Size',options=['<10','10/49','50-99', '100-500','500-999','1000-4999','5000-9999' ,'10000+'  ])
company_type = st.selectbox(label='Company Type',options =['Pvt Ltd', 'Funded Startup',  'Public Sector','Early Stage Startup', 'NGO','Other'])
last_new_job = st.selectbox(label='Last New Job',options=['never','1','2','3','4' ,'>4' ])
experience_category = st.selectbox(label='Experience Category',options=['Junior','Intermediate','Senior','Veteran'])
city_development_index = st.slider('City Development Index',0.0, 1.0, 0.5 )

data_inf = pd.DataFrame({
    'gender': gender,
    'relevent_experience': relevent_experience,
    'enrolled_university': enrolled_university,
    'education_level': education_level,
    'major_discipline': major_discipline,
    'company_size': company_size,
    'company_type': company_type,
    'last_new_job': last_new_job,
    'experience_category': experience_category,
    'city_development_index': city_development_index,
    
},index=[0])

if st.button(label='predict loyality of your employees!'):
    df_inf_fix = data_inf[list_cat_columns+list_num_columns]
    df_inf_fix
    df_inf_prep = pipeline.transform(df_inf_fix)
    y_inf_predict = model_svc.predict(df_inf_prep)

    st.write(y_inf_predict[0])
    if y_inf_predict == 0:
      st.write('Karyawan Terprediksi Loyal')
    else:
      st.write('Karyawan Terprediksi tidak Loyal')
   
