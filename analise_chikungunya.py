import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configurações de Estilo e Padrão Visual
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']

def carregar_e_limpar_dados(caminho_arquivo):
    """Carrega a base de dados oficial e realiza o pré-processamento estrutural."""
    print("[INFO] Carregando a base de dados...")
    # Detecção automática de separador e motor robusto para arquivos complexos
    df = pd.read_csv(caminho_arquivo, sep=None, engine='python')
    print(f"[INFO] Dataset carregado com sucesso! Dimensões: {df.shape[0]} linhas e {df.shape[1]} colunas.")
    return df

def analise_exploratoria(df):
    """Executa agregações estatísticas e extrai os principais insights do dataset."""
    print("\n" + "="*50)
    print("       RELATÓRIO DE ANÁLISE EXPLORATÓRIA (EDA)")
    print("="*50)
    
    # Top 10 Bairros com maior incidência
    top_bairros = df['NM_BAIRRO'].value_counts().head(10)
    print("\n[INSIGHT ESPACIAL] Top 10 Bairros com Mais Casos:")
    print(top_bairros)
    
    # Distribuição demográfica por sexo
    dist_sexo = df['CS_SEXO'].value_counts(normalize=True) * 100
    print("\n[INSIGHT DEMOGRÁFICO] Distribuição Percentual por Sexo:")
    print(dist_sexo)
    
    print("\n" + "="*50)
    return top_bairros

def gerar_visualizacoes(df):
    """Gera, formata e exporta visualizações de alta qualidade para o portfólio."""
    print("\n[INFO] Gerando visualizações gráficas avançadas...")
    
    # Gráfico 1: Top 10 Bairros (Horizontal Bar Chart)
    plt.figure(figsize=(11, 6))
    top_bairros = df['NM_BAIRRO'].value_counts().head(10).sort_values(ascending=True)
    ax = top_bairros.plot(kind='barh', color='#1f4e79', edgecolor='none')
    plt.title('Top 10 Bairros com Casos Confirmados de Chikungunya\n(Recife, 2025)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Número de Casos Confirmados', fontsize=11, fontweight='semibold')
    plt.ylabel('Bairro', fontsize=11, fontweight='semibold')
    
    # Anotações de rótulos nas barras para clareza executiva
    for p in ax.patches:
        ax.annotate(f"{int(p.get_width())}", 
                    (p.get_width() + 2, p.get_y() + p.get_height()/2.),
                    va='center', ha='left', fontsize=9, fontweight='bold', color='#222222')
                    
    plt.tight_layout()
    plt.savefig('top_bairros_chikungunya.png', dpi=300)
    plt.close()
    
    # Gráfico 2: Dinâmica Temporal por Semana Epidemiológica (Line Chart)
    plt.figure(figsize=(13, 5))
    semana_counts = df['SEM_NOT'].value_counts().sort_index()
    plt.plot(semana_counts.index.astype(str), semana_counts.values, marker='o', color='#d9534f', linewidth=2.2, markersize=5)
    plt.title('Dinâmica Temporal: Casos de Chikungunya por Semana Epidemiológica (Recife, 2025)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Semana Epidemiológica', fontsize=11, fontweight='semibold')
    plt.ylabel('Número de Notificações', fontsize=11, fontweight='semibold')
    plt.xticks(rotation=90, fontsize=8)
    plt.locator_params(axis='x', nbins=15)
    plt.tight_layout()
    plt.savefig('temporal_chikungunya.png', dpi=300)
    plt.close()
    
    print("[INFO] Gráficos exportados com sucesso ('top_bairros_chikungunya.png' e 'temporal_chikungunya.png').")

if __name__ == "__main__":
    # Caminho do dataset local
    arquivo_csv = 'resources_b300a634-1ab7-49fc-8592-4b45227822a8_casos-confirmados-de-chikungunya-em-2025.csv'
    
    # Execução do pipeline de dados
    df_chikungunya = carregar_e_limpar_dados(arquivo_csv)
    analise_exploratoria(df_chikungunya)
    gerar_visualizacoes(df_chikungunya)