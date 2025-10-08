import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title='Customer Churn Predictor', layout='wide')

st.title('Customer Churn Prediction Dashboard')
st.write('Predict which customers are likely to leave and take action!')

# Load data
df = pd.read_csv('data/telco_churn_cleaned.csv')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to:', ['Overview', 'Predict Churn', 'Insights'])

if page == 'Overview':
    st.header('Dataset Overview')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric('Total Customers', len(df))
        churn_rate = df['Churn_binary'].mean() * 100
        st.metric('Churn Rate', str(round(churn_rate, 1)) + '%')
    
    with col2:
        avg_tenure = df['tenure'].mean()
        st.metric('Average Tenure', str(round(avg_tenure, 1)) + ' months')
        avg_charges = df['MonthlyCharges'].mean()
        st.metric('Avg Monthly Charges', '$' + str(round(avg_charges, 2)))
    
    # Show sample data
    st.subheader('Sample Data')
    st.dataframe(df.head(8))

elif page == 'Predict Churn':
    st.header('Predict Customer Churn')
    st.write('Enter customer details to predict churn risk:')
    
    col1, col2 = st.columns(2)
    
    with col1:
        tenure = st.slider('Tenure (months)', 0, 72, 12)
        monthly_charges = st.number_input('Monthly Charges ($)', 0, 200, 70)
    
    with col2:
        total_charges = st.number_input('Total Charges ($)', 0, 10000, 1000)
        contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])
    
    # Simple risk calculation
    contract_risk = {'Month-to-month': 0.8, 'One year': 0.3, 'Two year': 0.1}
    base_risk = contract_risk[contract]
    
    # Adjust based on other factors
    if monthly_charges > 80:
        base_risk += 0.15
    if tenure < 12:
        base_risk += 0.2
    elif tenure > 36:
        base_risk -= 0.2
    
    # Ensure risk is between 0 and 1
    risk_score = max(0, min(1, base_risk))
    
    st.subheader('Prediction Result')
    
    if risk_score > 0.6:
        st.error('HIGH RISK of Churn (' + str(round(risk_score * 100, 1)) + '%)')
        st.write('Recommended Actions: Offer discount, improve service, extend contract')
    elif risk_score > 0.3:
        st.warning('MEDIUM RISK of Churn (' + str(round(risk_score * 100, 1)) + '%)')
        st.write('Recommended Actions: Regular check-ins, loyalty rewards')
    else:
        st.success('LOW RISK of Churn (' + str(round(risk_score * 100, 1)) + '%)')
        st.write('Keep up the good work!')

else:  # Insights page
    st.header('Business Insights')
    
    st.subheader('Churn by Contract Type')
    fig, ax = plt.subplots(figsize=(10, 5))
    churn_data = df.groupby(['Contract', 'Churn']).size().unstack()
    churn_data.plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.subheader('Key Findings:')
    st.write('• Month-to-month contracts have highest churn')
    st.write('• Fiber optic customers churn more')
    st.write('• High monthly charges increase churn risk')
    st.write('• Longer tenure reduces churn risk')

st.sidebar.markdown('---')
st.sidebar.write('Built with Streamlit + Machine Learning')
