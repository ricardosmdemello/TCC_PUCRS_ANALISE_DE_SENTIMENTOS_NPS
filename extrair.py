# -*- coding: utf-8 -*-
"""Extrair.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_1tpaJZOHUHrVASb0tRJJRMnjK-AAcLk

## Dados - Origem arquivos HTML's

---
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""## Dados - Seta se vai usar caminho Local/Ou Não"""

# True  => LOCAL Desktop
# False => colab
isPathLocal = False

from google.colab import drive
drive.mount('/content/drive')

if isPathLocal:
    path = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\NPS - Suporte\\NPS - Suporte - HTML\\01 - TELEFONE - JANEIRO.html'
else:
    path = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/NPS - Suporte/NPS - Suporte - HTML/01 - TELEFONE - JANEIRO.html'

path

df = pd.read_html(path)

type(df)

df[0]

if isPathLocal:
    path_root = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\NPS - Suporte\\NPS - Suporte - HTML\\'
else:
    path_root = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/NPS - Suporte/NPS - Suporte - HTML/'

# Obtem os arquivos na pasta
if isPathLocal:
    files = os.listdir('D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\NPS - Suporte\\NPS - Suporte - HTML\\')
else:
    files = os.listdir("./drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/NPS - Suporte/NPS - Suporte - HTML/")

# https://www.kite.com/python/answers/how-to-save-a-pandas-dataframe-in-python

list_dfs = []

for file in files:
  path_full = path_root + file
  df = pd.DataFrame(pd.read_html(path_full)[0])
  month = file.split(' - ')[2].replace('.html', '')
  # print(month)
  # print(type(df))
  #print(df.shape)

  df['Mês'] = pd.Series([month for x in range(df.shape[0])])

  #print(df.shape)
  #print(df[0:-1])

  # DROPA a primeira linha, que contem => Requisição	Nota	Observação Responsável
  df.drop(df.index[[0]], inplace=True)

  list_dfs.append(df)

  #break

# Junta todos os dataframes
df_full = pd.concat(list_dfs)

df_full.shape

# Renomear as colunas
df_full.columns = ['Requisição', 'Nota', 'Comentário', 'Responsável', 'Mês']

df_full

df_full['Comentário']

# Total de Observções validas
df_full[df_full['Comentário'].notnull()].shape

"""## Dados - Origem arquivos EXCEL/xlsx'"""

import pandas as pd

if isPathLocal:
    path_excel = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\Excel\\Financeiro NPS.xlsx'
else:
    path_excel = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/Excel/Financeiro NPS.xlsx'

sheet_page = 0
df_excel = pd.read_excel(path_excel, sheet_name=sheet_page)

df_excel

sheet_page = 32
df_excel = pd.read_excel(path_excel, sheet_name=sheet_page)
df_excel

df_excel['Comentário']

df_excel.columns.shape

# Se contém SO as 3 colunas ['Protocolo', 'Nota', 'Comentário']
if df_excel.columns.shape[0] == 3 and set(['Protocolo', 'Nota', 'Comentário']).issubset(df_excel.columns):
  print('Exits columns')

# Se contém SO as 3 colunas e mais outras ['Protocolo', 'Nota', 'Comentário']
if df_excel.columns.shape[0] > 3 and set(['Protocolo', 'Nota', 'Comentário']).issubset(df_excel.columns):
  print('Exits columns', df_excel.columns.shape[0])

isExcept = False
sheet_page = 0

while True:
  print('sheet_page:', sheet_page)
  
  try:

    ################################################################################################

    df_excel = pd.read_excel(path_excel, sheet_name=sheet_page)


    ################################################################################################
  except: 
    isExcept = True
    print('Acabou as sheets!')

  sheet_page = sheet_page + 1

  if isExcept:
    print('isExcept', isExcept)
    break

list_dic_nps = [] # Lista de Dictionary

# calories = {'apple' : 52, 'banana' : 89, 'choco' : 546}
list_dic_nps.append(
    {'Requisição': '324234234', 'Nota': 10, 'Comentário': 'Teste', 'Responsável': 'Ricardo'}
)
list_dic_nps

if isPathLocal:
    path_excel = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\Excel\\Financeiro NPS.xlsx'
else:
    path_excel = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/Excel/Financeiro NPS.xlsx'

sheet_page = 0
df_excel = pd.read_excel(path_excel, sheet_name=sheet_page)
df_excel.head()

from numpy.core.numeric import NaN
# Montar Dataframe nesse padrão!
# ['Requisição', 'Nota', 'Comentário', 'Responsável', 'Mês']

path_excel = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/Excel/Financeiro NPS.xlsx'

# sheet_page = 0
# df_excel = pd.read_excel(path_excel, sheet_name=sheet_page)


isExcept = False
sheet_page = 0

full_list_nps = []

