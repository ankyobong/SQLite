import seaborn as sns
import matplotlib.pyplot as plt
import pandas
import os

# plt.rc('font', family='NanumBarunGothic')
# plt.rcParams["figure.figsize"] = (20, 20)

sns.set_theme(style=None)

# Load the example dataset for Anscombe's quartet
# df = sns.load_dataset("anscombe")
# df = pandas.read_csv("anscombe.csv")
df = pandas.read_excel("C:\\Users\\argos\\Desktop\\bongsplugin\\plug-in-test\\seaborn\\anscombe.xlsx",sheet_name="Sheet1",engine='openpyxl')


# print(df)
# print(str(type(df)))

# t = 'x="x", y="y", data=df, hue="dataset"
# Show the results of a linear regression within each dataset
# sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
#            col_wrap=2, ci=None, height=4,)
# sns.scatterplot(x="x", y="y", data=df, hue="dataset")
# sns.lineplot(x="x", y="y", data=df, hue="dataset")

# sns.displot(x="x", y="y", data=df, hue="dataset")
# sns.histplot(x="x", y="y", data=df, hue="dataset")
# sns.kdeplot(x="x", y="y", data=df, hue="dataset")
sns.ecdfplot(x="x", y="y", data=df, hue="dataset")
# sns.rugplot(x="x", y="y", data=df, hue="dataset")
# sns.distplot(x="x", y="y", data=df, hue="dataset")

# sns.catplot(x="x", y="y", data=df, hue="dataset")
# sns.stripplot(x="x", y="y", data=df, hue="dataset")
# sns.swarmplot(x="x", y="y", data=df, hue="dataset")
# sns.boxplot(x="x", y="y", data=df, hue="dataset")
# sns.violinplot(x="x", y="y", data=df, hue="dataset")
# sns.boxenplot(x="x", y="y", data=df, hue="dataset")
# sns.pointplot(x="x", y="y", data=df, hue="dataset")
# sns.barplot(x="x", y="y", data=df, hue="dataset")
# sns.countplot(x="x", y="y", data=df, hue="dataset")
#
# sns.lmplot(x="x", y="y", data=df, hue="dataset")
# sns.regplot(x="x", y="y", data=df, hue="dataset")
# sns.residplot(x="x", y="y", data=df, hue="dataset")

# df.to_excel("anscombe.xlsx")
# df.to_csv("anscombe.csv")
plt.savefig('test5.png')


