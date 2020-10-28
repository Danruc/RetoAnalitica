
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import numpy as np; np.random.seed(0)
import seaborn as sns

df = pd.read_csv("covid19_tweets.csv")
newdf = df 
newdf = newdf.drop(['user_name','user_location','user_description','user_created','user_verified','date','text','hashtags','source','is_retweet'], axis=1)

print(df.describe())

#correlacion
print(df.corr(method='pearson'))

sns.pairplot(df)
plt.show()



#boxplot
plt.boxplot(df["user_followers"])
plt.show() 


#histograma
np.random.seed(10**7) 
mu = 121 
sigma = 21
num_bins = 100
   
n, bins, patches = plt.hist(df["user_followers"], num_bins, density = 1, color ='green', alpha = 0.7) 
   
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2)) 
  
plt.plot(bins, y, '--', color ='black') 
  
plt.xlabel('X-Axis') 
plt.ylabel('Y-Axis') 
  
plt.title('matplotlib.pyplot.hist() function Example\n\n', 
          fontweight ="bold") 
  
plt.show() 


#mapa de calor
grid_kws = {"height_ratios": (.9, .05), "hspace": .3} 
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
ax = sns.heatmap(newdf, cmap="YlGnBu", ax=ax, cbar_ax=cbar_ax, cbar_kws={"orientation": "horizontal"})
plt.show()