# Projeto_eda_covid
Projeto Digital Innovation One em parceria com o Prof. Dr. Neylson Crepalde

Análise exploratória dos dados do COVID-19 com Python.

Fonte da descrição - https://covid19.who.int/data

## Sumário dos campos:

<table role="table"><thead><tr role="row"><th colSpan="1" role="columnheader">Field name	</th><th colSpan="1" role="columnheader">Type</th><th colSpan="1" role="columnheader">Description</th></tr></thead><tbody role="rowgroup"><tr role="row"><td role="cell">Date_reported</td><td role="cell">Date</td><td role="cell">Date of reporting to WHO</td></tr><tr role="row"><td role="cell">Country_code</td><td role="cell">String</td><td role="cell">ISO Alpha-2 country code</td></tr><tr role="row"><td role="cell">Country</td><td role="cell">String</td><td role="cell">Country, territory, area</td></tr><tr role="row"><td role="cell">WHO_region</td><td role="cell">String</td><td role="cell">WHO regional offices: WHO Member States are grouped into six WHO regions -- Regional Office for Africa (AFRO), Regional Office for the Americas (AMRO), Regional Office for South-East Asia (SEARO), Regional Office for Europe (EURO), Regional Office for the Eastern Mediterranean (EMRO), and Regional Office for the Western Pacific (WPRO).</td></tr><tr role="row"><td role="cell">New_cases</td><td role="cell">Integer</td><td role="cell">New confirmed cases. Calculated by subtracting previous cumulative case count from current cumulative cases count.*</td></tr><tr role="row"><td role="cell">Cumulative_cases</td><td role="cell">Integer</td><td role="cell">Cumulative confirmed cases reported to WHO to date.</td></tr><tr role="row"><td role="cell">New_deaths</td><td role="cell">Integer</td><td role="cell">New confirmed deaths. Calculated by subtracting previous cumulative deaths from current cumulative deaths.*</td></tr><tr role="row"><td role="cell">Cumulative_deaths</td><td role="cell">Integer</td><td role="cell">Cumulative confirmed deaths reported to WHO to date.</td></tr></tbody></table>

## Descrição do projeto

Nesse projeto foi utilizado dados públicos para construção de modelo preditivo e gráficos para apresentação.

Além dos gráficos dos dados apresentados, foi construído as taxas de crescimento médio e de crescimento diário. Métrica para mensurar o comportamento da série.

Calculado através do modelo ARIMA uma predição dos óbitos para os próximos 30 dias.

### Gráficos de decomposição
1º Série de dados;
2º Tendência; 
3º Sazonalidade;
4º Ruido;

<img src = https://github.com/Cesarszabo/Projeto_Python_COVID19/blob/0cab80446eeab92c653bc01f1ce1064cdab51ae1/Graficos/Graficos%20estatisticos.png>

### Modelo Arima

Esse modelo utiliza da média móvel para predizer os dados nos próximos períodos.

#### Base periodo de 2022 - previsão para os proximos 30 dias: 692K *
<img src = https://github.com/Cesarszabo/Projeto_Python_COVID19/blob/0cab80446eeab92c653bc01f1ce1064cdab51ae1/Graficos/Predi%C3%A7%C3%A3o%20COVID%202022.png>

#### Base desde o primeiro caso no Brasil - previsão para os proximos 30 dias: 689K *
<img src = https://github.com/Cesarszabo/Projeto_Python_COVID19/blob/0cab80446eeab92c653bc01f1ce1064cdab51ae1/Graficos/Predi%C3%A7%C3%A3o%20COVID%20inicio.png>

##### *Observados = dados reais, Preditos = aprendizado do modelo, Forecast = previsão 



