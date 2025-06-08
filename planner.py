def ano_bissexto(ANO):
#correção em relação a duração estimada do ano, que não é de 365,25 dias e sim 365,2422 dias
    if ANO %4 == 0 and (ANO %100 != 0 or ANO %400 == 0): 
        return True
    else:
        return False
    
def dias_no_mes(ANO, MES):
    if MES in [1,3,5,7,8,10,12]:
        return 31 
    elif MES == 2:
        if not ano_bissexto(ANO):
            return 28
        else:
            return 29
    else: 
        return 30

def desenha_planner(ANO, MES):
    if ANO!=2025:
        print('No momento, apenas a versão de 2025 está disponível.')
        return
    
    primeiro_dia_2025 = {1:3, 2:6, 3:6, 4:2, 5:4, 6:0, 7:2, 8:5, 9:1, 10:3, 11:6, 12:1} #tentando não utilizar bibliotecas por enquanto
    dias_semana = ['Dom','Seg','Ter','Qua','Qui','Sex', 'Sáb']
    dias_mes = dias_no_mes(ANO, MES)
    inicio = primeiro_dia_2025[MES]
    largura = 12

    # Cabeçalho
    caixa = "+------------"*7+"+"
    print(caixa)
    print("| "+" | ".join(dia.center(10) for dia in dias_semana))
    print(caixa)

    dia = 1
    while dia <= dias_mes:
        linha_dias, linha_tarefas = [], []
        for i in range(7):
            if dia == 1 and i<inicio:
                linha_dias.append(" " * largura)
            elif dia <= dias_mes:
                linha_dias.append(f'{dia}'.rjust(largura))
                dia+=1
            else:
                linha_dias.append(" "*largura)
        print("|"+"|".join(linha_dias)+"|")
        print(caixa)

ANO = 2025
MES = 6

BISSEXTO = ano_bissexto(ANO)
NUM_DIAS = dias_no_mes(ANO, MES)
print(f'ANO: {ANO}, MÊS: {MES}, QTD_DIAS: {NUM_DIAS}')

desenha_planner(ANO, MES)

