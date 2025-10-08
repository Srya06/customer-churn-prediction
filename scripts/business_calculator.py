import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

print(' CREATING BUSINESS IMPACT CALCULATOR...')

# This will be added to your dashboard
business_code = '''
# Add this to your dashboard.py in the sidebar or new page

st.sidebar.header(" Business Impact Calculator")

# Inputs
avg_monthly_revenue = st.sidebar.number_input("Average Monthly Revenue per Customer ($)", 
                                            min_value=0, max_value=500, value=70)
customer_lifetime = st.sidebar.slider("Estimated Customer Lifetime (months)", 
                                    min_value=1, max_value=60, value=24)
retention_cost = st.sidebar.number_input("Cost per Retention Attempt ($)", 
                                       min_value=0, max_value=100, value=20)
success_rate = st.sidebar.slider("Expected Success Rate %", 
                               min_value=0, max_value=100, value=30)

# Calculations
high_risk_customers = len(df[df['Churn_prediction'] == 1])
potential_revenue_loss = high_risk_customers * avg_monthly_revenue * customer_lifetime
retention_program_cost = high_risk_customers * retention_cost
potential_savings = potential_revenue_loss * (success_rate / 100)
roi = potential_savings - retention_program_cost

# Display results
st.sidebar.subheader("Financial Impact")
st.sidebar.metric("High-Risk Customers", high_risk_customers)
st.sidebar.metric("Potential Revenue at Risk", f"")
st.sidebar.metric("Retention Program Cost", f"")
st.sidebar.metric("Potential Savings", f"")
st.sidebar.metric("Estimated ROI", f"", 
                delta=f"{((roi/retention_program_cost)*100 if retention_program_cost > 0 else 0):.0f}%")
'''

print('Business impact calculator code ready!')
print('Copy and paste this into your dashboard.py file')
print('')
print('Code has been prepared for dashboard integration')
