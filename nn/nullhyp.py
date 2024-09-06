import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats
import numpy as np

df = pd.read_excel('causalprojfiles\orglifeexp.xlsx')


def determine_value(gnd):
    if gnd == 'F':
        return 0
    else:
        return 1


df['bingen'] = df['gnd'].apply(determine_value)
new_column_names = ['gender', 'year', 'count', 'avg sal', 'life exp', 'bingen']
df.columns = new_column_names
columns_to_normalize = ['count', 'avg sal', 'life exp']
# Perform min-max normalization
df[columns_to_normalize] = (df[columns_to_normalize] - df[columns_to_normalize].min()) / (
            df[columns_to_normalize].max() - df[columns_to_normalize].min())


X='bingen'
M='avg sal'
Y='life exp'
C='count'

model = sm.OLS(df[Y], sm.add_constant(df[[X, M, C]])).fit()
model2 = sm.OLS(df[Y], sm.add_constant(df[[X, M]])).fit()
model3 = sm.OLS(df[M], sm.add_constant(df[X])).fit()
# Get the direct, indirect, and total effects
direct_effect = model.params[X]
direct_effect2 = model2.params[X]
direct_effect_se = model2.bse[X]
direct_effect_std = direct_effect_se / np.sqrt(model2.nobs)
spurious_effect = direct_effect2-direct_effect
indirect_effect = model.params[M] * model3.params[X]
total_effect = direct_effect + indirect_effect+spurious_effect

# Assuming you have the sample mean, sample size, and null hypothesis value
sample_mean = direct_effect2 # Replace with your sample mean
sample_size = 2800    # Replace with your sample size
null_hypothesis = 0  # Replace with your null hypothesis value
se = direct_effect_std
# Perform the one-sample t-test
t_stat, p_value = stats.ttest_1samp([sample_mean]*sample_size, null_hypothesis)


