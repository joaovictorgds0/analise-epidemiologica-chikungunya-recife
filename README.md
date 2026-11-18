# 📊 Análise Epidemiológica e Espacial: Casos de Chikungunya em Recife (2025)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success.svg)]()

## 📌 Visão Geral do Projeto
Este projeto realiza uma **Análise Exploratória de Dados (EDA)** aprofundada sobre o panorama de notificações e confirmações de febre de Chikungunya na cidade de Recife ao longo do ano de 2025. O objetivo central é transformar dados brutos de vigilância em saúde pública em inteligência acionável, mapeando padrões espaciais e a sazonalidade temporal da doença.

## 🛠️ Stack Tecnológica
* **Linguagem:** Python 3.x
* **Manipulação e Tratamento:** Pandas, NumPy
* **Visualização de Dados:** Matplotlib, Seaborn
* **Ambiente de Desenvolvimento:** VS Code

## 🔍 Principais Descobertas (Insights)
1. **Concentração Regional:** As ocorrências concentram-se fortemente em zonas populosas. Os destaques do *Top 3* são:
   * **Cohab:** 218 casos
   * **Ibura:** 159 casos
   * **Nova Descoberta:** 117 casos
2. **Sazonalidade Temporal:** Acompanhamento contínuo por semanas epidemiológicas, permitindo identificar os períodos críticos de surto ao longo do ano.

## 📁 Estrutura do Repositório
```text
├── analise_chikungunya.py                                                         # Script principal com pipeline de EDA e gráficos
|── README.md                                                                      # Documentação do projeto
├── resources_b300a634-1ab7-49fc-8592-4b45227822a8_casos-confirmados-de-chikungunya-em-2025.csv # Base de dados epidemiológica
├── temporal_chikungunya.png                                                       # Gráfico: Evolução por semana epidemiológica
└── top_bairros_chikungunya.png                                                    # Gráfico: Top 10 bairros com mais casos