while True:
  #print('sheet_page:', sheet_page)
  
  try:

    ################################################################################################

    df_excel = pd.read_excel(path_excel, sheet_name=sheet_page)

    i = 0
    index_old = 0

    isPrint = False

    isFirst = False

    isProtocolo = False
    isNota = False
    isComentario = False

    isProtocolo_index = False
    isNota_index = False
    isComentario_index = False

    index_cell_Protocolo = 0
    index_cell_Nota = 0
    index_cell_Comentario = 0

    isOperador = False
    operador_str = ''

    list_dic_nps = [] # Lista de Dictionary


    for index, row in df_excel.iterrows():

      dic_nps = {'Requisição': NaN, 'Nota': NaN, 'Comentário': NaN, 'Responsável': NaN}

      ### 1 - Se contém SÓ as colunas (['Protocolo', 'Nota', 'Comentário'])
      if df_excel.columns.shape[0] == 3 and set(['Protocolo', 'Nota', 'Comentário']).issubset(df_excel.columns):
        if isPrint:
          print(index, row['Protocolo'], row['Nota'], row['Comentário'])

        dic_nps['Requisição'] = row['Protocolo']
        dic_nps['Comentário'] =  row['Comentário']
        dic_nps['Nota'] = row['Nota']
        dic_nps['Responsável'] = operador_str

        list_dic_nps.append(dic_nps)

      ### 2 - Se contém SO as 3 colunas e mais outras ['Protocolo', 'Nota', 'Comentário']
      elif df_excel.columns.shape[0] > 3 and set(['Protocolo', 'Nota', 'Comentário']).issubset(df_excel.columns) and isOperador == False:
        if isPrint:
          print(index, row['Protocolo'], row['Nota'], row['Comentário'])

        if type(row['Protocolo']) == str:
          if 'Operador:' in row['Protocolo']:

            isOperador = True
            operador_str = row['Protocolo'].replace('Operador: ', '')

            if isPrint:
              print('Operador:', operador_str)
        
        if isOperador == False:
          dic_nps['Requisição'] = row['Protocolo']
          dic_nps['Comentário'] =  row['Comentário']
          dic_nps['Nota'] = row['Nota']
          dic_nps['Responsável'] = operador_str

          list_dic_nps.append(dic_nps)

      ### 3 - sem colunas definidas
      else:

        # print(index, row.shape)
        # print(index, row)

        # Mostra as linhas
        #print('Linha - index:', index, 'index_old:', index_old)

        index_cell = 0

        ### INICIO = for cell ###
        for cell in row:

          index_cell = index_cell + 1
          
          # Acha a linha que contém o 'Operador: ')
          if type(cell) == str:
            #print('teste 1')

            if 'Operador: ' in cell:

              operador_str = cell.replace('Operador: ', '')

              if isPrint:
                print('Operador:', operador_str)

              #print(dic_nps)

              # Zera as variaveis, por que e um novo operado!
              #isIndexPrint = False
              isProtocolo = False
              isNota = False
              isComentario = False

              isProtocolo_index = False
              isNota_index = False
              isComentario_index = False

              index_cell_Protocolo = 0
              index_cell_Nota = 0
              index_cell_Comentario = 0

            # Acha a linha que contém os ('Protocolo', 'Nota', 'Comentário')
            ### Obtem os indeces das colunas Protocolo, Nota, Comentário
            if isProtocolo == False or isNota == False or isComentario == False:

              # print(cell)
              if 'Protocolo' in cell and isProtocolo == False:
                isProtocolo = True
                index_cell_Protocolo = index_cell
                #print(cell)

              if 'Nota' in cell and isNota == False:
                isNota = True
                index_cell_Nota = index_cell
                #print(cell)
              
              if 'Comentário' in cell and isComentario == False:
                isComentario = True
                index_cell_Comentario = index_cell
                #print(cell)

            if isProtocolo and isNota and isComentario:
              if isPrint:
                print('FLAGS = index:', index, isProtocolo, isNota, isComentario, 'index', index, '>', index_old, 'index_old')

          # Se achou a linha que cotém os ('Protocolo', 'Nota', 'Comentário'), 
          # começa a pegar os valor de ('Protocolo', 'Nota', 'Comentário')
          # index > index_old => Só entra nesse IF se estiver na proxima linha
          # cell != 'Comentário' => pula a celular que contem a COLUNA = 'Comentário'
          if isProtocolo and isNota and isComentario and index > index_old and cell != 'Comentário':

            # print('index_old > index = ', index_old, '>', index)
            # print('TESTE 1', row.shape, 'index_cell:', index_cell, 'Protocolo:', index_cell_Protocolo, 'Nota:', index_cell_Nota, 'Comentario:', index_cell_Comentario)

            if index_cell == index_cell_Protocolo:
              if isPrint:
                print('Protocolo:', cell)
              dic_nps['Requisição'] = cell
              isProtocolo_index = True

            if index_cell == index_cell_Comentario:
              if isPrint:
                print('Comentário:', cell)
              dic_nps['Comentário'] = cell
              isComentario_index = True
          
            if index_cell == index_cell_Nota:
              if isPrint:
                print('Nota:', cell)
              dic_nps['Nota'] = cell
              isNota_index = True

            if isProtocolo_index and isComentario_index and isNota_index and isFirst ==  False:
              isFirst = True
              dic_nps['Responsável'] = operador_str
              list_dic_nps.append(dic_nps)

              if isPrint:
                print(dic_nps)

          ### FIM = for cell ###

      # # Zera o index, para a proxima linha
      # index_cell = 0
      index_old = index
      isFirst = False
      isOperador = False
      
      i = i + 1

      # if i == 30:
      #   break

    print('Sheet', sheet_page, 'list_dic_nps: ', len(list_dic_nps))

    full_list_nps.append(list_dic_nps)

    ################################################################################################
  except: 
    isExcept = True
    print('Acabou as sheets!')

  sheet_page = sheet_page + 1

  if isExcept:
    print('FIM DO EXCEL - isExcept', isExcept)
    break

