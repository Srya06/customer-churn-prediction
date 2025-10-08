import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import numpy as np

# Set page config
st.set_page_config(page_title='Advanced Churn Dashboard', layout='wide')

st.title('Advanced Customer Churn Prediction Dashboard')
st.write('Predict churn + Business Impact + Customer Segments')

# Load data
df = pd.read_csv('data/telco_churn_cleaned.csv')

# Sidebar - BUSINESS CALCULATOR
st.sidebar.header('Business Impact Calculator')

avg_monthly_revenue = st.sidebar.number_input('Average Monthly Revenue per Customer ($)', 
                                            min_value=0, max_value=500, value=70)
customer_lifetime = st.sidebar.slider('Estimated Customer Lifetime (months)', 
                                    min_value=1, max_value=60, value=24)
retention_cost = st.sidebar.number_input('Cost per Retention Attempt ($)', 
                                       min_value=0, max_value=100, value=20)
success_rate = st.sidebar.slider('Expected Success Rate %', 
                               min_value=0, max_value=100, value=30)

# Simple churn prediction (using your model logic)
high_risk_customers = len(df[(df['MonthlyCharges'] > 70) & (df['tenure'] < 12)])

# Business calculations
potential_revenue_loss = high_risk_customers * avg_monthly_revenue * customer_lifetime
retention_program_cost = high_risk_customers * retention_cost
potential_savings = potential_revenue_loss * (success_rate / 100)
roi = potential_savings - retention_program_cost

# Display business results
st.sidebar.subheader('Financial Impact')
st.sidebar.metric('High-Risk Customers', high_risk_customers)
st.sidebar.metric('Revenue at Risk', f'')
st.sidebar.metric('Program Cost', f'')
st.sidebar.metric('Potential Savings', f'')
st.sidebar.metric('Estimated ROI', f'')

# Main navigation
st.sidebar.header('Navigation')
page = st.sidebar.radio('Go to:', ['Overview', 'Predict Churn', 'Customer Segments', 'Insights'])

if page == 'Overview':
    st.header('Dataset Overview')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric('Total Customers', len(df))
        churn_rate = df['Churn_binary'].mean() * 100
        st.metric('Churn Rate', str(round(churn_rate, 1)) + '%')
    
    with col2:
        avg_tenure = df['tenure'].mean()
        st.metric('Average Tenure', str(round(avg_tenure, 1)) + ' months')
        st.metric('High Risk Customers', high_risk_customers)
    
    with col3:
        avg_charges = df['MonthlyCharges'].mean()
        st.metric('Avg Monthly Charges', '$' + str(round(avg_charges, 2)))
        st.metric('Potential Savings', f'')
    
    st.subheader('Sample Data')
    st.dataframe(df.head(10))

elif page == 'Predict Churn':
    st.header('Predict Customer Churn')
    
    st.write('Enter customer details to predict churn risk:')
    
    col1, col2 = st.columns(2)
    
    with col1:
        tenure = st.slider('Tenure (months)', 0, 72, 12, key='tenure_slider')
        monthly_charges = st.number_input('Monthly Charges ($)', 0, 200, 70, key='charges_input')
    
    with col2:
        total_charges = st.number_input('Total Charges ($)', 0, 10000, 1000, key='total_input')
        contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'], key='contract_select')
    
    # Enhanced risk calculation
    contract_risk = {'Month-to-month': 0.8, 'One year': 0.3, 'Two year': 0.1}
    base_risk = contract_risk[contract]
    
    # Adjust based on factors from your model
    if monthly_charges > 80:
        base_risk += 0.15
    if tenure < 6:
        base_risk += 0.25
    elif tenure < 12:
        base_risk += 0.15
    elif tenure > 36:
        base_risk -= 0.2
    
    risk_score = max(0, min(1, base_risk))
    
    st.subheader('Prediction Result')
    
    if risk_score > 0.7:
        st.error('HIGH RISK of Churn (' + str(round(risk_score * 100, 1)) + '%)')
        st.write('Immediate action required! Offer personalized discount, service review, contract extension')
    elif risk_score > 0.4:
        st.warning('MEDIUM RISK of Churn (' + str(round(risk_score * 100, 1)) + '%)')
        st.write('Proactive outreach: Regular check-ins, loyalty rewards, service optimization')
    else:
        st.success('LOW RISK of Churn (' + str(round(risk_score * 100, 1)) + '%)')
        st.write('Maintain current service quality, occasional satisfaction surveys')

elif page == 'Customer Segments':
    st.header('Customer Segmentation Analysis')
    
    st.write('Identifying different customer groups for targeted marketing:')
    
    # Prepare data for clustering
    cluster_features = df[['tenure', 'MonthlyCharges', 'TotalCharges']].copy()
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    df['Segment'] = kmeans.fit_predict(cluster_features)
    
    # Analyze segments
    segment_analysis = df.groupby('Segment').agg({
        'tenure': 'mean',
        'MonthlyCharges': 'mean', 
        'TotalCharges': 'mean',
        'Churn_binary': 'mean',
        'customerID': 'count'
    }).round(2)
    
    segment_analysis.columns = ['Avg Tenure', 'Avg Monthly $', 'Avg Total $', 'Churn Rate', 'Count']
    
    st.subheader('Customer Segments Identified:')
    st.dataframe(segment_analysis)
    
    # Visualize segments
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(df['tenure'], df['MonthlyCharges'], c=df['Segment'], cmap='viridis', alpha=0.6)
    plt.colorbar(scatter, label='Customer Segment')
    ax.set_xlabel('Tenure (months)')
    ax.set_ylabel('Monthly Charges ($)')
    ax.set_title('Customer Segments: Tenure vs Monthly Charges')
    st.pyplot(fig)
    
    st.subheader('Segment Recommendations:')
    st.write('Segment 0: Low tenure, medium charges -> Focus on onboarding')
    st.write('Segment 1: Medium tenure, high charges -> High value, monitor closely')
    st.write('Segment 2: High tenure, low charges -> Loyal customers, upsell opportunities')
    st.write('Segment 3: Mixed profile -> General retention strategies')

else:  # Insights page
    st.header('Advanced Business Insights')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('Churn by Contract Type')
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        churn_by_contract = pd.crosstab(df['Contract'], df['Churn'])
        churn_by_contract.plot(kind='bar', ax=ax1)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig1)
    
    with col2:
        st.subheader('Monthly Charges Distribution')
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        df['MonthlyCharges'].hist(bins=30, ax=ax2, alpha=0.7)
        ax2.set_xlabel('Monthly Charges ($)')
        ax2.set_ylabel('Number of Customers')
        plt.tight_layout()
        st.pyplot(fig2)
    
    st.subheader('Key Strategic Insights:')
    st.write('Top 3 Retention Strategies:')
    st.write('1. Target high-monthly-charge customers with personalized offers')
    st.write('2. Convert month-to-month to annual contracts with incentives')  
    st.write('3. Focus on customers under 12 months tenure with proactive support')

st.sidebar.markdown('---')
st.sidebar.write('Built with Advanced ML + Business Analytics')
