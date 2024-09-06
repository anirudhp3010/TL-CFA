import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols


def determine_value(gnd):
    if gnd == 'F':
        return 0
    else:
        return 1


s1 = "causalprojfiles\medonorgdata1.csv"
s2 = "causalprojfiles\pathonorgdata1.csv"
df = pd.read_excel('causalprojfiles\orglifeexp.xlsx')
df['bingen'] = df['gnd'].apply(determine_value)
new_column_names = ['gender', 'year', 'count', 'avg sal', 'life exp', 'bingen']
df.columns = new_column_names

columns_to_normalize = ['count', 'avg sal', 'life exp']
# Perform min-max normalization
df[columns_to_normalize] = (df[columns_to_normalize] - df[columns_to_normalize].min()) / (
            df[columns_to_normalize].max() - df[columns_to_normalize].min())

columns = ['timestep', 'total-effect', 'direct-effect', 'indirect-effect']
ndf = pd.DataFrame(columns=columns)

for i in range(2001, 2009):
    fdf = df[(df['year'] == i)]
    independent_var = fdf['bingen']  # Independent variable
    mediator_var = fdf['avg sal']  # Moderator variable
    dependent_var = fdf['life exp']  # Dependent variable

    model_mediator = sm.OLS(mediator_var, sm.add_constant(independent_var)).fit()
    model_dependent = sm.OLS(dependent_var, sm.add_constant(pd.concat([independent_var, mediator_var], axis=1))).fit()
    indirect_effect = model_mediator.params[1] * model_dependent.params[2]
    indirect_effect_se = model_mediator.bse[1] * model_dependent.bse[2]
    direct_effect = model_dependent.params[1]
    direct_effect_se = model_dependent.bse[1]
    residuals_mediator = model_mediator.resid
    residuals_dependent = model_dependent.resid

    # Obtain the total effect and its standard error
    total_effect = model_dependent.params[1] + (model_mediator.params[1] * model_dependent.params[2])
    total_effect_se = (direct_effect_se ** 2 + indirect_effect_se ** 2) ** 0.5

    new_row = pd.DataFrame({'timestep': [i - 2001], 'total-effect': [total_effect], 'direct-effect': [direct_effect],
                            'indirect-effect': [indirect_effect]})
    ndf = pd.concat([ndf, new_row], ignore_index=True)
ndf.to_csv(s1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# ax.plot(nedf['timestep'], nedf['totaleffect'], label='total effect')
plt.rcParams.update({'font.size': 16})
ax1.plot(ndf['timestep'], ndf['direct-effect'], label='direct effect')
ax1.plot(ndf['timestep'], ndf['indirect-effect'], label='indirect effect')
# ax.plot(nedf['timestep'], nedf['spuriouseffect'], label='spurious effect')
plt.rcParams.update({'font.size': 16})
ax1.set_xlabel('timestep')
ax1.set_ylabel('Value')
ax1.legend()
ax1.set_title("mediation analysis")


columns = ['timestep', 'total-effect', 'direct-effect', 'indirect-effect', 'spurious-effect']
pdf = pd.DataFrame(columns=columns)
for i in range(2001, 2009):
    fdf = df[(df['year'] == i)]
    C = 'count'
    X = 'bingen'  # Independent variable
    M = 'avg sal'  # Moderator variable
    Y = 'life exp'  # Dependent variable

    model = sm.OLS(fdf[Y], sm.add_constant(fdf[[X, M, C]])).fit()
    model2 = sm.OLS(fdf[Y], sm.add_constant(fdf[[X, M]])).fit()
    # Get the direct, indirect, and total effects
    direct_effect = model.params[X]
    direct_effect2 = model2.params[X]
    spurious_effect = direct_effect-direct_effect2
    indirect_effect = model.params[M] * model.params[X]
    total_effect = direct_effect + indirect_effect + spurious_effect
    new_row = pd.DataFrame({'timestep': [i-2001], 'total-effect': [total_effect],\
                            'direct-effect': [direct_effect], 'indirect-effect': [indirect_effect], 'spurious-effect': [spurious_effect]})
    pdf = pd.concat([pdf, new_row], ignore_index=True)
pdf.to_csv(s2)

# ax.plot(pedf['timestep'], pedf['totaleffect'], label='total effect')
ax2.plot(pdf['timestep'], pdf['direct-effect'], label='direct effect')
ax2.plot(pdf['timestep'], pdf['indirect-effect'], label='indirect effect')
ax2.plot(pdf['timestep'], pdf['spurious-effect'], label='spurious effect')
plt.rcParams.update({'font.size': 16})
ax2.set_xlabel('timestep')
ax2.set_ylabel('Value')
ax2.legend()
ax2.set_title("path analysis")
plt.suptitle('Life Expectancy dataset')
plt.tight_layout
plt.show()
