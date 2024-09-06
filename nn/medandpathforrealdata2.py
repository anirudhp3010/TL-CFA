import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


s1 = "causalprojfiles\medonorgdata2.csv"
s2 = "causalprojfiles\pathonorgdata2.csv"
df = pd.read_csv('ds2.csv')


columns_to_normalize = ['sex', 'age', 'annhrs', 'yrsexp', 'annlabinc', 'region']
# Perform min-max normalization
df[columns_to_normalize] = (df[columns_to_normalize] - df[columns_to_normalize].min()) / (df[columns_to_normalize].max() - df[columns_to_normalize].min())
df['region'] = df['region'].fillna(0)
unq = sorted(df['wave'].unique().tolist())
columns = ['timestep', 'total-effect', 'direct-effect', 'indirect-effect-age',\
           'indirect-effect-annhrs', 'indirect-effect-yrsexp']
ndf = pd.DataFrame(columns=columns)

for i in unq:
    fdf = df[(df['wave'] == i)]
    independent_var = fdf['sex']  # Independent variable
    mediator_var = fdf[['age', 'annhrs', 'yrsexp']]  # Moderator variable
    dependent_var = fdf['annlabinc']  # Dependent variable

    model_mediator = sm.OLS(mediator_var, sm.add_constant(independent_var)).fit()
    model_dependent = sm.OLS(dependent_var, sm.add_constant(pd.concat([independent_var, mediator_var], axis=1))).fit()
    indirect_effect_age = model_mediator.params[0][1] * model_dependent.params['age']
    indirect_effect_annhrs = model_mediator.params[1][1] * model_dependent.params['annhrs']
    indirect_effect_yrsexp = model_mediator.params[2][1] * model_dependent.params['yrsexp']
    # indirect_effect_se = model_mediator.bse[1] * model_dependent.bse[2]
    direct_effect = model_dependent.params['sex']

    # direct_effect_se = model_dependent.bse[1]

    # Obtain the total effect and its standard error
    total_effect = model_dependent.params['sex'] + indirect_effect_age+indirect_effect_yrsexp+indirect_effect_annhrs
    # total_effect_se = (direct_effect_se ** 2 + indirect_effect_se ** 2) ** 0.5

    new_row = pd.DataFrame({'timestep': [i], 'total-effect': [total_effect], 'direct-effect': [direct_effect],\
                           'indirect-effect-age': [indirect_effect_age], 'indirect-effect-annhrs': [indirect_effect_annhrs],\
                           'indirect-effect-yrsexp': [indirect_effect_yrsexp]})
    ndf = pd.concat([ndf, new_row], ignore_index=True)

ndf.to_csv(s1)


fig, ax = plt.subplots()
# ax.plot(nedf['timestep'], nedf['totaleffect'], label='total effect')
ax.plot(ndf['timestep'], ndf['direct-effect'], label='direct effect')
ax.plot(ndf['timestep'], ndf['indirect-effect-age'], label='indirect effect age')
ax.plot(ndf['timestep'], ndf['indirect-effect-annhrs'], label='indirect effect annhrs')
ax.plot(ndf['timestep'], ndf['indirect-effect-yrsexp'], label='indirect effect yrsexp')
ax.set_xlabel('years')
ax.set_ylabel('Relation between life expectancy and gender')
ax.legend()
plt.title("mediation analysis for GenderPayGap dataset")
plt.show()

columns = ['timestep', 'total-effect', 'direct-effect', 'indirect-effect-age',\
           'indirect-effect-annhrs', 'indirect-effect-yrsexp', 'spurious-effect']
pdf = pd.DataFrame(columns=columns)
for i in unq:
    fdf = df[(df['wave'] == i)]
    independent_var = fdf['sex']  # Independent variable
    mediator_var = fdf[['age', 'annhrs', 'yrsexp']]  # Moderator variable
    dependent_var = fdf['annlabinc']  # Dependent variable
    con_var = fdf['region']

    model_mediator = sm.OLS(mediator_var, sm.add_constant(independent_var)).fit()
    model_dependent = sm.OLS(dependent_var, sm.add_constant(pd.concat([independent_var, mediator_var], axis=1))).fit()
    model_spurious = sm.OLS(dependent_var, sm.add_constant(pd.concat([independent_var, mediator_var, con_var], axis=1))).fit()
    indirect_effect_age = model_mediator.params[0][1] * model_dependent.params['age']
    indirect_effect_annhrs = model_mediator.params[1][1] * model_dependent.params['annhrs']
    indirect_effect_yrsexp = model_mediator.params[2][1] * model_dependent.params['yrsexp']
    # indirect_effect_se = model_mediator.bse[1] * model_dependent.bse[2]
    direct_effect = model_dependent.params['sex']
    direct_effect_s = model_spurious.params['sex']
    spurious_effect_s = direct_effect-direct_effect_s
    # direct_effect_se = model_dependent.bse[1]

    # Obtain the total effect and its standard error
    total_effect = model_spurious.params['sex'] + indirect_effect_age+indirect_effect_yrsexp+indirect_effect_annhrs
    # total_effect_se = (direct_effect_se ** 2 + indirect_effect_se ** 2) ** 0.5

    new_row = pd.DataFrame({'timestep': [i], 'total-effect': [total_effect], 'direct-effect': [direct_effect_s],\
                           'indirect-effect-age': [indirect_effect_age], 'indirect-effect-annhrs': [indirect_effect_annhrs],\
                           'indirect-effect-yrsexp': [indirect_effect_yrsexp], 'spurious-effect': [spurious_effect_s]})
    pdf = pd.concat([pdf, new_row], ignore_index=True)

pdf.to_csv(s2)
fig, ax = plt.subplots()
# ax.plot(pedf['timestep'], pedf['totaleffect'], label='total effect')
ax.plot(pdf['timestep'], pdf['direct-effect'], label='direct effect')
ax.plot(pdf['timestep'], pdf['indirect-effect-age'], label='indirect effect age')
ax.plot(pdf['timestep'], pdf['indirect-effect-annhrs'], label='indirect effect annhrs')
ax.plot(pdf['timestep'], pdf['indirect-effect-yrsexp'], label='indirect effect yrsexp')
ax.plot(pdf['timestep'], pdf['spurious-effect'], label='spurious effect')
ax.set_xlabel('years')
ax.set_ylabel('life expectency vs finanincial status')
ax.legend()
plt.title("path analysis for GenderPayGap dataset")
plt.show()
