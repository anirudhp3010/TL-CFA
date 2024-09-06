import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


#pdf = pd.read_csv('finalbindata.csv')
pdf = pd.read_csv('finaldf.csv')
#s1 = 'stlformula(conf-allzeros)/pathdata2.csv'
#s2 = 'stlformula(conf-allzeros)/meddata2.csv'
columns = ['pro', 'conf', 'Med', 'out']
df = pd.DataFrame(columns=columns)
for i in range(0, 3):
    C = 'cont'+str(i)
    M = 'medt'+str(i)
    X = 'prot'+str(i)
    Y = 'outt'+str(i)

model = sm.OLS(pdf[Y], sm.add_constant(pdf[[X, M, C]])).fit()
model2 = sm.OLS(pdf[Y], sm.add_constant(pdf[[X, M]])).fit()
model3 = sm.OLS(pdf[M], sm.add_constant(pdf[X])).fit()
# Get the direct, indirect, and total effects
direct_effect = model.params[X]
direct_effect2 = model2.params[X]
spurious_effect = direct_effect-direct_effect2
indirect_effect = model.params[M] * model3.params[X]
total_effect = direct_effect + indirect_effect
new_row = pd.DataFrame({'timestep': [i], 'total-effect': [total_effect], 'direct-effect': [direct_effect], 'indirect-effect': [indirect_effect], 'spurious-effect': [spurious_effect]})
df = pd.concat([df, new_row], ignore_index=True)
df.to_csv(s1)
fig, ax = plt.subplots()
# ax.plot(pedf['timestep'], pedf['totaleffect'], label='total effect')
ax.plot(df['timestep'], df['direct-effect'], label='direct effect')
ax.plot(df['timestep'], df['indirect-effect'], label='indirect effect')
ax.plot(df['timestep'], df['spurious-effect'], label='spurious effect')
ax.set_xlabel('timestep')
ax.set_ylabel('life expectency vs finanincial status')
ax.legend()
plt.title("path analysis for Life expectancy Boolean ")
plt.show()

columns = ['timestep', 'total-effect', 'direct-effect', 'indirect-effect', 'spurious-effect']
ndf = pd.DataFrame(columns=columns)
for i in range(0, 3):
    M = 'medt'+str(i)
    X = 'prot'+str(i)
    Y = 'outt'+str(i)
    independent_var = pdf[X]  # Independent variable
    mediator_var = pdf[M]  # Moderator variable
    dependent_var = pdf[Y]  # Dependent variable

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

    new_row = pd.DataFrame({'timestep': [i], 'total-effect': [total_effect], 'direct-effect': [direct_effect],
                            'indirect-effect': [indirect_effect]})
    ndf = pd.concat([ndf, new_row], ignore_index=True)
ndf.to_csv(s2)
fig, ax = plt.subplots()
# ax.plot(nedf['timestep'], nedf['totaleffect'], label='total effect')
ax.plot(ndf['timestep'], ndf['direct-effect'], label='direct effect')
ax.plot(ndf['timestep'], ndf['indirect-effect'], label='indirect effect')
# ax.plot(nedf['timestep'], nedf['spuriouseffect'], label='spurious effect')
ax.set_xlabel('timestep')
ax.set_ylabel('Value')
ax.legend()
plt.title("mediation analysis for Life Expectancy Boolean")
plt.show()

