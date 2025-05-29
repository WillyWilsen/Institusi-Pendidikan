import joblib
 
model = joblib.load("model/log_model.joblib")
result_target = joblib.load("model/encoder_target.joblib")

def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
 
    Returns:
        str: Prediction result (Good, Standard, or Poor)
    """
    desired_order = [
        "Marital_status",
        "Application_mode",
        "Application_order",
        "Course",
        "Daytime_evening_attendance",
        "Previous_qualification",
        "Previous_qualification_grade",
        "Nacionality",
        "Mothers_qualification",
        "Fathers_qualification",
        "Mothers_occupation",
        "Fathers_occupation",
        "Admission_grade",
        "Displaced",
        "Educational_special_needs",
        "Debtor",
        "Tuition_fees_up_to_date",
        "Gender",
        "Scholarship_holder",
        "Age_at_enrollment",
        "International",
        "Curricular_units_1st_sem_without_evaluations",
        "Curricular_units_2nd_sem_without_evaluations",
        "Unemployment_rate",
        "Inflation_rate",
        "GDP",
        "pc1_1",
        "pc1_2",
        "pc1_3"
    ]
    data = data[desired_order]
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)[0]
    return final_result