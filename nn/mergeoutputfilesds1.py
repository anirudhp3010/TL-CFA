import pandas as pd

pdf = pd.read_csv(r'outputpro.csv')
cdf = pd.read_csv(r'outputcon.csv')
mdf = pd.read_csv(r'outputmed.csv')
odf = pd.read_csv(r'outputout.csv')

column_names1=[]
column_names2=[]
column_names3=[]
column_names4=[]

for i in range(0,14):
  d='prot'+str(i)
  a='cont'+str(i)
  b='medt'+str(i)
  c='outt'+str(i)
  column_names1.append(a)
  column_names2.append(b)
  column_names3.append(c)
  column_names4.append(d)

cdf.columns = column_names1
mdf.columns = column_names2
odf.columns = column_names3
pdf.columns = column_names4

result = pd.concat([pdf, cdf, mdf, odf], axis=1)

result.to_csv('finalbindata.csv', index=False)
