import pandas as pd
import matplotlib.pyplot as plt

cdf = pd.read_csv('stlformula(conf-allzeros)\cfadata.csv')
fig, ax = plt.subplots()

#ax.plot(cdf['x'], cdf['y1'], label='total effect')
ax.plot(cdf['timestep'], cdf['direct-effect'], label='direct effect')
ax.plot(cdf['timestep'], cdf['indirect-effect'], label='indirect effect')
ax.plot(cdf['timestep'], cdf['spurious-effect'],label='spurious effect')
custom_xticks = cdf['timestep']  # Only plot ticks at these positions
plt.xticks(custom_xticks)
ax.set_xlabel('timestep')
ax.set_ylabel('Value')
ax.legend()
plt.title("causal fairness analysis for LifeExpectancy")
plt.show()
