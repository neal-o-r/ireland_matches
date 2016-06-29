import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

sns.set_palette('muted')


df = pd.read_csv('ireland.csv', delimiter='\t')

df.index = df[' Against']

fig = plt.figure()

#df.Played.plot(kind='bar')
#f.Won.plot(kind='bar', color='red', legend=True)

df[["Won", "Drew", "Lost"]].plot(kind='bar', legend=True, stacked=True)

plt.title("Ireland's International Results Since 1926")
plt.xlabel('Country')
plt.ylabel('Number of games played')

fig = plt.figure()

(df.GD / df.Played).plot(kind='bar')

plt.title("Average Goal Difference")
plt.xlabel('Country')
plt.ylabel('Average Goal Difference')

plt.show()

df1 = pd.read_csv('matches.csv', parse_dates=['Date'])
df1.index = df1.Date

our_score = lambda x: int(x.split("-")[0])
their_score = lambda x: int(x.split("-")[1])

df1["Us"] = df1.Score.apply(our_score)
df1["Them"] = df1.Score.apply(their_score)

df1[['Us', 'Them']].groupby(10*(df1.index.year//10)).mean().plot()
plt.ylim([0,3])

plt.xlabel('Decade')
plt.ylabel('Average Goals Per Game')
plt.title("Average Goals per Game over the Decades")

plt.show()