print('full_list_nps', len(full_list_nps))
print('list_dic_nps', len(list_dic_nps))

list_dic_nps[0:5]

import os
import pandas as pd

if isPathLocal:
  path_root = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\Excel\\'
else:
  path_root = './drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/Excel/'

# /content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/Excel
# Obtem os arquivos na pasta
files = os.listdir(path_root)

path_full_files = []
for file in files:
  path_full = path_root + file
  path_full_files.append(path_full)
  #print(path_full)

path_full_files

from numpy.core.numeric import NaN
# Montar Dataframe nesse padrão!
# ['Requisição', 'Nota', 'Comentário', 'Responsável', 'Mês']

# sheet_page = 27
# df_excel = pd.read_excel(path_excel, sheet_name=sheet_page)

full_list_dic_nps = []

for file_excel in path_full_files:

  print(file_excel)

  isExcept = False
  sheet_page = 0

  list_dic_nps = [] # Lista de Dictionary

  operador_str = ''

  while True:
    #print('sheet_page:', sheet_page)
    
    try:

      ################################################################################################

      df_excel = pd.read_excel(file_excel, sheet_name=sheet_page)

      i = 0
      index_old = 0

      isPrint = False

      isFirst = False

      isProtocolo = False
      isNota = False
      isComentario = False

      isProtocolo_index = False
      isNota_index = False
      isComentario_index = False

      index_cell_Protocolo = 0
      index_cell_Nota = 0
      index_cell_Comentario = 0

      isOperador = False
      #operador_str = ''

      # list_dic_nps = [] # Lista de Dictionary


      for index, row in df_excel.iterrows():

        dic_nps = {'Requisição': NaN, 'Nota': NaN, 'Comentário': NaN, 'Responsável': NaN}

        ### 1 - Se contém SÓ as colunas (['Protocolo', 'Nota', 'Comentário'])
        if df_excel.columns.shape[0] == 3 and set(['Protocolo', 'Nota', 'Comentário']).issubset(df_excel.columns):
          if isPrint:
            print(index, row['Protocolo'], row['Nota'], row['Comentário'])

          dic_nps['Requisição'] = row['Protocolo']
          dic_nps['Comentário'] =  row['Comentário']
          dic_nps['Nota'] = row['Nota']
          dic_nps['Responsável'] = operador_str

          list_dic_nps.append(dic_nps)

        ### 2 - Se contém SO as 3 colunas e mais outras ['Protocolo', 'Nota', 'Comentário']
        elif df_excel.columns.shape[0] > 3 and set(['Protocolo', 'Nota', 'Comentário']).issubset(df_excel.columns) and isOperador == False:
          if isPrint:
            print(index, row['Protocolo'], row['Nota'], row['Comentário'])

          if type(row['Protocolo']) == str:
            if 'Operador:' in row['Protocolo']:

              isOperador = True
              operador_str = row['Protocolo'].replace('Operador: ', '')

              if isPrint:
                print('Operador:', operador_str)
          
          if isOperador == False:
            dic_nps['Requisição'] = row['Protocolo']
            dic_nps['Comentário'] =  row['Comentário']
            dic_nps['Nota'] = row['Nota']
            dic_nps['Responsável'] = operador_str

            list_dic_nps.append(dic_nps)

        ### 3 - sem colunas definidas
        else:

          # print(index, row.shape)
          # print(index, row)

          # Mostra as linhas
          #print('Linha - index:', index, 'index_old:', index_old)

          index_cell = 0

          ### INICIO = for cell ###
          for cell in row:

            index_cell = index_cell + 1
            
            # Acha a linha que contém o 'Operador: ')
            if type(cell) == str:
              #print('teste 1')

              if 'Operador: ' in cell:

                operador_str = cell.replace('Operador: ', '')

                if isPrint:
                  print('Operador:', operador_str)

                #print(dic_nps)

                # Zera as variaveis, por que e um novo operado!
                #isIndexPrint = False
                isProtocolo = False
                isNota = False
                isComentario = False

                isProtocolo_index = False
                isNota_index = False
                isComentario_index = False

                index_cell_Protocolo = 0
                index_cell_Nota = 0
                index_cell_Comentario = 0

              # Acha a linha que contém os ('Protocolo', 'Nota', 'Comentário')
              ### Obtem os indeces das colunas Protocolo, Nota, Comentário
              if isProtocolo == False or isNota == False or isComentario == False:

                # print(cell)
                if 'Protocolo' in cell and isProtocolo == False:
                  isProtocolo = True
                  index_cell_Protocolo = index_cell
                  #print(cell)

                if 'Nota' in cell and isNota == False:
                  isNota = True
                  index_cell_Nota = index_cell
                  #print(cell)
                
                if 'Comentário' in cell and isComentario == False:
                  isComentario = True
                  index_cell_Comentario = index_cell
                  #print(cell)

              if isProtocolo and isNota and isComentario:
                if isPrint:
                  print('FLAGS = index:', index, isProtocolo, isNota, isComentario, 'index', index, '>', index_old, 'index_old')

            # Se achou a linha que cotém os ('Protocolo', 'Nota', 'Comentário'), 
            # começa a pegar os valor de ('Protocolo', 'Nota', 'Comentário')
            # index > index_old => Só entra nesse IF se estiver na proxima linha
            # cell != 'Comentário' => pula a celular que contem a COLUNA = 'Comentário'
            if isProtocolo and isNota and isComentario and index > index_old and cell != 'Comentário':

              # print('index_old > index = ', index_old, '>', index)
              # print('TESTE 1', row.shape, 'index_cell:', index_cell, 'Protocolo:', index_cell_Protocolo, 'Nota:', index_cell_Nota, 'Comentario:', index_cell_Comentario)

              if index_cell == index_cell_Protocolo:
                if isPrint:
                  print('Protocolo:', cell)
                dic_nps['Requisição'] = cell
                isProtocolo_index = True

              if index_cell == index_cell_Comentario:
                if isPrint:
                  print('Comentário:', cell)
                dic_nps['Comentário'] = cell
                isComentario_index = True
            
              if index_cell == index_cell_Nota:
                if isPrint:
                  print('Nota:', cell)
                dic_nps['Nota'] = cell
                isNota_index = True

              if isProtocolo_index and isComentario_index and isNota_index and isFirst ==  False:
                isFirst = True
                dic_nps['Responsável'] = operador_str
                list_dic_nps.append(dic_nps)

                if isPrint:
                  print(dic_nps)

            ### FIM = for cell ###

        # # Zera o index, para a proxima linha
        # index_cell = 0
        index_old = index
        isFirst = False
        isOperador = False
        
        i = i + 1

        # if i == 30:
        #   break

      print('Sheet', sheet_page, 'list_dic_nps: ', len(list_dic_nps))

      ################################################################################################
    except: 
      isExcept = True
      print('Acabou as sheets!')

    sheet_page = sheet_page + 1

    if isExcept:
      print('FIM DO EXCEL - isExcept', isExcept)
      break
  
  full_list_dic_nps.append(list_dic_nps)

