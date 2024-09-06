import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
import matplotlib.ticker as ticker
matplotlib.rcParams['text.usetex'] = True
rc('text', usetex=True)
matplotlib.rc('text.latex', preamble=r'\usepackage{amsmath}\usepackage{amssymb}')
matplotlib.rcParams["font.family"] = "Times New Roman"

plt.rcParams['text.usetex']

#####################################################
# ###################
adf = pd.read_csv('stlformula(conf-allzeros)\cfadata.csv')
bdf = pd.read_csv('stlformula(conf-allzeros)\pathdata1.csv')
cdf = pd.read_csv('stlformula(conf-allzeros)\meddata1.csv')

s1 = 'direct-effect'
s2 = 'indirect-effect'
s3 = 'spurious-effect'
s = s2
l1 = 'Tl-CFA'
l2 = 'Path Analysis'
l3 = 'Mediation Analysis'

xa = [ '1981', '1989', '1999']
fig, (ax1,ax2,ax3) = plt.subplots(1, 3, figsize=(9, 3))
t1 = ax1.plot(xa, adf[s1], label=l1)
t2 = ax1.plot(xa, bdf[s1], label=l2)
t3 = ax1.plot(xa, cdf[s1], label=l3)

t4 = ax2.plot(xa, adf[s2], label=l1)
t5 = ax2.plot(xa, bdf[s2], label=l2)
t6 = ax2.plot(xa, cdf[s2], label=l3)

t7 = ax3.plot(xa, adf[s3], label=l1)
t8 = ax3.plot(xa, bdf[s3], label=l2)
t9 = ax3.plot(xa, cdf[s3], label=l3)

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)

line_labels = [l1, l2, l3]
ax3.legend([t1, t2, t3],     # The line objects
           labels=line_labels,   # The labels for each line
           loc="upper left",   # Position of legend
           borderaxespad=0.85,    # Small spacing around legend box
           fontsize=15
           )

ax1.set_xlabel('Years', fontsize=15, fontweight="bold")
ax1.set_ylabel('Values', fontsize=15, fontweight="bold")
ax1.set_title('Direct Effect', fontsize=20, fontweight="bold")

ax2.set_xlabel('Years', fontsize=15, fontweight="bold")
ax2.set_ylabel('', fontsize=15, fontweight="bold")
ax2.set_title('Indirect Effect', fontsize=20, fontweight="bold")

ax3.set_xlabel('Years', fontsize=15, fontweight="bold")
ax3.set_ylabel('', fontsize=15, fontweight="bold")
ax3.set_title('Spurious Effect', fontsize=20, fontweight="bold")

ax1.tick_params(axis='x', labelsize=17, rotation=45)
ax2.tick_params(axis='x', labelsize=17, rotation=45)
ax3.tick_params(axis='x', labelsize=17, rotation=45)

ax1.tick_params(axis='y', labelsize=17, rotation=45)
ax2.tick_params(axis='y', labelsize=17, rotation=45)
ax3.tick_params(axis='y', labelsize=17, rotation=45)

#plt.subplots_adjust(left=0.05, right=0.99, bottom=0.15, top=0.9, hspace=0.3)
#plt.subplots_adjust(left=0.1)

fig.set_size_inches(14, 3)

fig.savefig("case2.pdf",
            #This is simple recomendation for publication plots
            dpi=1000,
            # Plot will be occupy a maximum of available space
            bbox_inches='tight',
            )
matplotlib.pyplot.tight_layout(pad=2)
#pad=2, h_pad=None, w_pad=None, rect=None
plt.show()
