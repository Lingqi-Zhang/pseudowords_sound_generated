# coding=utf8
import numpy as np
import pandas as pd
import random
wordfile1=pd.read_csv("words/verb.csv",encoding='utf-8',)
wordfile2=pd.read_csv("words/noun.csv",encoding='utf-8')
wordfile3=pd.read_csv("words/adj.csv",encoding='utf-8')
wordv=pd.DataFrame(data=wordfile1)
wordn=pd.DataFrame(data=wordfile2)
worda=pd.DataFrame(data=wordfile3)
words=pd.concat([wordv,wordn,worda])
words.columns=['number','chinese','happiness']
words.reset_index(inplace=True,drop=False)
newwords=[]
letter=[]
for i in range(len(words['happiness'])):
    if words['happiness'][i]>=4 and words['happiness'][i]<=6:
        newwords.append(words['chinese'][i])
length=len(newwords)
for i in range(length):
    for j in range(len(newwords[i])):
        letter.append(newwords[i][j])     
letter=pd.DataFrame(data=letter,columns=['L'])
letter.sample(frac=1).reset_index(drop=True)
fir_letter=letter['L'].sample(500,replace=False).reset_index(drop=True).tolist()
sec_letter=letter['L'].sample(500,replace=False).reset_index(drop=True).tolist()
neowords=[]
for i in range(500):
    neoword=str(fir_letter[i])+str(sec_letter[i])
    neowords.append(neoword)

neowords=pd.DataFrame(data=neowords,columns=['pseudowords'])
neowords.to_csv('pseudowords.csv')
    
        

