import pandas as pd
import numpy as np

#1)

arr=np.ones((3,4))
list_cols= ["A","B","C","D"]
list_rows= ["i1","i2","i3"]

df1=pd.DataFrame(data=arr,columns=list_cols,index=list_rows)
print(df1)

#2)



arr=np.ones((100,4))
list_rows = []
list_cols= ["p1","p2","p3","p4"]
for i in np.arange(1,101):
    list_rows.append("i"+ str(i))

df2=pd.DataFrame(data=arr, columns=list_cols,index=list_rows)
print(df2)

#3)


for i in np.arange(1,100):
    for j in np.arange(0,4):
        df2.iloc[i,j] = (i+1) ** (j+1)

print(df2)

#4)

print(df2.shape)

#5)
print(df2.head(10))

#6)
print(df2.tail(10))

#7)
print (df2.columns.values)

#8)
print(df2.dtypes)

#9)
print(df2.info())

#10)

print(df2.describe())

#11)

print(df2["p4"])
print(df2.iloc[:,-1])

#12)

print(df2.iloc[:,(0,3)])

#13)
print(df2)
print (df2["p4"].value_counts(bins=10))

#14)

print(df2.apply(lambda x:x.mean(),axis=0))

print(df2.apply(lambda x:x.mean(),axis=1))
