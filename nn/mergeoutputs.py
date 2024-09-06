import pandas as pd

pdf = pd.read_csv(r'outputpro1.csv')
cdf = pd.read_csv(r'outputcon1.csv')
mdf = pd.read_csv(r'outputmed1.csv')
odf = pd.read_csv(r'outputout1.csv')

column_names1 = ['prot0', 'prot1', 'prot2', 'prot3', 'prot4', 'prot5']
column_names2 = ['cont0', 'cont1', 'cont2', 'cont3', 'cont4', 'cont5']
column_names3 = ['medt0', 'medt1', 'medt2', 'medt3', 'medt4', 'medt5']
column_names4 = ['outt0', 'outt1', 'outt2', 'outt3', 'outt4', 'outt5']

# Assign column names to the DataFrame

pdf.columns = column_names1
cdf.columns = column_names2
mdf.columns = column_names3
odf.columns = column_names4

result = pd.concat([pdf, cdf, mdf, odf], axis=1)
result.to_csv('finaldf.csv',index=False)
