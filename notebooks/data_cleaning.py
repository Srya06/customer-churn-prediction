import pandas as pd
import numpy as np

print('🧹 STEP 3: DATA CLEANING & FEATURE ENGINEERING')
print('=' * 60)

# Load data
df = pd.read_csv('data/telco_churn.csv')

print('1. FIXING TOTALCHARGES COLUMN:')
# Convert TotalCharges to numeric, errors will become NaN
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

print('Fixed data types:', df['TotalCharges'].dtype)
missing_count = df['TotalCharges'].isnull().sum()
print('Missing values after conversion:', missing_count)

# Fill missing TotalCharges with 0 (for new customers)
df['TotalCharges'].fillna(0, inplace=True)
print('Filled missing values with 0')

print('')
print('2. ENCODING TARGET VARIABLE:')
# Convert Churn to binary (1=Yes, 0=No)
df['Churn_binary'] = df['Churn'].map({'Yes': 1, 'No': 0})
churn_counts = df['Churn_binary'].value_counts().to_dict()
print('Churn binary distribution:', churn_counts)

print('')
print('3. BASIC FEATURE ENGINEERING:')
# Create new features that might help prediction
df['TenureGroup'] = pd.cut(df['tenure'], bins=[0, 12, 24, 48, 72], 
                          labels=['0-1yr', '1-2yr', '2-4yr', '4+yr'])
df['ChargeToTenureRatio'] = df['MonthlyCharges'] / (df['tenure'] + 1)

print('Created new features: TenureGroup, ChargeToTenureRatio')

print('')
print('4. FINAL DATASET INFO:')
print('Final shape:', df.shape)
print('Data types:')
print(df.dtypes)

print('')
print('5. SAVING CLEANED DATA:')
df.to_csv('data/telco_churn_cleaned.csv', index=False)
print('✅ Cleaned data saved as: data/telco_churn_cleaned.csv')

print('')
print('🎯 READY FOR MACHINE LEARNING!')
