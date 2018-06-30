#Q1
import pandas as pd
d={'Name':['Lovi','Vine','Arhu'],'Age':[20,21,18],'Mail.id':['lovi1997@gmail.com','vine24@gmail.com','arhu17@gmail.com'],'Phone no.':[1234567890,9087654321,1243658709]}
df=pd.DataFrame(d)
print(df)

#Q2
import pandas as pd
data=pd.read_csv("dataset.csv")
df=pd.DataFrame(data)
print(df)
print(df.head(5))
print(df.head(10))
print(df.shape)
print(df.T)
print(df.tail(5))
print(df['Location'].sum())
print(df['Location'].describe())


