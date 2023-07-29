import pandas as pd
data={
    'Subjects':["Java","Python"],
    'Fees':[1000,2000]
}
df=pd.DataFrame(data)
print(df)

df_fees=df['Fees'].map(lambda x:x*2)
print("After multiplying \n", df_fees)
print("After filtering")
print('map, filter,reduce')
