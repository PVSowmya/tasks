import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

data="sale.xlsx"
df=pd.read_excel(data)
print(df)

#histogram
df.hist()
plt.show()

#plot bar
product = df['Product']
total = df['Total']
#plt.xticks(rotation=70)
plt.bar(product,total)
plt.title('Bar plot')
plt.show()

#  box plot
df.plot.box()
plt.title('Box plot')
plt.show()

#Scatter plot
plt.scatter(df['Product'], df['Quarter2'])
plt.xlabel('Products')
plt.ylabel('Quarter2')
plt.title('Scatter plot')
plt.show()

#Pie chart
product = {}
print(df['Product'])
total = df['Total'].sum()
for i in range(df['Product'].nunique()):
    c = df['Product'].unique()[i]
    c_order = df[df['Product']==c]['Total'].sum()
    product[c] = c_order/total
plt.pie([x*100 for x in product.values()],labels=[x for x in product.keys()],autopct='%0.1f') 
plt.title('Products share %')
plt.show()


