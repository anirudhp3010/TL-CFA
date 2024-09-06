import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


#pdf = pd.read_csv('finalbindata.csv')
pdf = pd.read_csv('finaldf.csv')
#s1 = 'stlformula(conf-allzeros)/pathdata2.csv'
#s2 = 'stlformula(conf-allzeros)/meddata2.csv'
columns = ['timestep', 'total-effect', 'direct-effect', 'indirect-effect', 'spurious-effect']
df = pd.DataFrame(columns=columns)
for i in range(0, 3):
    C = 'cont'+str(i)
    M = 'medt'+str(i)
    X = 'prot'+str(i)
    Y = 'outt'+str(i)
    # Fit the path model
    model = sm.OLS(pdf[Y], sm.add_constant(pdf[[X, M, C]])).fit()
    model2 = sm.OLS(pdf[M], sm.add_constant(pdf[[X, C]])).fit()
    #model3 = sm.OLS(pdf[M], sm.add_constant(pdf[X])).fit()
    # Get the direct, indirect, and total effects
    direct_effect = model.params[X]
    pyc = model.params[C]
    pmc = model2.params[C]
    c_c = pdf[C].corr(pdf[X])

    indirect_effect = model.params[M] * model2.params[X]
    spurious_effect = pyc*pmc
    total_effect = direct_effect + indirect_effect +spurious_effect
    new_row = pd.DataFrame({'timestep': [i], 'total-effect': [total_effect], 'direct-effect': [direct_effect], 'indirect-effect': [indirect_effect], 'spurious-effect': [spurious_effect]})
    df = pd.concat([df, new_row], ignore_index=True)
#df.to_csv(s1)
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

