# -*- coding: utf-8 -*-
"""CEP-APP

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V_AtNLsuH5DaOjcD7j1QEXDvTl72ItAi
"""

import streamlit as st
import math
from scipy.stats import binom

def obter_codigo_amostra(tamanho_lote, nivel_inspecao):
    tabela = {
        (2, 8): {'S1': 'A', 'S2': 'A', 'S3': 'A', 'S4': 'A', 'I': 'A', 'II': 'A', 'III': 'B'},
        (9, 15): {'S1': 'A', 'S2': 'A', 'S3': 'A', 'S4': 'A', 'I': 'A', 'II': 'B', 'III': 'C'},
        (16, 25): {'S1': 'A', 'S2': 'A', 'S3': 'B', 'S4': 'B', 'I': 'B', 'II': 'C', 'III': 'D'},
        (26, 50): {'S1': 'A', 'S2': 'B', 'S3': 'B', 'S4': 'C', 'I': 'C', 'II': 'D', 'III': 'E'},
        (51, 90): {'S1': 'B', 'S2': 'B', 'S3': 'C', 'S4': 'C', 'I': 'C', 'II': 'E', 'III': 'F'},
        (91, 150): {'S1': 'B', 'S2': 'B', 'S3': 'C', 'S4': 'D', 'I': 'D', 'II': 'F', 'III': 'G'},
        (151, 280): {'S1': 'B', 'S2': 'C', 'S3': 'D', 'S4': 'E', 'I': 'E', 'II': 'G', 'III': 'H'},
        (281, 500): {'S1': 'B', 'S2': 'C', 'S3': 'D', 'S4': 'E', 'I': 'F', 'II': 'H', 'III': 'J'},
        (501, 1200): {'S1': 'C', 'S2': 'C', 'S3': 'E', 'S4': 'F', 'I': 'G', 'II': 'J', 'III': 'K'},
        (1201, 3200): {'S1': 'C', 'S2': 'D', 'S3': 'E', 'S4': 'G', 'I': 'H', 'II': 'K', 'III': 'L'},
        (3201, 10000): {'S1': 'C', 'S2': 'D', 'S3': 'F', 'S4': 'G', 'I': 'J', 'II': 'L', 'III': 'M'},
        (10001, 35000): {'S1': 'C', 'S2': 'D', 'S3': 'F', 'S4': 'H', 'I': 'K', 'II': 'M', 'III': 'N'},
        (35001, 150000): {'S1': 'D', 'S2': 'E', 'S3': 'G', 'S4': 'J', 'I': 'L', 'II': 'N', 'III': 'P'},
        (150001, 500000): {'S1': 'D', 'S2': 'E', 'S3': 'G', 'S4': 'J', 'I': 'M', 'II': 'P', 'III': 'Q'},
        (500001, float('inf')): {'S1': 'D', 'S2': 'E', 'S3': 'H', 'S4': 'K', 'I': 'N', 'II': 'Q', 'III': 'R'}
    }

    for faixa, valores in tabela.items():
        if faixa[0] <= tamanho_lote <= faixa[1]:
            return valores.get(nivel_inspecao, 'Valor inválido para nível de inspeção.')

    return 'Tamanho do lote fora das faixas da tabela.'

