#Função que busca valores em keys especificas
#Recebe list que é o dicionario original que vai ser analisado
#fltrs a key que vai ser analisada
#sps é o valor que vai ser selecionado para o dicionario novo
def filtr(list, fltrs, sps):
    
    #cria um dicionario novo para armazenar os itens selecionados
    newlist = {}

    #busca pelos itens vendo se o valor da key é igual ao esperado
    for item, item_info in list.items():
        
        #salva o item encontrado no dicionario criado anteriomente
        if sps == item_info[fltrs]:
          newlist[item] = list[item].copy()
    
    #printa quantos itens tem no dicionario
    print(f"{len(newlist)} pets available!")
    
    #retorna o novo dicionario
    return newlist