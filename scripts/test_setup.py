# test_setup.py - Run this to check what works
try:
    import pandas as pd
    print('✅ pandas installed')
except ImportError:
    print('❌ pandas failed')

try:
    import numpy as np
    print('✅ numpy installed') 
except ImportError:
    print('❌ numpy failed')

try:
    import sklearn
    print('✅ scikit-learn installed')
except ImportError:
    print('❌ scikit-learn failed')

print('\n🎯 Let''s test loading your data:')
try:
    df = pd.read_csv('data/telco_churn.csv')
    print(f'✅ Data loaded! Shape: {df.shape}')
    print(f'✅ Columns: {list(df.columns)[:5]}...')
except Exception as e:
    print(f'❌ Data loading failed: {e}')
