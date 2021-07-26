import seaborn as sns
import matplotlib.pyplot as plt
import pandas
import os

# plt.rc('font', family='NanumBarunGothic')
# plt.rcParams["figure.figsize"] = (20, 20)

sns.set_theme(style=None)

# Load the example dataset for Anscombe's quartet
# df = sns.load_dataset("anscombe")
df = pandas.read_csv("anscombe.csv")
# df = pandas.read_excel("anscombe.xlsx")

print(df)
print(str(type(df)))


# Show the results of a linear regression within each dataset
# sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
#            col_wrap=2, ci=None, height=4,)
# sns.scatterplot(x="x", y="y", data=df, hue="dataset")
# sns.lineplot(x="x", y="y", data=df, hue="dataset")
sns.displot(x="x", y="y", data=df, hue="dataset")
# df.to_excel("anscombe.xlsx")
# df.to_csv("anscombe.csv")
plt.savefig('test2.png')


