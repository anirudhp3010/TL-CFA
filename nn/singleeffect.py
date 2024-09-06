import pandas as pd
df = pd.read_csv('finaldf.csv')

columns = ['cont', 'prot', 'medt', 'outt']
adf = pd.DataFrame(0, index=range(11997), columns=columns)

for i in range(0, 3):
    adf.iloc[3999*i: i*3999+3999] = df.loc[:, [columns[0]+str(i), columns[1]+str(i), columns[2]+str(i), columns[3]+str(i)]].values

adf.to_csv('singlebooleancase2.csv', index=False)
