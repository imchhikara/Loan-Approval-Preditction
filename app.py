import pickle
import streamlit as st

#loading the model
pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "sans serif"

#Our prediction model
def prediction(Gender, Married, Dependents, Education, Self_employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):
    prediction = model.predict([[Gender, Married, Dependents, Education, Self_employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]])
    print(prediction)
    return 

#Hiding Host
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer{visibility: hidden;}
    header{visibility: hidden;}
    </style>
    """
# Header
html_temp = """
        <div style ="background-color:black;padding:13px">
        <h1 style ="color:yellow;text-align:center;">Loan Approval Prediction</h1>
        </div>
        """      
st.markdown(html_temp, unsafe_allow_html = True)

with st.form("entry_form", clear_on_submit=False):
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    Gender = st.selectbox("Please Select your Gender", ("Male", "Female"))
    Married = st.selectbox("Are you married?", ("Yes", "No"))
    Dependents = st.radio("Dependent on Applicant",("0","1","2","2+"), horizontal=True)
    Education = st.selectbox("Are you Graudate?", ("Yes", "No"))
    Self_employed = st.selectbox("Are you Self-Employed?", ("Yes", "No"))
    ApplicantIncome = st.number_input('Income of Applicant')
    CoapplicantIncome = st.number_input('Income of CoApplicant')
    LoanAmount = st.number_input('Loan Amount')
    Loan_Amount_Term = st.select_slider("Tenure of Loan(Years)",("1","3","5","7","10","15","20","25","30", "40"))
    Credit_History =  st.selectbox("Do you have a credit history", ("Yes", "No"))
    Property_Area = st.selectbox("Your property is in which area ?", ("Rural", "Semi-Rural", "Urban"))
    
    "---"
    submitted = st.form_submit_button("Predict")
    if submitted:
        #db.insert_period(variance,skewness,curtosis,entropy)
        result = prediction(Gender, Married, Dependents, Education, Self_employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)
        if result == 0:
            st.success('This is a Fake Currency')
        elif result == 1:
            st.success('This is a Real Currency')
            st.balloons()
            


