#import json
#import os

def ano_bissexto(ANO):
#correção em relação a duração estimada do ano, que não é de 365,25 dias e sim 365,2422 dias
    if ANO %4 == 0 and (ANO %100 != 0 or ANO %400 == 0): 
        return True
    else:
        return False
    
def dias_no_mes(MES, BISSEXTO):
    if MES in [1,3,5,7,8,10,12]:
        return 31 
    elif MES == 2:
        if not BISSEXTO:
            return 28
        else:
            return 29
    else: 
        return 30

ANO = 2024
MES = 2

BISSEXTO = ano_bissexto(ANO)
NUM_DIAS = dias_no_mes(MES, BISSEXTO)
print(f'ANO: {ANO}, MÊS: {MES}, QTD_DIAS: {NUM_DIAS}')

