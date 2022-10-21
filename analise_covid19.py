import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose 

url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'

df = pd.read_csv(url, parse_dates=['Date_reported']) 
# print(df.shape) 

# #Salvando backup em para .csv
# bkp = ".\BKP\BKP_21_10_2022.csv"
# df.to_csv(bkp)

## Criação de df com apenas Brasil e sem registros zerados

Brasil = df.loc[(df.Country_code == "BR") & (df.Cumulative_cases > 0)] 
    
# print(Brasil.shape) 
# print(Brasil.sample(2))

## Criando grafico de casos confirmados
print("Gerando o grafico")
linha_Acumulado = px.line(Brasil,"Date_reported","Cumulative_cases", title="Acumulado Casos Brasil")
linha_novos_casos = px.line(Brasil,"Date_reported","New_cases", title="Novos Casos Brasil")
linha_Acumulado.show()
linha_novos_casos.show()

## Criando graficos de mortes

# mortes_dia = go.Figure()
# mortes_dia.add_trace(
#     go.Scatter(x=Brasil.Date_reported, y=Brasil.New_deaths, 
#                mode='lines+markers', line={'color':"red"} )
# )
# mortes_dia.show()

#**** Taxa de crecimento

def taxa_crescimento(data, variable, data_inicio=None, data_fim=None):
# definindo a primeira data com valor > 0 e a ultima linha do dataframe
  if data_inicio == None:
      data_inicio = data.Date_reported.loc[data[variable] > 0].min()
  else:
      data_inicio = pd.to_datetime(data_inicio)

  if data_fim == None:
      data_fim = data.Date_reported.iloc[-1]
  else:
      data_fim = pd.to_datetime(data_fim)

  # definindo os valores de presente e passado

  passado = data.loc[data.Date_reported == data_inicio, variable].values[0]
  presente = data.loc[data.Date_reported == data_fim, variable].values[0]    

  # definindo a variavel n

  n = (data_fim - data_inicio).days

  # formula taxa de crescimento

  taxa = (presente/passado)**(1/n)-1

#   print(f'Taxa media de mortes em {data_fim}: {taxa*100}')
  
# Retornando a taxa de crescimento medio no brasil
taxa_crescimento(Brasil,'New_deaths',None,'2020-05-15') 

def taxa_crescimento_dia(data,variable,data_inicio=None):
    if data_inicio == None:
        data_inicio = data.Date_reported.loc[data[variable] > 0].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)

    data_fim = data.Date_reported.max()

    n = (data_fim - data_inicio).days

    taxas = list(map(
        lambda x: (data[variable].iloc[x] - data[variable].iloc[x-1]) / (data[variable].iloc[x-1]),
        range(1, n+1)
    ))
    # print(f'Taxas diarias de mortes {np.array(taxas) * 100}')
    return np.array(taxas) * 100

taxa_crescimento_dia(Brasil, 'Cumulative_deaths')

primeiro_dia = Brasil.Date_reported.loc[Brasil.Cumulative_deaths > 0].min()

## ****grafico da taxa_crescimento_dia

taxa_dia = go.Figure()
taxa_dia.add_trace(
    go.Scatter(x=pd.date_range(primeiro_dia, Brasil.Date_reported.max())[1:], y=taxa_crescimento_dia(Brasil, 'Cumulative_deaths'), 
               mode='lines+markers', line={'color':"red"})
)
taxa_dia.update_layout(title='taxa de crescimento dos óbitos por dia(%)')
taxa_dia.show()

# ******* Predições *******

df_br_2022 = Brasil.loc[Brasil.Date_reported >= '2022-01-01']

obitos_2022 = df_br_2022.Cumulative_deaths

obitos_2022.index = df_br_2022.Date_reported

## Decompondo o obitos_2022

res = seasonal_decompose(obitos_2022)

## Gerando 4 graficos: serie, tendencia, sazionalidade, residual

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1,figsize=(10,8))

ax1.plot(res.observed)
ax2.plot(res.trend)
ax3.plot(res.seasonal)
ax4.plot(obitos_2022.index, res.resid)
ax4.axhline(0, linestyle = 'dashed', c='black')
plt.show()

## ***** modelo arima *******

from pmdarima import auto_arima

modelo = auto_arima(obitos_2022)

# fig = go.Figure(go.Scatter(
#     x=obitos_2022.index, y=obitos_2022, name='Obervados'    
# ))

# fig.add_trace(go.Scatter(
#     x=obitos_2022.index, y=modelo.predict_in_sample(), name = 'Preditos'
# ))

# fig.add_trace(go.Scatter(
#     x=pd.date_range('2022-10-21', '2022-11-21'), y=modelo.predict(31), name= 'Forecast'
# ))

# fig.update_layout(title='Previsão de óbitos por COVID-19 no Brasil para os próximos 30 dias')
# fig.show()






   
  

