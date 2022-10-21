# projeto_eda_covid
Projeto Digital Innovation One em parceria com o Prof. Dr. Neylson Crepalde

Análise exploratória dos dados do COVID-19 com Python.

Fonte da descrição - https://covid19.who.int/data

##Sumario dos campos:

Field name	Type	Description
Date_reported	Date	Date of reporting to WHO
Country_code	String	ISO Alpha-2 country code
Country	String	Country, territory, area
WHO_region	String	WHO regional offices: WHO Member States are grouped into six WHO regions -- Regional Office for Africa (AFRO), Regional Office for the Americas (AMRO), Regional Office for South-East Asia (SEARO), Regional Office for Europe (EURO), Regional Office for the Eastern Mediterranean (EMRO), and Regional Office for the Western Pacific (WPRO).
New_cases	Integer	New confirmed cases. Calculated by subtracting previous cumulative case count from current cumulative cases count.*
Cumulative_cases	Integer	Cumulative confirmed cases reported to WHO to date.
New_deaths	Integer	New confirmed deaths. Calculated by subtracting previous cumulative deaths from current cumulative deaths.*
Cumulative_deaths	Integer	Cumulative confirmed deaths reported to WHO to date.

## Descrição do projeto

Nesse projeto foi utilizado dados públicos para construção de modelo preditivo e gráficos para apresentação.

Além dos gráficos dos dados apresentados, foi construído as taxas de crescimento médio e de crescimento diário. Métrica para mensurar o comportamento da série.

Calculado através do modelo ARIMA uma predição dos óbitos para os próximos 30 dias.