print('full_list_dic_nps:', len(full_list_dic_nps))
print('list_dic_nps:', len(list_dic_nps))

num = 0
for full in full_list_dic_nps:
  num = num + 1
  print('Itens', num,':', len(full))

list_dic_nps[0:4]

df_full

num = 0
for full in full_list_dic_nps:
  num = num + 1
  #print('Itens', num,':', len(full))
  print(type(full), type(full[0]))
  break

# Renomear as colunas
# df_full.columns = ['Requisição', 'Nota', 'Observação', 'Responsável', 'Mês']
print(type(full_list_dic_nps), type(full_list_dic_nps[0]), type(full_list_dic_nps[0][0]))

list_excel_dfs = [] # list
for full in full_list_dic_nps:

  excel_df = pd.DataFrame(full)
  print(type(full), type(full[0]), type(excel_df), excel_df.shape)

  list_excel_dfs.append(excel_df)

# Junta todos os dataframes
df_full_excel = pd.concat(list_excel_dfs)

df_full_excel['Mês'] = ''

df_full_excel.shape

df_full.shape

df_full.columns

df_full_excel.columns

df_full_data = pd.concat([ df_full_excel, df_full])

"""## DataSet NPS"""

df_full_data.shape

df_full_data

"""## Remove Tags Html - Comentário"""

import re, cgi

def remove_tag_html(text):
  tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
  text_result = cgi.escape(tag_re.sub('', text))
  return text_result

