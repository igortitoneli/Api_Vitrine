import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from lazypredict.Supervised import LazyRegressor

# Read the Excel file
tabela = '/home/igor/Documentos/stemis/Api_Vitrine/webscraping/Web Scraping_Setor1_Completo_Lat_Long.xlsx'
df = pd.read_excel(tabela)

df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
df = df.drop(['ID', 'Cidade', 'Bairro'], axis=1)
df['Tipo'] = df['Tipo'].replace({'Ã£': 'ã', 'Ã©': 'é', 'Ã_x0081_': 'Á'}, regex=True)
df = df.drop(df[df['Tipo'].isin(['Salão', 'Terreno', 'Prédio', 'Sobrado', 'Flat', 'Ponto', 'Área', 'Laje'])].index)
df['Tipo'] = df['Tipo'].replace({'Kitnet': 'Studio'}, regex=True)



money_col = df[['Preço', 'Condomínio', 'IPTU']]
for col in money_col:
    df[col] = df[col].astype(str).apply(lambda x: x.replace('.', ''))
    df[col] = df[col].replace({'R\$ ': '', ',': '.'}, regex=True).astype('float64')
int_col = df[['Quartos', 'Banheiros', 'Vagas']]
for col in int_col:
    df[col] = df[col].astype(int)
df = df.reset_index(drop=True)




#Mape

#saber o q cada coeficiente significa r-squared, rmse , adjusted r-squared, etc





# house_df = property_dfs['Casa']
# studio_df = property_dfs['Studio']
# loja_df = property_dfs['Loja']
# sala_df = property_dfs['Sala']
# galpao_df = property_dfs['Galpão']

# print(apartment_df)



# X = df.drop(columns='Preço')
# y = df['Preço']
