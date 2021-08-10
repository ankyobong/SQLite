
import seaborn as sns
import matplotlib.pyplot as plt
import pandas
import os
import matplotlib.font_manager as fm


# plt.rc('font', family='NanumBarunGothic')
# plt.rcParams["figure.figsize"] = (20, 20)

# sns.set_theme(style=None)
# sns.set_palette("Blues")
# Load the example dataset for Anscombe's quartet
# df = sns.load_dataset("anscombe")
# df = pandas.read_csv("anscombe.csv")
df = pandas.read_excel("C:\\Users\\argos\\Desktop\\bongsplugin\\plug-in-test\\seaborn\\anscombe.xlsx", engine='openpyxl')


# print(df)
# print(str(type(df)))

# t = 'x="x", y="y", data=df, hue="dataset"
# Show the results of a linear regression within each dataset
sns.set_theme(style='dark')
# x = "'Blues', 8, .75"
# sns.set_palette('Blues', None, None)
# s = sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
#                col_wrap=2, ci=None, height=4, )
# s = sns.scatterplot(x="x", y="y", data=df, hue="dataset")
# s.set_title('한국어')
# sns.lineplot(x="x", y="y", data=df, hue="dataset")

# sns.displot(x="x", y="y", data=df, hue="dataset")
# sns.histplot(x="x", y="y", data=df, hue="dataset")
# sns.kdeplot(x="x", y="y", data=df, hue="dataset")
sns.ecdfplot(x="x", y="y", data=df, hue="dataset")
# s = sns.rugplot(x="x", y="y", data=df)     # 이상하게나오는 부분
# sns.distplot(x="x", y="y", data=df, hue="dataset")      # 안나옴

# sns.catplot(x="x", y="y", data=df, hue="dataset")
# sns.stripplot(x="x", y="y", data=df, hue="dataset")
# sns.swarmplot(x="x", y="y", data=df, hue="dataset")
# sns.boxplot(x="x", y="y", data=df, hue="dataset")
# sns.violinplot(x="x", y="y", data=df, hue="dataset")
# sns.boxenplot(x="x", y="y", data=df, hue="dataset")
# sns.pointplot(x="x", y="y", data=df, hue="dataset")
# sns.barplot(x="x", y="y", data=df, hue="dataset")
# sns.countplot(x="x", y="y", data=df, )     # 에러

# sns.lmplot(x="x", y="y", data=df, hue="dataset")
# sns.regplot(x="x", y="y", data=df)
# sns.residplot(x="x", y="y", data=df)
# sns.set_context("paper")
# s.set_xticklabels(None)
# s.set_theme(style='bark')
# s.set_xlabels(None, fontsize=None)
# plt.xlabel("20", fontsize=None)
plt.savefig('test6.png')
# plt.rc('font', family='Malgun Gothic')
# plt.rc('axes', unicode_minus=False)
# plt.title("this is 한국말")
# x = "엑스축"
# plt.ylabel("와이축")
# plt.xlabel("엑스축")
# plt.show()
# df.to_excel("anscombe.xlsx")
# df.to_csv("anscombe.csv")
# plt.savefig('test6.png', encoding="utf-8")