remove_tag_html('Obrigada<br>')

text_reuslt_html = [str(item) for item in df_full_data['Comentário']]

df_full_data['Comentário'] = text_reuslt_html

"""## Removendo "Requisição" duplicadas"""

df_full_data.shape

df_full_data = df_full_data.drop_duplicates('Requisição', keep='last')

df_full_data.shape

"""## Salva DataSet"""

def save_to_excel(df, name):
  # Salvar DataFrame
  if isPathLocal:
    path_root_out = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\'
  else:
    path_root_out = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/'
  
  df.to_excel(path_root_out + name)

# Salvar DataFrame
if isPathLocal:
    path_root_out = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\'
else:
    path_root_out = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/'

df_full_excel.to_excel(path_root_out + 'output_test.xlsx')

df_full_data.to_excel(path_root_out + 'output.xlsx')

"""## Carrega DataSet"""

def open_to_excel(name):
  # Salvar DataFrame
  if isPathLocal:
    path_root_out = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\'
  else:
    path_root_out = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/'
  
  df_output_ = pd.read_excel(path_root_out + name, sheet_name=0)
  return df_output_

import pandas as pd

if isPathLocal:
    path_root_out = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados\\'
else:
    path_root_out = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados/'

### Rodar a partir daqui! ### caso tenho o arquivo 'output.xlsx'
# Abrir DataFrame
df_output = pd.read_excel(path_root_out + 'output.xlsx', sheet_name=0)
df_output

# Total de Comentário validas
df_output[df_output['Comentário'].notnull()].shape

"""## Preparando os Dados - IMDB

"""

import pandas as pd
import numpy as np

if isPathLocal:
    path_imdb = 'D:\\2. Ciência de Dados\\1. Trabalho de Conclusão\\Dados do IMDB PT-BR\\imdb-reviews-pt-br.csv'
else:
    path_imdb = '/content/drive/MyDrive/1. Pós Ciência de Dados/1. Trabalho de Conclusão/Testes/Extrair Dados/Dados do IMDB PT-BR/imdb-reviews-pt-br.csv'

df_imdb = pd.read_csv(path_imdb)

df_imdb.shape

del df_imdb['text_en']

# 'pos' para 1 e 'neg' para 0
df_imdb['sentiment'].replace(['pos', 'neg'], [1, 0], inplace=True)

df_imdb.rename(columns={'text_pt': 'text', 'sentiment': 'target'}, inplace=True)

df_imdb

"""# Basic Naive Bayes - MultinomialNB"""

#import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

"""## Dados - train, test"""

X = df_imdb['text'].values # Textos
Y = df_imdb['target'].values # alvo

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.5) # 0.5 => 50% dos textos para teste ?? pega o dataset e faz um split entre treino e teste

data_test = pd.DataFrame(x_test, columns=['text'])
data_test['target'] = y_test #cria 1 dataframe utilizando pandas, um para teste

data_train = pd.DataFrame(x_train, columns=['text']) #cria 1 dataframe utilizando pandas, um para treinamento do modelo\
data_train['target'] = y_train

# Pega 30% dos dados para validar
data_val = df_imdb.sample(frac =.30)

print('data_test: ', len(data_test), 'data_train: ', len(data_train), 'data_val: ', len(data_val))

"""## Modelo"""

class MultinomialNBModel:

  def __init__(self, classes):
    self.classes = classes
    self.modelo = MultinomialNB()
  
  def vectorizer(self, texts):
    self.vectorizer = CountVectorizer(analyzer="word")
    self.texts_vec = self.vectorizer.fit_transform(texts)

  def fit(self):
    self.modelo.fit(self.texts_vec, self.classes)

  def prediction(self, texts):
    self.texts_vector = self.vectorizer.transform(texts)
    result = self.modelo.predict(self.texts_vector)
    return result

  def accuracy_score(self):
    results = cross_val_predict(self.modelo, self.texts_vec, self.classes, cv=10)
    metrics_ = metrics.accuracy_score(self.classes, results)
    return metrics_

predictor = MultinomialNBModel(data_test['target'])

predictor.vectorizer(data_test['text'])

"""## Treinamento"""

predictor.fit()

"""## Teste"""

testes = ['Esse governo está no início, vamos ver o que vai dar',
         'Estou muito feliz com o governo de Minas esse ano',
         'O estado de Minas Gerais decretou calamidade financeira!!!',
         'A segurança desse país é muio ruim',
         'O governador de Minas é bom']

predictions = predictor.prediction(testes)
predictions

"""## Avaliação"""

from sklearn import metrics
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import train_test_split

predictions_test = predictor.prediction(data_test['text'])
#predictions_test[0:10]

precision, recall, fscore, support = precision_recall_fscore_support(data_test['target'], predictions_test, average='binary')
print('precision:', precision, 'recall:', recall, 'fscore:', fscore)

