import os
import pickle
import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="Prediction of Disease Outbreaks System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define the base directory where the models are stored
base_dir = "C:/Users/prati/OneDrive/Desktop/edunet/work/"

# Load machine learning models
try:
    diabetes_model = pickle.load(open(os.path.join(base_dir, 'diabetes_model.sav'), 'rb'))
    heart_disease_model = pickle.load(open(os.path.join(base_dir, 'heart_disease_model.sav'), 'rb'))
    parkinson_model = pickle.load(open(os.path.join(base_dir, 'parkinsons_model.sav'), 'rb'))
except FileNotFoundError as e:
    st.error(f"Model file not found: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Prediction of Disease Outbreaks System',
        ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
        menu_icon="hospital-fill",
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Helper function to validate numeric inputs
def validate_inputs(inputs):
    try:
        return [float(x) for x in inputs]
    except ValueError:
        st.error("Please enter valid numeric values for all inputs.")
        return None

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Collecting input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
        skin_thickness = st.text_input('Skin Thickness value')

    with col2:
        glucose = st.text_input('Glucose Level')
        insulin = st.text_input('Insulin Level')

    with col3:
        blood_pressure = st.text_input('Blood Pressure value')
        bmi = st.text_input('BMI value')

    with col1:
        diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function value')

    with col2:
        age = st.text_input('Age')

    # Prediction logic
    if st.button('Diabetes Test Result'):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
        validated_input = validate_inputs(user_input)

        if validated_input:
            diab_prediction = diabetes_model.predict([validated_input])

            if diab_prediction[0] == 1:
                st.success('The person is diabetic')
            else:
                st.success('The person is not diabetic')

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Collecting input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        sex = st.text_input('Sex (1 = male; 0 = female)')
        chol = st.text_input('Serum Cholesterol in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        cp = st.text_input('Chest Pain types')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')

    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # Prediction logic
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        validated_input = validate_inputs(user_input)

        if validated_input:
            heart_prediction = heart_disease_model.predict([validated_input])

            if heart_prediction[0] == 1:
                st.success('The person has heart disease')
            else:
                st.success('The person does not have heart disease')

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Collecting input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        spread1 = st.text_input('Spread1')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        spread2 = st.text_input('Spread2')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        d2 = st.text_input('D2')

    with col4:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
        ppe = st.text_input('PPE')

    with col5:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
        shimmer = st.text_input('Shimmer')

    # Additional inputs
    with col1:
        rap = st.text_input('MDVP:RAP')

    with col2:
        ppq = st.text_input('MDVP:PPQ')

    with col3:
        ddp = st.text_input('Jitter:DDP')

    with col4:
        apq3 = st.text_input('Shimmer:APQ3')

    with col5:
        apq5 = st.text_input('Shimmer:APQ5')

    # Additional shimmer inputs
    with col1:
        dda = st.text_input('Shimmer:DDA')
        nhr = st.text_input('NHR')

    with col2:
        hnr = st.text_input('HNR')
        rpde = st.text_input('RPDE')

    with col3:
        dfa = st.text_input('DFA')
        total_components = st.text_input('Total Components')

    with col4:
        hnr_corr = st.text_input('HNR Correlation')
        entropy = st.text_input('Entropy')

    # Prediction logic
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, apq3, apq5, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe, total_components, hnr_corr, entropy]
        validated_input = validate_inputs(user_input)

        if validated_input:
            parkinsons_prediction = parkinson_model.predict([validated_input])

            if parkinsons_prediction[0] == 1:
                st.success("The person has Parkinson's disease")
            else:
                st.success("The person does not have Parkinson's disease")
