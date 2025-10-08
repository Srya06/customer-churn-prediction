print('Testing dashboard components...')

try:
    import streamlit as st
    print('✅ streamlit works')
except:
    print('❌ streamlit failed')

try:
    import pandas as pd
    df = pd.read_csv('data/telco_churn_cleaned.csv')
    print('✅ pandas and data loading works')
    print('Data shape:', df.shape)
except Exception as e:
    print('❌ data loading failed:', e)

try:
    import matplotlib.pyplot as plt
    print('✅ matplotlib works')
except:
    print('❌ matplotlib failed')

print('If all checks pass, run: streamlit run dashboard.py')