texts_imdb = df_imdb.sample(frac =.40)
texts_test_imdb = texts_imdb['text']
texts_target_imdb = texts_imdb['target']

predictions_test_imdb = predictor.prediction(texts_test_imdb)
predictions_test_imdb

precision, recall, fscore, support = precision_recall_fscore_support(texts_target_imdb, predictions_test_imdb, average='binary')
print('precision:', precision, 'recall:', recall, 'fscore:', fscore)

metrics.accuracy_score(data_test['target'], predictions_test)

"""## DataSet - NPS"""

df_output_nps = df_output[df_output['Comentário'].notnull()]

df_output_nps.shape

df_output_nps_comentario = df_output_nps['Comentário'].tolist()

df_output_nps_comentario = [str(item) for item in df_output_nps_comentario]

predictions_nps = predictor.prediction(df_output_nps_comentario)
predictions_nps

len(predictions_nps)

df_output_nps['MultinomialNB'] = predictions_nps

df_output_nps

"""# Keras"""

import tensorflow as tf 
from tensorflow import keras

#import keras
from keras.layers import (
    Embedding,
    Conv1D,
    LSTM,
    Concatenate,
    GlobalMaxPool1D,
    Dense, 
)
from keras import Model
from keras import losses

from keras import backend as K

from distutils.version import LooseVersion as LV
from keras import __version__

from tensorflow.keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer, one_hot
from keras.preprocessing.sequence import pad_sequences

from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split # Metodo usado para obter os dados de treino e teste

print('Using Keras version:', __version__, 'backend:', K.backend())
assert(LV(__version__) >= LV("2.0.0"))

classes = df_imdb['target'].unique() # verifica todas as classes diferentes dentro do dataset imdb
classes # (1 == POSITIVO, 0 == NEGATIVO)

"""## Dados - train, test"""

X = df_imdb['text'].values # Textos
Y = df_imdb['target'].values # alvo

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.5) # 0.5 => 50% dos textos para teste ?? pega o dataset e faz um split entre treino e teste

data_test = pd.DataFrame(x_test, columns=['text'])
data_test['target'] = y_test #cria 1 dataframe utilizando pandas, um para teste

data_train = pd.DataFrame(x_train, columns=['text']) #cria 1 dataframe utilizando pandas, um para treinamento do modelo\
data_train['target'] = y_train

# Pega 30% dos dados para validar
data_val = df_imdb.sample(frac =.30)

print('data_test: ', len(data_test), 'data_train: ', len(data_train), 'data_val: ', len(data_val))

"""## Tokenização"""

class TokenizerText: #cria uma classe para tokenizar os textos, ou seja, vetoria todos os textos

  def __init__(self, texts, num_words=20000):
    #self.texts = texts

    self.tokenizer = Tokenizer(num_words=num_words)
    self.tokenizer.fit_on_texts(texts)
  
  def to_sequences(self, texts):
    tokens = self.tokenizer.texts_to_sequences(texts)
    return tokens

  def get_tokenizer(self):
    return self.tokenizer

tokenizerText = TokenizerText(data_train.text)

train_tokens = tokenizerText.to_sequences(data_train.text) # retorna os tokens para o treinamento
test_tokens = tokenizerText.to_sequences(data_test.text)# testes
val_tokens = tokenizerText.to_sequences(data_val.text)# validacao

# Print: Teste
train_tokens[0][:10]

lengths = [len(text_tokens) for text_tokens in train_tokens] # pega o tamanho de todos os textos, quantidade de tokens e converte para uma lista

plt.hist(lengths, bins=30) # printa um historiograma

# https://stackoverflow.com/questions/42943291/what-does-keras-io-preprocessing-sequence-pad-sequences-do
padded_val_tokens = pad_sequences(val_tokens, maxlen=850) 
padded_test_tokens = pad_sequences(test_tokens, maxlen=850)
padded_train_tokens = pad_sequences(train_tokens, maxlen=850)

# https://rdrr.io/cran/keras/man/to_categorical.html
train_label = to_categorical(data_train['target'], num_classes=len(classes))
val_label = to_categorical(data_val['target'], num_classes=len(classes))
test_label = to_categorical(data_test['target'], num_classes=len(classes))

"""## Modelo"""

inputs = keras.Input(shape=(850,)) 
embed = Embedding(20000, output_dim=300)(inputs) 
lstm = LSTM(256, return_sequences=True)(embed)
pooling = GlobalMaxPool1D()(lstm) 
classification = Dense(2, activation='softmax')(pooling) # N x 2 # Saida do modelo, o mesmo gera 2 saidas de dados, uma para positivo e outra para negativo

model = Model(inputs=inputs, outputs=classification)

model.summary()

epochs = 30 # 100 
learning_rate = 0.04 # Taxa de aprendizado # 0.001