def obter_plano_amostragem(codigo_amostra, nqa):
    tabela_amostragem = {
        'A': {0.010: (2, 0, 1), 0.015: (2, 0, 1), 0.025: (2, 0, 1), 0.040: (2, 0, 1), 0.065: (2, 0, 1),
              0.10: (2, 0, 1), 0.15: (2, 0, 1), 0.25: (2, 0, 1), 0.40: (2, 0, 1), 0.65: (2, 0, 1),
              1.0: (2, 0, 1), 1.5: (2, 0, 1), 2.5: (2, 0, 1), 4.0: (2, 0, 1), 6.5: (2, 0, 1), 10: (2, 1, 2),
        15: (2, 1, 2), 25: (2, 1, 2), 40: (2, 2, 3), 65: (2, 3, 4), 100: (2, 5, 6), 150: (2, 7, 8), 250: (2, 10, 11),
        400: (2, 14, 15), 650: (2, 21, 22), 1000: (2, 30, 31)},
        'B': {0.010: (3, 0, 1), 0.015: (3, 0, 1), 0.025: (3, 0, 1), 0.040: (3, 0, 1), 0.065: (3, 0, 1),
              0.10: (3, 0, 1), 0.15: (3, 0, 1), 0.25: (3, 0, 1), 0.40: (3, 0, 1), 0.65: (3, 0, 1),
              1.0: (3, 0, 1), 1.5: (3, 0, 1), 2.5: (3, 0, 1), 4.0: (3, 0, 1), 6.5: (3, 0, 1), 10: (3, 1, 2),
        15: (3, 1, 2), 25: (3, 2, 3), 40: (3, 3, 4), 65: (3, 5, 6), 100: (3, 7, 8), 150: (3, 10, 11), 250: (3, 14, 15),
        400: (3, 21, 22), 650: (3, 30, 31), 1000: (3, 44, 45)},
        'C': {0.010: (5, 0, 1), 0.015: (5, 0, 1), 0.025: (5, 0, 1), 0.040: (5, 0, 1), 0.065: (5, 0, 1),
              0.10: (5, 0, 1), 0.15: (5, 0, 1), 0.25: (5, 0, 1), 0.40: (5, 0, 1), 0.65: (5, 0, 1),
              1.0: (5, 0, 1), 1.5: (5, 0, 1), 2.5: (5, 0, 1), 4.0: (5, 0, 1), 6.5: (5, 1, 2), 10: (5, 1, 2),
        15: (5, 2, 3), 25: (5, 3, 4), 40: (5, 5, 6), 65: (5, 7, 8), 100: (5, 10, 11), 150: (5, 14, 15), 250: (5, 21, 22),
        400: (5, 30, 31), 650: (5, 44, 45), 1000: (5, 44, 45)},
        'D': {0.010: (8, 0, 1), 0.015: (8, 0, 1), 0.025: (8, 0, 1), 0.040: (8, 0, 1), 0.065: (8, 0, 1),
              0.10: (8, 0, 1), 0.15: (8, 0, 1), 0.25: (8, 0, 1), 0.40: (8, 0, 1), 0.65: (8, 0, 1),
              1.0: (8, 0, 1), 1.5: (8, 0, 1), 2.5: (8, 0, 1), 4.0: (8, 1, 2), 6.5: (8, 1, 2), 10: (8, 2, 3),
              15: (8, 3, 4), 25: (8, 5, 6), 40: (8, 7, 8), 65: (8, 10, 11), 100: (8, 14, 15), 150: (8, 21, 22),
              250: (8, 30, 31), 400: (8, 44, 45), 650: (8, 44, 45), 1000: (8, 44, 45)},
        'E': {0.010: (13, 0, 1), 0.015: (13, 0, 1), 0.025: (13, 0, 1), 0.040: (13, 0, 1), 0.065: (13, 0, 1),
              0.10: (13, 0, 1), 0.15: (13, 0, 1), 0.25: (13, 0, 1), 0.40: (13, 0, 1), 0.65: (13, 0, 1),
              1.0: (13, 0, 1), 1.5: (13, 0, 1), 2.5: (13, 1, 2), 4.0: (13, 1, 2), 6.5: (13, 2, 3), 10: (13, 3, 4),
              15: (13, 5, 6), 25: (13, 7, 8), 40: (13, 10, 11), 65: (13, 14, 15), 100: (13, 21, 22), 150: (13, 30, 31),
              250: (13, 44, 45), 400: (13, 44, 45), 650: (13, 44, 45), 1000: (13, 44, 45)},
        'F': {0.010: (20, 0, 1), 0.015: (20, 0, 1), 0.025: (20, 0, 1), 0.040: (20, 0, 1), 0.065: (20, 0, 1),
              0.10: (20, 0, 1), 0.15: (20, 0, 1), 0.25: (20, 0, 1), 0.40: (20, 0, 1), 0.65: (20, 0, 1),
              1.0: (20, 0, 1), 1.5: (20, 1, 2), 2.5: (20, 1, 2), 4.0: (20, 2, 3), 6.5: (20, 3, 4), 10: (20, 5, 6),
              15: (20, 7, 8), 25: (20, 10, 11), 40: (20, 14, 15), 65: (20, 21, 22), 100: (20, 21, 22), 150: (20, 30, 31),
              250: (20, 44, 45), 400: (20, 44, 45), 650: (20, 44, 45), 1000: (20, 44, 45)},
        'G': {0.010: (32, 0, 1), 0.015: (32, 0, 1), 0.025: (32, 0, 1), 0.040: (32, 0, 1), 0.065: (32, 0, 1),
              0.10: (32, 0, 1), 0.15: (32, 0, 1), 0.25: (32, 0, 1), 0.40: (32, 0, 1), 0.65: (32, 0, 1),
              1.0: (32, 1, 2), 1.5: (32, 1, 2), 2.5: (32, 2, 3), 4.0: (32, 3, 4), 6.5: (32, 5, 6), 10: (32, 7, 8),
              15: (32, 10, 11), 25: (32, 14, 15), 40: (32, 21, 22), 65: (32, 21, 22), 100: (32, 21, 22), 150: (32, 30, 31),
              250: (32, 44, 45), 400: (32, 44, 45), 650: (32, 44, 45), 1000: (32, 44, 45)},
        'H': {0.010: (50, 0, 1), 0.015: (50, 0, 1), 0.025: (50, 0, 1), 0.040: (50, 0, 1), 0.065: (50, 0, 1),
              0.10: (50, 0, 1), 0.15: (50, 0, 1), 0.25: (50, 0, 1), 0.40: (50, 0, 1), 0.65: (50, 1, 2),
              1.0: (50, 1, 2), 1.5: (50, 2, 3), 2.5: (50, 3, 4), 4.0: (50, 5, 6), 6.5: (50, 7, 8), 10: (50, 10, 11),
              15: (50, 14, 15), 25: (50, 21, 22), 40: (50, 21, 22), 65: (50, 21, 22), 100: (50, 21, 22), 150: (50, 30, 31),
              250: (50, 44, 45), 400: (50, 44, 45), 650: (50, 44, 45), 1000: (50, 44, 45)},
        'J': {0.010: (80, 0, 1), 0.015: (80, 0, 1), 0.025: (80, 0, 1), 0.040: (80, 0, 1), 0.065: (80, 0, 1),
              0.10: (80, 0, 1), 0.15: (80, 0, 1), 0.25: (80, 0, 1), 0.40: (80, 1, 2), 0.65: (80, 1, 2),
              1.0: (80, 2, 3), 1.5: (80, 3, 4), 2.5: (80, 5, 6), 4.0: (80, 7, 8), 6.5: (80, 10, 11), 10: (80, 14, 15),
              15: (80, 21, 22), 25: (80, 21, 22), 40: (80, 21, 22), 65: (80, 21, 22), 100: (80, 21, 22), 150: (80, 30, 31),
              250: (80, 44, 45), 400: (80, 44, 45), 650: (80, 44, 45), 1000: (80, 44, 45)},
        'K': {0.010: (125, 0, 1), 0.015: (125, 0, 1), 0.025: (125, 0, 1), 0.040: (125, 0, 1), 0.065: (125, 0, 1),
              0.10: (125, 0, 1), 0.15: (125, 0, 1), 0.25: (125, 1, 2), 0.40: (125, 1, 2), 0.65: (125, 2, 3),
              1.0: (125, 3, 4), 1.5: (125, 5, 6), 2.5: (125, 7, 8), 4.0: (125, 10, 11), 6.5: (125, 14, 15), 10: (125, 21, 22),
              15: (125, 21, 22), 25: (125, 21, 22), 40: (125, 21, 22), 65: (125, 21, 22), 100: (125, 21, 22), 150: (125, 30, 31),
              250: (125, 44, 45), 400: (125, 44, 45), 650: (125, 44, 45), 1000: (125, 44, 45)},
        'L': {0.010: (200, 0, 1), 0.015: (200, 0, 1), 0.025: (200, 0, 1), 0.040: (200, 0, 1), 0.065: (200, 0, 1),
              0.10: (200, 0, 1), 0.15: (200, 1, 2), 0.25: (200, 1, 2), 0.40: (200, 2, 3), 0.65: (200, 3, 4),
              1.0: (200, 5, 6), 1.5: (200, 7, 8), 2.5: (200, 10, 11), 4.0: (200, 14, 15), 6.5: (200, 21, 22), 10: (200, 21, 22),
              15: (200, 21, 22), 25: (200, 21, 22), 40: (200, 21, 22), 65: (200, 21, 22), 100: (200, 21, 22), 150: (200, 30, 31),
              250: (200, 44, 45), 400: (200, 44, 45), 650: (200, 44, 45), 1000: (200, 44, 45)},
        'M': {0.010: (315, 0, 1), 0.015: (315, 0, 1), 0.025: (315, 0, 1), 0.040: (315, 0, 1), 0.065: (315, 0, 1),
              0.10: (315, 1, 2), 0.15: (315, 1, 2), 0.25: (315, 2, 3), 0.40: (315, 3, 4), 0.65: (315, 5, 6),
              1.0: (315, 7, 8), 1.5: (315, 10, 11), 2.5: (315, 14, 15), 4.0: (315, 21, 22), 6.5: (315, 21, 22), 10: (315, 21, 22),
              15: (315, 21, 22), 25: (315, 21, 22), 40: (315, 21, 22), 65: (315, 21, 22), 100: (315, 21, 22), 150: (315, 30, 31),
              250: (315, 44, 45), 400: (315, 44, 45), 650: (315, 44, 45), 1000: (315, 44, 45)},
        'N': {0.010: (500, 0, 1), 0.015: (500, 0, 1), 0.025: (500, 0, 1), 0.040: (500, 0, 1), 0.065: (500, 1, 2),
              0.10: (500, 1, 2), 0.15: (500, 2, 3), 0.25: (500, 3, 4), 0.40: (500, 5, 6), 0.65: (500, 7, 8),
              1.0: (500, 10, 11), 1.5: (500, 14, 15), 2.5: (500, 21, 22), 4.0: (500, 21, 22), 6.5: (500, 21, 22), 10: (500, 21, 22),
              15: (500, 21, 22), 25: (500, 21, 22), 40: (500, 21, 22), 65: (500, 21, 22), 100: (500, 21, 22), 150: (500, 30, 31),
              250: (500, 44, 45), 400: (500, 44, 45), 650: (500, 44, 45), 1000: (500, 44, 45)},
        'P': {0.010: (800, 0, 1), 0.015: (800, 0, 1), 0.025: (800, 0, 1), 0.040: (800, 1, 2), 0.065: (800, 1, 2),
              0.10: (800, 2, 3), 0.15: (800, 3, 4), 0.25: (800, 5, 6), 0.40: (800, 7, 8), 0.65: (800, 10, 11),
              1.0: (800, 14, 15), 1.5: (800, 21, 22), 2.5: (800, 21, 22), 4.0: (800, 21, 22), 6.5: (800, 21, 22), 10: (800, 21, 22),
              15: (800, 21, 22), 25: (800, 21, 22), 40: (800, 21, 22), 65: (800, 21, 22), 100: (800, 21, 22), 150: (800, 30, 31),
              250: (800, 44, 45), 400: (800, 44, 45), 650: (800, 44, 45), 1000: (800, 44, 45)},
        'Q': {0.010: (1250, 0, 1), 0.015: (1250, 0, 1), 0.025: (1250, 1, 2), 0.040: (1250, 1, 2), 0.065: (1250, 2, 3),
              0.10: (1250, 3, 4), 0.15: (1250, 5, 6), 0.25: (1250, 7, 8), 0.40: (1250, 10, 11), 0.65: (1250, 14, 15),
              1.0: (1250, 21, 22), 1.5: (1250, 21, 22), 2.5: (1250, 21, 22), 4.0: (1250, 21, 22), 6.5: (1250, 21, 22), 10: (1250, 21, 22),
              15: (1250, 21, 22), 25: (1250, 21, 22), 40: (1250, 21, 22), 65: (1250, 21, 22), 100: (1250, 21, 22), 150: (1250, 30, 31),
              250: (1250, 44, 45), 400: (1250, 44, 45), 650: (1250, 44, 45), 1000: (1250, 44, 45)},
        'R': {0.010: (2000, 0, 1), 0.015: (2000, 0, 1), 0.025: (2000, 1, 2), 0.040: (2000, 2, 3), 0.065: (2000, 3, 4),
              0.10: (2000, 5, 6), 0.15: (2000, 7, 8), 0.25: (2000, 10, 11), 0.40: (2000, 14, 15), 0.65: (2000, 21, 22),
              1.0: (2000, 21, 22), 1.5: (2000, 21, 22), 2.5: (2000, 21, 22), 4.0: (2000, 21, 22), 6.5: (2000, 21, 22), 10: (2000, 21, 22),
              15: (2000, 21, 22), 25: (2000, 21, 22), 40: (2000, 21, 22), 65: (2000, 21, 22), 100: (2000, 21, 22), 150: (2000, 30, 31),
              250: (2000, 44, 45), 400: (2000, 44, 45), 650: (2000, 44, 45), 1000: (2000, 44, 45)}
    }

    if codigo_amostra not in tabela_amostragem:
        return 'Código de amostra inválido'

    nqa_validos = sorted(tabela_amostragem[codigo_amostra].keys())
    nqa_proximo = min(nqa_validos, key=lambda x: abs(x - nqa))

    tamanho_amostra, ac, re = tabela_amostragem[codigo_amostra][nqa_proximo]
    return tamanho_amostra, ac, re

