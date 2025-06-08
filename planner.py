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
    largura = 24

    # Cabeçalho
    caixa = ("+" + "-"*largura)*7+"+"
    #caixa = "+------------"*7+"+"
    print(caixa)
    print("| "+" | ".join(dia.center(largura-2) for dia in dias_semana))
    print(caixa)

    dia = 1
    while dia <= dias_mes:
        linha_dias, linhas_tarefas = [], [[] for _ in range(3)]
        for i in range(7):
            if dia == 1 and i<inicio:
                linha_dias.append(" " * largura)
                for linha in linhas_tarefas:
                    linha.append(" " * largura)
            elif dia <= dias_mes:
                linha_dias.append(f'{dia} '.rjust(largura))
                lista = tarefas.get(dia, [])

                for j in range(3):
                    if j == 2 and len(lista) > 3:
                        # + de duas tarefas (...)
                        linhas_tarefas[j].append("...".center(largura))
                    elif j < len(lista):
                        # tarefa abrev
                        tarefa = (" " + lista[j][:largura-1]).ljust(largura)
                        linhas_tarefas[j].append(tarefa)
                    else:
                        # linha vazia
                        linhas_tarefas[j].append(" " * largura)
                dia+=1
            else:
                linha_dias.append(" " * largura)
                for linha in linhas_tarefas:
                    linha.append(" " * largura)
        print("|"+"|".join(linha_dias)+"|")
        for linha in linhas_tarefas:
            print("|"+"|".join(linha)+"|")
        print(caixa)

ANO = 2025
MES = 6
BISSEXTO = ano_bissexto(ANO)
NUM_DIAS = dias_no_mes(ANO, MES)
tarefas = {
    1: ["Estudar", "Limpar casa", "Fazer lista de compras"],
    2: ["Yoga"],
    3: ["Revisar provas", "Assistir aula", "Enviar email", "Ler artigo"],
    4: ["Descansar"],
    5: ["Trabalho em grupo"],
    6: ["Exercício físico", "Mercado"],
    7: ["PsicoEducação", "Consulta médica"],
    8: ["Organizar arquivos", "Backup"],
    9: ["Estudar Cálculo", "Revisar slides"],
    10: ["Prova de BD", "Comprar lanche", "Trocar lâmpada"],
    11: ["Dia livre"],
    12: ["Limpar geladeira", "Agendar revisão"],
    13: ["Churrasco com amigos", "Preparar sobremesa", "Comprar carvão", "Lavar roupa"],
    14: ["Fazer relatório"],
    15: ["Revisão geral", "Preparar apresentação"],
    16: ["Jogar videogame", "Descansar", "Ver série"],
    17: ["Aula prática", "Responder fórum", "Corrigir exercícios"],
    18: ["Festa da turma"],
    19: ["Estudar com colega"],
    20: ["Prova final", "Fazer resumo"],
    21: ["Dia de folga"],
    22: ["Organizar planilhas", "Revisar scripts", "Atualizar planner"],
    23: ["Fazer exercício", "Passear com cachorro"],
    24: ["Revisar notas", "Mandar email pro professor"],
    25: ["Aniversário da mãe", "Comprar presente", "Fazer bolo"],
    26: ["Estudar redes", "Prova de redes", "Revisar DHCP"],
    27: ["Reunião online", "Testar projeto"],
    28: ["Atualizar CV", "Procurar estágio"],
    29: ["Limpar casa", "Arrumar quarto"],
    30: ["Encerrar tarefas do mês", "Planejar julho"]
}

desenha_planner(ANO, MES)