# Definindo o tamanho dos batchs
batch_size = 512

optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
model.compile(
    optimizer=optimizer, 
    loss='categorical_crossentropy', 
    metrics=['accuracy']
)

padded_train_tokens.shape, train_label.shape

"""## Treinamento"""

history = model.fit(x=padded_train_tokens, y=train_label, batch_size=batch_size, epochs=epochs)

print(history.history)

plt.plot(history.history['loss'])
plt.show()

"""## Salvar o modelo"""

# modelo_nome = 'Modelo_1__11_01_2021_epochs_30' => ultimo
#modelo_nome = 'Modelo_1__11_01_2021_epochs_5'

modelo_nome = 'Modelo_1__20_02_2022_epochs_' + str(epochs)

model.save(path_root_out + modelo_nome)

"""## Carregar o modelo"""

model = keras.models.load_model(path_root_out + modelo_nome)

"""## Teste"""

class PredicModel:

  def __init__(self, model, tokenizer, classes):
    self.model = model
    self.tokenizer = tokenizer
    self.classes = classes

  def prediction(self, text: list):
    tokens = self.tokenizer.texts_to_sequences(text) 
    tokens = pad_sequences(tokens, maxlen=850)
    preds = self.model.predict(tokens)
    pred_class_prediction = preds.argmax(1)
    classes = [self.classes[pred] for pred in pred_class_prediction]
    return preds, classes

predictor = PredicModel(model, tokenizerText.get_tokenizer(), classes)

testes = ['Esse governo está no início, vamos ver o que vai dar',
         'Estou muito feliz com o governo de Minas esse ano',
         'O estado de Minas Gerais decretou calamidade financeira!!!',
         'A segurança desse país é muio ruim',
         'O governador de Minas é bom',
         'Eu sou bonito!']

predictions = predictor.prediction(testes)
predictions

predictions[1]

"""## Avaliação"""

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

tokenizerText_test = TokenizerText(data_test['text'])

predictor_test = PredicModel(model, tokenizerText_test.get_tokenizer(), data_test['target'].tolist())
predictor_test

predictions_test = predictor_test.prediction(data_test['text'].tolist())
type(predictions_test)

precision, recall, fscore, support = precision_recall_fscore_support(data_test['target'].tolist(), predictions_test[1], average='binary')
print('precision:', precision, 'recall:', recall, 'fscore:', fscore)

evaluate_ = model.evaluate(x=padded_val_tokens, y=val_label, batch_size=epochs)

evaluate_

"""## DataSet - NPS"""

df_output_nps_comentario = df_output_nps['Comentário'].tolist()

type(df_output_nps_comentario)

df_output_nps_comentario = [str(item) for item in df_output_nps_comentario]

predictions_nps = predictor.prediction(df_output_nps_comentario)
#len(predictions_nps[1])
len(predictions_nps)

len(predictions_nps[1])

#print(len(predictions_nps[0]), len(predictions_nps[1]))

df_output_nps['Keras_30'] = predictions_nps[1]
#df_output_nps['Keras_30'] = predictions_nps[1]
#df_output_nps['Keras'] = predictions_nps[1]

df_output_nps

"""#DataSet - NPS"""

df_name = 'df_output_nps.xlsx'

#save_to_excel(df_output_nps, df_name)

df_output_nps_ = open_to_excel(df_name)

# pip install openpyxl==3.0.0

df_output_nps_

df_output_nps_.shape

# Converte a coluna 'Nota' para INT
df_output_nps_['Nota'] = pd.to_numeric(df_output_nps_['Nota'], errors='coerce').fillna(0).astype(np.int64)

###############################################################################################
# Promotores nota de (9 e 10)

promotores_total = df_output_nps_.query('Nota >= 9 ')
promotores_total.shape

# Promotores (9 e 10) (MultinomialNB) = Positivos
promotores_MultinomialNB_pos = df_output_nps_.query('Nota >= 9 and MultinomialNB == 1 ')
promotores_MultinomialNB_pos.shape

# Promotores (9 e 10) (Keras_30) = Positivos
promotores_Keras_pos = df_output_nps_.query('Nota >= 9 and Keras_30 == 1 ')
promotores_Keras_pos.shape

# Promotores (9 e 10) (MultinomialNB/Keras_30)  = Positivos
promotores_MultinomialNB_Keras_pos = df_output_nps_.query('Nota >= 9 and MultinomialNB == 1 and Keras_30 == 1 ')
promotores_MultinomialNB_Keras_pos.shape

# Promotores (9 e 10) (MultinomialNB) = Negativos
promotores_MultinomialNB_neg = df_output_nps_.query('Nota >= 9 and MultinomialNB == 0 ')
promotores_MultinomialNB_neg.shape

# Promotores (9 e 10) (Keras_30) = Negativos
promotores_Keras_neg = df_output_nps_.query('Nota >= 9 and Keras_30 == 0 ')
promotores_Keras_neg.shape

