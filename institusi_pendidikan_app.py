import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Application_mode, encoder_Course, \
    encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Displaced, \
    encoder_Educational_special_needs, encoder_Fathers_occupation, \
    encoder_Fathers_qualification, encoder_Gender, encoder_International, \
    encoder_Marital_status, encoder_Mothers_occupation, \
    encoder_Mothers_qualification, encoder_Nacionality, \
    encoder_Previous_qualification, encoder_Scholarship_holder, \
    encoder_Tuition_fees_up_to_date
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Institusi Pendidikan App')

data = pd.DataFrame()
 
col1, col2, col3 = st.columns(3)
 
with col1:
    Application_mode = st.selectbox(label='Application_mode', options=encoder_Application_mode.classes_, index=1)
    data["Application_mode"] = [Application_mode]
 
with col2:
    Course = st.selectbox(label='Course', options=encoder_Course.classes_, index=0)
    data["Course"] = [Course]

with col3:
    Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.classes_, index=0)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]

col1, col2, col3 = st.columns(3)

with col1:
    Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, index=0)
    data["Debtor"] = [Debtor]

with col2:
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, index=0)
    data["Displaced"] = [Displaced]

with col3:
    Educational_special_needs = st.selectbox(label='Educational_special_needs', options=encoder_Educational_special_needs.classes_, index=0)
    data["Educational_special_needs"] = [Educational_special_needs]

col1, col2, col3 = st.columns(3)

with col1:
    Fathers_occupation = st.selectbox(label='Fathers_occupation', options=encoder_Fathers_occupation.classes_, index=0)
    data["Fathers_occupation"] = [Fathers_occupation]

with col2:
    Fathers_qualification = st.selectbox(label='Fathers_qualification', options=encoder_Fathers_qualification.classes_, index=0)
    data["Fathers_qualification"] = [Fathers_qualification]

with col3:
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=0)
    data["Gender"] = [Gender]

col1, col2, col3 = st.columns(3)

with col1:
    International = st.selectbox(label='International', options=encoder_International.classes_, index=0)
    data["International"] = [International]

with col2:
    Marital_status = st.selectbox(label='Marital_status', options=encoder_Marital_status.classes_, index=0)
    data["Marital_status"] = [Marital_status]

with col3:
    Mothers_occupation = st.selectbox(label='Mothers_occupation', options=encoder_Mothers_occupation.classes_, index=0)
    data["Mothers_occupation"] = [Mothers_occupation]

col1, col2, col3 = st.columns(3)

with col1:
    Mothers_qualification = st.selectbox(label='Mothers_qualification', options=encoder_Mothers_qualification.classes_, index=0)
    data["Mothers_qualification"] = [Mothers_qualification]

with col2:
    Nacionality = st.selectbox(label='Nacionality', options=encoder_Nacionality.classes_, index=0)
    data["Nacionality"] = [Nacionality]

with col3:
    Previous_qualification = st.selectbox(label='Previous_qualification', options=encoder_Previous_qualification.classes_, index=0)
    data["Previous_qualification"] = [Previous_qualification]

col1, col2 = st.columns(2)

with col1:
    Scholarship_holder = st.selectbox(label='Scholarship_holder', options=encoder_Scholarship_holder.classes_, index=0)
    data["Scholarship_holder"] = [Scholarship_holder]

with col2:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=encoder_Tuition_fees_up_to_date.classes_, index=0)
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Admission_grade = st.number_input(label='Admission_grade', min_value=0.0, max_value=20.0, value=10.0, step=0.1)
    data["Admission_grade"] = [Admission_grade]

with col2:
    Age_at_enrollment = st.number_input(label='Age_at_enrollment', min_value=0, max_value=100, value=18, step=1)
    data["Age_at_enrollment"] = [Age_at_enrollment]

with col3:
    Application_order = st.number_input(label='Application_order', min_value=0, max_value=1000, value=1, step=1)
    data["Application_order"] = [Application_order]

with col4:
    Curricular_units_1st_sem_credited = st.number_input(label='Curricular_units_1st_sem_credited', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_1st_sem_credited"] = [Curricular_units_1st_sem_credited]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_1st_sem_enrolled = st.number_input(label='Curricular_units_1st_sem_enrolled', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_1st_sem_enrolled"] = [Curricular_units_1st_sem_enrolled]

with col2:
    Curricular_units_1st_sem_evaluations = st.number_input(label='Curricular_units_1st_sem_evaluations', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_1st_sem_evaluations"] = [Curricular_units_1st_sem_evaluations]

with col3:
    Curricular_units_1st_sem_approved = st.number_input(label='Curricular_units_1st_sem_approved', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_1st_sem_approved"] = [Curricular_units_1st_sem_approved]

with col4:
    Curricular_units_1st_sem_grade = st.number_input(label='Curricular_units_1st_sem_grade', min_value=0.0, max_value=20.0, value=10.0, step=0.1)
    data["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_1st_sem_without_evaluations = st.number_input(label='Curricular_units_1st_sem_without_evaluations', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_1st_sem_without_evaluations"] = [Curricular_units_1st_sem_without_evaluations]

with col2:
    Curricular_units_2nd_sem_credited = st.number_input(label='Curricular_units_2nd_sem_credited', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_2nd_sem_credited"] = [Curricular_units_2nd_sem_credited]

with col3:
    Curricular_units_2nd_sem_enrolled = st.number_input(label='Curricular_units_2nd_sem_enrolled', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_2nd_sem_enrolled"] = [Curricular_units_2nd_sem_enrolled]

with col4:
    Curricular_units_2nd_sem_evaluations = st.number_input(label='Curricular_units_2nd_sem_evaluations', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_2nd_sem_evaluations"] = [Curricular_units_2nd_sem_evaluations]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_2nd_sem_approved = st.number_input(label='Curricular_units_2nd_sem_approved', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_2nd_sem_approved"] = [Curricular_units_2nd_sem_approved]

with col2:
    Curricular_units_2nd_sem_grade = st.number_input(label='Curricular_units_2nd_sem_grade', min_value=0.0, max_value=20.0, value=10.0, step=0.1)
    data["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]

with col3:
    Curricular_units_2nd_sem_without_evaluations = st.number_input(label='Curricular_units_2nd_sem_without_evaluations', min_value=0, max_value=100, value=0, step=1)
    data["Curricular_units_2nd_sem_without_evaluations"] = [Curricular_units_2nd_sem_without_evaluations]
    
with col4:
    GDP = st.number_input(label='GDP', min_value=0.0, max_value=100000.0, value=10000.0, step=100.0)
    data["GDP"] = [GDP]

col1, col2, col3 = st.columns(3)

with col1:
    Inflation_rate = st.number_input(label='Inflation_rate', min_value=0.0, max_value=100.0, value=2.0, step=0.1)
    data["Inflation_rate"] = [Inflation_rate]

with col2:
    Previous_qualification_grade = st.number_input(label='Previous_qualification_grade', min_value=0.0, max_value=20.0, value=10.0, step=0.1)
    data["Previous_qualification_grade"] = [Previous_qualification_grade]

with col3:
    Unemployment_rate = st.number_input(label='Unemployment_rate', min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    data["Unemployment_rate"] = [Unemployment_rate]
    
with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Status: {}".format(prediction(new_data)))
