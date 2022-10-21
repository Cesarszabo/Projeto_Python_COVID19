# projeto_eda_covid
Projeto Digital Innovation One em parceria com o Prof. Dr. Neylson Crepalde

Análise exploratória dos dados do COVID-19 com Python.

Fonte da descrição - https://covid19.who.int/data

## Sumario dos campos:

<table role="table"><thead><tr role="row"><th colSpan="1" role="columnheader">Field name	</th><th colSpan="1" role="columnheader">Type</th><th colSpan="1" role="columnheader">Description</th></tr></thead><tbody role="rowgroup"><tr role="row"><td role="cell">Date_reported</td><td role="cell">Date</td><td role="cell">Date of reporting to WHO</td></tr><tr role="row"><td role="cell">Country_code</td><td role="cell">String</td><td role="cell">ISO Alpha-2 country code</td></tr><tr role="row"><td role="cell">Country</td><td role="cell">String</td><td role="cell">Country, territory, area</td></tr><tr role="row"><td role="cell">WHO_region</td><td role="cell">String</td><td role="cell">WHO regional offices: WHO Member States are grouped into six WHO regions -- Regional Office for Africa (AFRO), Regional Office for the Americas (AMRO), Regional Office for South-East Asia (SEARO), Regional Office for Europe (EURO), Regional Office for the Eastern Mediterranean (EMRO), and Regional Office for the Western Pacific (WPRO).</td></tr><tr role="row"><td role="cell">New_cases</td><td role="cell">Integer</td><td role="cell">New confirmed cases. Calculated by subtracting previous cumulative case count from current cumulative cases count.*</td></tr><tr role="row"><td role="cell">Cumulative_cases</td><td role="cell">Integer</td><td role="cell">Cumulative confirmed cases reported to WHO to date.</td></tr><tr role="row"><td role="cell">New_deaths</td><td role="cell">Integer</td><td role="cell">New confirmed deaths. Calculated by subtracting previous cumulative deaths from current cumulative deaths.*</td></tr><tr role="row"><td role="cell">Cumulative_deaths</td><td role="cell">Integer</td><td role="cell">Cumulative confirmed deaths reported to WHO to date.</td></tr></tbody></table>

## Descrição do projeto

Nesse projeto foi utilizado dados públicos para construção de modelo preditivo e gráficos para apresentação.

Além dos gráficos dos dados apresentados, foi construído as taxas de crescimento médio e de crescimento diário. Métrica para mensurar o comportamento da série.

Calculado através do modelo ARIMA uma predição dos óbitos para os próximos 30 dias.



