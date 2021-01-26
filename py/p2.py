# -*- coding: utf-8 -*-
"""P2-alt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15_PLsiO4wMkBei3Jma-eGvBITpCQVURk
"""

import pandas as pd
import numpy as np

df = pd.read_csv('EnjoySport.csv',index_col=0)

df.head()

def is_consistent(H,D):
  for i,d in enumerate(D):
    if H[i] != d and H[i] != '?':
      return False
  return True


def generalize_s(S,H):
  if (S == np.array(['%','%','%','%','%','%'])).all():
    return H
  for i,h in enumerate(H):
    if S[i] != h:
      S[i] = '?'
  return S

def specialize_g(G,S,H):
  for i,h in enumerate(H):
    if S[i] != h:
      G[i][i] = S[i]
  return G

concepts = np.array(df.iloc[:,:-1]).copy()
target = np.array(df.iloc[:,-1]).copy()

S = ['%','%','%','%','%','%']
G = [['?' for i in range(len(concepts[0]))] for j in range(len(concepts[0]))]

for i,h in enumerate(concepts):
  if target[i] == 'Yes':
    if not is_consistent(h,S):
      S = generalize_s(S,h)
      inconsistent_g = [i for i,s in enumerate(S) if s == '?']
      for g in inconsistent_g:
        G[g][g] = '?'
      # print(S)

  else:
    for j,g in enumerate(G):
      if is_consistent(g,h):
        G = specialize_g(G,S,h)
        # print(G)

filter_g = [i for i,g in enumerate(G) if g == ['?', '?', '?', '?', '?', '?']]
for i in filter_g:
  G.remove(['?', '?', '?', '?', '?', '?'])

print(S)
print(G)