# Promotores (9 e 10) (MultinomialNB/Keras_30) = Negativos
promotores_MultinomialNB_Keras_neg = df_output_nps_.query('Nota >= 9 and MultinomialNB == 0 and Keras_30 == 0 ')
promotores_MultinomialNB_Keras_neg.shape

# Promotores (9 e 10) (MultinomialNB/Keras_30)  = Diferença
promotores_MultinomialNB_Keras_pos = df_output_nps_.query('Nota >= 9 and MultinomialNB != Keras_30 ')
promotores_MultinomialNB_Keras_pos.shape

###############################################################################################
# Passivos nota de (7 e 8)

passivos_total = df_output_nps_.query('Nota >= 7 and Nota <= 8 ')
passivos_total.shape

# Passivos (7 e 8) (MultinomialNB) = Positivos
passivos_MultinomialNB_pos = df_output_nps_.query('Nota >= 7 and Nota <= 8 and MultinomialNB == 1 ')
passivos_MultinomialNB_pos.shape

# Passivos (7 e 8) (Keras_30) = Positivos
passivos_Keras_pos = df_output_nps_.query('Nota >= 7 and Nota <= 8  and Keras_30 == 1 ')
passivos_Keras_pos.shape

# Passivos (7 e 8) (MultinomialNB/Keras_30)  = Positivos
passivos_MultinomialNB_Keras_pos = df_output_nps_.query('Nota >= 7 and Nota <= 8  and MultinomialNB == 1 and Keras_30 == 1 ')
passivos_MultinomialNB_Keras_pos.shape

# Passivos (7 e 8) (MultinomialNB) = Negativos
passivos_MultinomialNB_neg = df_output_nps_.query('Nota >= 7 and Nota <= 8 and MultinomialNB == 0 ')
passivos_MultinomialNB_neg.shape

# Passivos (7 e 8) (Keras_30) = Negativos
passivos_Keras_neg = df_output_nps_.query('Nota >= 7 and Nota <= 8 and Keras_30 == 0 ')
passivos_Keras_neg.shape

# Passivos (7 e 8) (MultinomialNB/Keras_30) = Negativos
passivos_MultinomialNB_Keras_neg = df_output_nps_.query('Nota >= 7 and Nota <= 8 and MultinomialNB == 0 and Keras_30 == 0 ')
passivos_MultinomialNB_Keras_neg.shape

# Passivos (7 e 8) (MultinomialNB/Keras_30) = Diferença
passivos_MultinomialNB_Keras_neg = df_output_nps_.query('Nota >= 7 and Nota <= 8 and MultinomialNB != Keras_30 ')
passivos_MultinomialNB_Keras_neg.shape

###############################################################################################
# Detratores (nota de 0 a 6)

detratores_total = df_output_nps_.query('Nota >= 0 and Nota <= 6 ')
detratores_total.shape

# Detratores (0 a 6) (MultinomialNB) = Positivos
detratores_MultinomialNB_pos = df_output_nps_.query('Nota >= 0 and Nota <= 6 and MultinomialNB == 1 ')
detratores_MultinomialNB_pos.shape

# Detratores (0 a 6) (Keras_30) = Positivos
detratores_Keras_pos = df_output_nps_.query('Nota >= 0 and Nota <= 6 and Keras_30 == 1 ')
detratores_Keras_pos.shape

# Detratores (0 a 6) (MultinomialNB/Keras_30)  = Positivos
detratores_MultinomialNB_Keras_pos = df_output_nps_.query('Nota >= 0 and Nota <= 6 and MultinomialNB == 1 and Keras_30 == 1 ')
detratores_MultinomialNB_Keras_pos.shape

# Detratores (0 a 6) (MultinomialNB) = Negativos
detratores_MultinomialNB_neg = df_output_nps_.query('Nota >= 0 and Nota <= 6 and MultinomialNB == 0 ')
detratores_MultinomialNB_neg.shape

# Detratores (0 a 6) (Keras_30) = Negativos
detratores_Keras_neg = df_output_nps_.query('Nota >= 0 and Nota <= 6 and Keras_30 == 0 ')
detratores_Keras_neg.shape

# Detratores (0 a 6) (MultinomialNB/Keras_30) = Negativos
detratores_MultinomialNB_Keras_neg = df_output_nps_.query('Nota >= 0 and Nota <= 6 and MultinomialNB == 0 and Keras_30 == 0 ')
detratores_MultinomialNB_Keras_neg.shape

# Detratores (0 a 6) (MultinomialNB/Keras_30) = Diferença
detratores_MultinomialNB_Keras_neg = df_output_nps_.query('Nota >= 0 and Nota <= 6 and MultinomialNB != Keras_30 ')
detratores_MultinomialNB_Keras_neg.shape

