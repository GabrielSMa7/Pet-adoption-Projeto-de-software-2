#Função que busca valores em keys especificas
#Recebe list que é o dicionario original que vai ser analisado
#fltrs a key que vai ser analisada
#sps é o valor que vai ser selecionado para o dicionario novo
def filtr(list, fltrs, sps):
    
    #cria um dicionario novo para armazenar os itens selecionados
    newlist = [i for i in list if getattr(i, fltrs, "").lower() == sps.lower()]

    #printa quantos itens tem no dicionario
    print(f"{len(newlist)} pets available!")
    
    #retorna o novo dicionario
    return newlist