import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
plt.switch_backend('Agg')
matplotlib.rcParams['text.usetex'] = True
rc('text', usetex=True)
matplotlib.rc('text.latex', preamble=r'\usepackage{amsmath}\usepackage{amssymb}')
matplotlib.rcParams["font.family"] = "Times New Roman"

plt.rcParams['text.usetex']
####################################################################################################################
df = pd.read_excel(r'C:\Users\aniru\Downloads\nn\nn\causalprojfiles\orglifeexp.xlsx')

df_avg = df.groupby(['year', 'gnd'])[['hh_inc', 'le_raceadj', 'count']].mean().reset_index()
ts_s1=df_avg[df_avg['gnd'] == 'F']
df_avg2 = df.groupby(['year'])[['hh_inc', 'le_raceadj', 'count']].mean().reset_index()
#print(ts_s1)
#print(df_avg2)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4), sharey=True)
pd.plotting.autocorrelation_plot(ts_s1['count'], ax=axes[0])
pd.plotting.autocorrelation_plot(df_avg2['count'], ax=axes[1])
axes[0].set_xlabel('Lag', fontsize=15, fontweight="bold")
axes[0].set_ylabel('Values', fontsize=15, fontweight="bold")
axes[0].set_title('Female population annual salary', fontsize=20, fontweight="bold")

axes[1].set_xlabel('Lag', fontsize=15, fontweight="bold")
axes[1].set_ylabel('', fontsize=15, fontweight="bold")
axes[1].set_title('Whole population annual salary', fontsize=20, fontweight="bold")

axes[0].tick_params(axis='both', labelsize=15, rotation=0)
axes[1].tick_params(axis='both', labelsize=15, rotation=0)
plt.show()

fig.set_size_inches(9, 4)

fig.savefig("populationcase1.pdf",
            #This is simple recomendation for publication plots
            dpi=1000,
            # Plot will be occupy a maximum of available space
            bbox_inches='tight',
            )
matplotlib.pyplot.tight_layout()
