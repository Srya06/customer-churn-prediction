import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print('🔍 STEP 2: DATA EXPLORATION')
print('=' * 50)

# Load the data
df = pd.read_csv('data/telco_churn.csv')

# 1. Basic Info
print('1. BASIC DATASET INFO:')
print(f'   Shape: {df.shape}')
print(f'   Columns: {list(df.columns)}')

# 2. Check Data Types & Missing Values
print('\n2. DATA TYPES & MISSING VALUES:')
print(df.info())

# 3. Check for missing values
print('\n3. MISSING VALUES:')
print(df.isnull().sum())

# 4. Target Variable Analysis
print('\n4. TARGET VARIABLE - CHURN:')
churn_counts = df['Churn'].value_counts()
churn_rate = (churn_counts['Yes'] / len(df) * 100)
print(churn_counts)
print(f'Churn Rate: {churn_rate:.2f}%')

# 5. Key Numerical Features
print('\n5. KEY NUMERICAL FEATURES:')
print(df[['tenure', 'MonthlyCharges', 'TotalCharges']].describe())

# 6. Check TotalCharges (common issue)
print('\n6. CHECKING TOTALCHARGES:')
print('Sample of TotalCharges values:')
print(df['TotalCharges'].head(10))
