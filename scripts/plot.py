import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 10
rcParams['font.sans-serif'] = ['Console Modern']
rcParams['savefig.format'] = ['pdf']
rcParams['savefig.bbox'] = 'tight'
rcParams['savefig.pad_inches'] = 0

df = pd.read_csv('../results/results.csv').sort_values(by=['Length','Algorithm'])

df_bruteforce = df.loc[df['Algorithm'] == 'bruteforce']
df_horspool = df.loc[df['Algorithm'] == 'horspool']
df_BNDM = df.loc[df['Algorithm'] == 'BNDM']
df_BOM = df.loc[df['Algorithm'] == 'BOM']


df_best = pd.DataFrame(columns=['Algorithm','Pattern','Length','Found','Time'])
for i in range(1,33):
    df_len = df.loc[df['Length'].astype(int) == i]
    df_best = df_best.append(df.loc[df_len['Time'].idxmin(),], ignore_index=True)


# First Plot
fig, ax = plt.subplots()
plt.ylabel('Running Time (s)')
plt.xlabel('Length of Pattern')
plt.plot(df_bruteforce['Length'], df_bruteforce['Time'],label='Bruteforce')
plt.plot(df_horspool['Length'], df_horspool['Time'],label='Horspool')
plt.plot(df_BNDM['Length'], df_BNDM['Time'],label='BNDM')
plt.plot(df_BOM['Length'], df_BOM['Time'],label='BOM')
plt.legend()
fig.tight_layout()
fig.savefig("../plots/time_len.pdf")
#plt.show()
plt.cla()
plt.clf()
plt.close()

# Second Plot
fig, ax = plt.subplots()
plt.ylabel('Best Algorithm')
plt.xlabel('Length of Pattern')
plt.yticks(range(4), ('Bruteforce', 'Horspool', 'BNDM', 'BOM'))
ax.set_ylim([-0.5,3.5])
plt.scatter(df_best['Length'], df_best['Algorithm'])
fig.tight_layout()
fig.savefig("../plots/alg_len.pdf")
#plt.show()
plt.cla()
plt.clf()
plt.close()

# Third Plot
fig, ax = plt.subplots()
plt.ylabel('Number of Patterns Found')
plt.xlabel('Length of Pattern')
plt.plot(df_bruteforce['Length'], df_bruteforce['Found'])
fig.tight_layout()
fig.savefig("../plots/matches_len.pdf")
#plt.show()
plt.cla()
plt.clf()
plt.close()

# Third 2 Plot
fig, ax = plt.subplots()
plt.ylabel('Number of Patterns Found')
plt.xlabel('Length of Pattern')
ax.set_xlim([9.8,18])
ax.set_ylim([0,2000])
plt.plot(df_bruteforce['Length'], df_bruteforce['Found'])
fig.tight_layout()
fig.savefig("../plots/matches_len2.pdf")
#plt.show()
plt.cla()
plt.clf()
plt.close()