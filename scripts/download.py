import pandas as pd
import os

print('📥 Downloading dataset...')
url = 'https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv'

try:
    df = pd.read_csv(url)
    # Make sure data folder exists
    os.makedirs('data', exist_ok=True)
    # Save the file
    df.to_csv('data/telco_churn.csv', index=False)
    print('✅ Dataset downloaded successfully!')
    print(f'📊 Data shape: {df.shape}')
    print(f'📁 File saved: data/telco_churn.csv')
    print(f'🎯 Churn distribution:')
    print(df['Churn'].value_counts())
except Exception as e:
    print(f'❌ Download failed: {e}')
