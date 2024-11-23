import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
heart_disease_model = pickle.load(open('D:\CacDuAnTrongVisualCode\DuDoanBenhTimMach\Train\trained_model.sav', 'rb'))
Combine_Heart = pickle.load(open('D:\CacDuAnTrongVisualCode\DuDoanBenhTimMach\Train\Combine_trained_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Heart Disease Prediction',
                           'Combine Heart'],
                          icons=['heart','heart'],
                          default_index=0)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=0, max_value=120, value=30)
        
    with col2:
        sex = st.selectbox('Sex', options=[0, 1], index=0)
        
    with col3:
        cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3], index=0)
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, value=120)
        
    with col2:
        chol = st.number_input('Serum Cholesterol', min_value=100, max_value=600, value=200)
        
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar', options=[0, 1], index=0)
        
    with col1:
       restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2], index=0)
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=50, max_value=220, value=150)
        
    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=[0, 1], index=0)
        
    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=1.0)
        
    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0, 1, 2], index=0)
        
    with col3:
        ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', options=[0, 1, 2, 3], index=0)
        
    with col1:
        thal = st.selectbox('Thalassemia Test Results', options=[0, 1, 2, 3], index=0)
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=0, max_value=120, value=30)
        
    with col2:
        sex = st.selectbox('Sex', options=[0, 1], index=0)
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, value=120)
        
    with col2:
        chol = st.number_input('Serum Cholesterol', min_value=100, max_value=600, value=200)
        
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar', options=[0, 1], index=0)
        
    with col1:
       restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2], index=0)
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=50, max_value=220, value=150)
        
    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=[0, 1], index=0)
        
    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=1.0)
        
    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0, 1, 2], index=0)
        
    with col3:
        ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', options=[0, 1, 2, 3], index=0)
        
    with col1:
        thal = st.selectbox('Thalassemia Test Results', options=[0, 1, 2, 3], index=0)
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = Combine_Heart.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)






































# creating a function for Prediction

# def heart_prediction(input_data):
    

#     # changing the input_data to numpy array
#     input_data_as_numpy_array = np.asarray(input_data)

#     # reshape the array as we are predicting for one instance
#     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#     prediction = loaded_model.predict(input_data_reshaped)
#     print(prediction)

#     if (prediction[0] == 0):
#       return 'The person is not heart diabetic'
#     else:
#       return 'The person is heart diabetic'
  
    
  
# def main():
    
    
#     # giving a title
#     st.title('Heart diabetes Prediction Web App')
    
#     age = st.number_input('Age', min_value=0, max_value=120, value=30)
#     sex = st.selectbox('Sex', options=[0, 1], index=0)
#     cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3], index=0)
#     trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, value=120)
#     chol = st.number_input('Serum Cholesterol', min_value=100, max_value=600, value=200)
#     fbs = st.selectbox('Fasting Blood Sugar', options=[0, 1], index=0)
#     restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2], index=0)
#     thalach = st.number_input('Maximum Heart Rate Achieved', min_value=50, max_value=220, value=150)
#     exang = st.selectbox('Exercise Induced Angina', options=[0, 1], index=0)
#     oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=1.0)
#     slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0, 1, 2], index=0)
#     ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', options=[0, 1, 2, 3], index=0)
#     thal = st.selectbox('Thalassemia Test Results', options=[0, 1, 2, 3], index=0)
    # age = st.text_input('Age')
    # sex = st.text_input('Sex')
    # cp = st.text_input('Chest Pain Type')
    # trestbps = st.text_input('Resting Blood Pressure')
    # chol = st.text_input('Serum Cholesterol')
    # fbs = st.text_input('Fasting Blood Sugar')
    # restecg = st.text_input('Resting Electrocardiographic Results')
    # thalach = st.text_input('Maximum Heart Rate Achieved')
    # exang = st.text_input('Exercise Induced Angina')
    # oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest')
    # slope = st.text_input('Slope of the Peak Exercise ST Segment')
    # ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy')
    # thal = st.text_input('Thalassemia Test Results')
    
    # age = float(st.text_input('Age'))
    # sex = float(st.text_input('Sex'))
    # cp = float(st.text_input('Chest Pain Type'))
    # trestbps = float(st.text_input('Resting Blood Pressure'))
    # chol = float(st.text_input('Serum Cholesterol'))
    # fbs = float(st.text_input('Fasting Blood Sugar'))
    # restecg = float(st.text_input('Resting Electrocardiographic Results'))
    # thalach = float(st.text_input('Maximum Heart Rate Achieved'))
    # exang = float(st.text_input('Exercise Induced Angina'))
    # oldpeak = float(st.text_input('ST Depression Induced by Exercise Relative to Rest'))
    # slope = float(st.text_input('Slope of the Peak Exercise ST Segment'))
    # ca = float(st.text_input('Number of Major Vessels Colored by Fluoroscopy'))
    # thal = float(st.text_input('Thalassemia Test Results'))
    
    # code for Prediction
    # diagnosis = ''
    
    # creating a button for Prediction
    
    # if st.button('Heart diabetes Test Result'):
    #     diagnosis = heart_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang,oldpeak,slope,ca,thal])
        
        
    # st.success(diagnosis)
    
    
    
    
    
# if __name__ == '__main__':
#     main()