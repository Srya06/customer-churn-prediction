import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('📈 QUICK INSIGHTS FROM CLEANED DATA')
print('=' * 50)

# Load cleaned data
df = pd.read_csv('data/telco_churn_cleaned.csv')

print('Creating visualizations...')

# 1. Churn by Contract Type
plt.figure(figsize=(10, 6))
churn_by_contract = pd.crosstab(df['Contract'], df['Churn'])
churn_by_contract.plot(kind='bar')
plt.title('Churn by Contract Type')
plt.xlabel('Contract Type')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('churn_by_contract.png')
print('Saved: churn_by_contract.png')

# 2. Churn by Internet Service
plt.figure(figsize=(10, 6))
churn_by_internet = pd.crosstab(df['InternetService'], df['Churn'])
churn_by_internet.plot(kind='bar')
plt.title('Churn by Internet Service Type')
plt.xlabel('Internet Service')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('churn_by_internet.png')
print('Saved: churn_by_internet.png')

print('')
print('✅ Insights generated! Check the PNG files.')
print('')
print('📊 Answer these questions:')
print('- Which contract type has the MOST red bars (Churn=Yes)?')
print('- Which internet service has highest churn rate?')