def calcular_probabilidade_aceitacao(ac, tamanho_amostra, taxa_defeituosos):
    return binom.cdf(ac, tamanho_amostra, taxa_defeituosos)

st.title("Aplicativo de Amostragem")

tamanho_lote = st.number_input("Tamanho do lote", min_value=1, step=1)
nivel_inspecao = st.selectbox("Nível de inspeção", ["S1", "S2", "S3", "S4", "I", "II", "III"])
nqa = st.number_input("NQA (Nível de Qualidade Aceitável)", min_value=0.01, max_value=1000.0, step=0.01, format="%.2f")
custo_unitario_inspecao = st.number_input("Custo unitário de Inspeção", min_value=0.01, step=0.01, format="%.2f")
despesa_lote_reprovado = st.number_input("Despesa por lote reprovado", min_value=0.0, step=0.01, format="%.2f")
taxa_defeituosos = st.number_input("Taxa de defeituosos do fornecedor", min_value=0.0, max_value=1.0, step=0.001, format="%.3f")
dias_uteis_mes = st.number_input("Dias úteis no mês", min_value=1, max_value=31, step=1)

if st.button("Calcular"):
    codigo_amostra = obter_codigo_amostra(tamanho_lote, nivel_inspecao)
    st.write(f"Código da amostra: {codigo_amostra}")

    if isinstance(codigo_amostra, str) and codigo_amostra.startswith('Valor inválido'):
        st.error(codigo_amostra)
    else:
        resultado = obter_plano_amostragem(codigo_amostra, nqa)

        if isinstance(resultado, str):
            st.error(resultado)
        else:
            tamanho_amostra, ac, re = resultado
            prob_aceitacao = calcular_probabilidade_aceitacao(ac, tamanho_amostra, taxa_defeituosos)
            prob_rejeicao = 1 - prob_aceitacao
            inspecao_total_media = tamanho_amostra + (prob_rejeicao * (tamanho_lote - tamanho_amostra))
            custo_inspecao_sem_despesas = inspecao_total_media * dias_uteis_mes * custo_unitario_inspecao
            custo_inspecao_com_despesas = custo_inspecao_sem_despesas + (dias_uteis_mes * taxa_defeituosos * despesa_lote_reprovado)

            st.write(f"Tamanho da amostra: {tamanho_amostra}")
            st.write(f"Número de aceitação (Ac): {ac}")
            st.write(f"Número de rejeição (Re): {re}")
            st.write(f"Probabilidade de Aceitação do Lote: {prob_aceitacao:.1%}")
            st.write(f"Probabilidade de Rejeição do Lote: {prob_rejeicao:.1%}")
            st.write(f"Valor de Inspeção Total Média: {inspecao_total_media:.2f}")
            st.write(f"Custo de Inspeção Mensal sem Despesas: {custo_inspecao_sem_despesas:.2f}")
            st.write(f"Custo de Inspeção Mensal com Despesas: {custo_inspecao_com_despesas:.2f}")