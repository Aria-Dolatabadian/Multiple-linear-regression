import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv (r'Wheat.csv')
print (df)
sns.set_theme(style="whitegrid")
g = sns.lmplot(
    data=df,
    x="seed_yiled", y="seed_number", hue="Cultivar",
    height=5
)
g.set_axis_labels("Seed yield", "Seed number")
plt.show()
