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

########################################################################
adf = pd.read_csv('stlformula(conf-allzeros)\cfadata.csv')
bdf = pd.read_csv('stlformula(conf-allzeros)\meddata1.csv')
cdf = pd.read_csv('stlformula(conf-allzeros)\pathdata1.csv')
s1 = 'direct-effect'
s2 = 'indirect-effect'
s3 = 'spurious-effect'
s = s2
l1 = 'Tl-CFA'
l3 = 'Path Analysis'
l2 = 'Mediation Analysis'

xa = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]
print(xa)
fig, axs = plt.subplots(2, 2, figsize=(9,4))
ax1, ax2, ax3, ax4 = axs.flatten()
t1 = ax1.plot(xa, adf[s1], label=l1)
t2 = ax1.plot(xa, bdf[s1], label=l3)
t3 = ax1.plot(xa, cdf[s1], label=l2)

t4 = ax2.plot(xa, adf[s2], label=l1)
t5 = ax2.plot(xa, bdf[s2], label=l3)
t6 = ax2.plot(xa, cdf[s2], label=l2)

t7 = ax3.plot(xa, adf[s3], label=l1)
t8 = ax3.plot(xa, cdf[s3], label=l3)



custom_xticks = xa  # Only plot ticks at these positions

ax1.set_xticklabels(custom_xticks)
ax2.set_xticklabels(custom_xticks)
ax3.set_xticklabels(custom_xticks)

ax1.xaxis.set_major_locator(ticker.MultipleLocator(base=1))
ax2.xaxis.set_major_locator(ticker.MultipleLocator(base=1))
ax3.xaxis.set_major_locator(ticker.MultipleLocator(base=1))
ax1.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=9))
ax2.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=9))
ax3.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=9))

ax1.yaxis.set_major_locator(ticker.MaxNLocator(integer=False, nbins=9))
ax2.yaxis.set_major_locator(ticker.MaxNLocator(integer=False, nbins=9))
ax3.yaxis.set_major_locator(ticker.MaxNLocator(integer=False, nbins=9))
ax4.axis('off')
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

# for label in ax1.get_xaxis().get_ticklabels()[::2]:
#     label.set_visible(False)
# for label in ax2.get_xaxis().get_ticklabels()[::2]:
#     label.set_visible(False)
# for label in ax3.get_xaxis().get_ticklabels()[::2]:
#     label.set_visible(False)
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)

line_labels = [l1, l3, l2]
ax2.legend([t1, t2, t3],     # The line objects
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
'''
ax1.tick_params(axis='y', labelsize=17, rotation=45)
ax2.tick_params(axis='y', labelsize=17, rotation=45)
ax3.tick_params(axis='y', labelsize=17, rotation=45)
'''
#plt.subplots_adjust(left=0.05, right=0.99, bottom=0.15, top=0.9, hspace=0.3)
#plt.subplots_adjust(left=0.1)

fig.set_size_inches(10, 8)
#plt.subplots_adjust(wspace=0.5)
matplotlib.pyplot.tight_layout()
fig.savefig("case1.pdf",
            #This is simple recomendation for publication plots
            dpi=1000,
            # Plot will be occupy a maximum of available space

            )

#pad=2, h_pad=None, w_pad=None, rect=None
plt.show()
