from Interface import*
from tradutor_lista import*
from time import sleep


nao_achados = []
final = []

while True:
    option_menu = menu(["Cadastrar nova Palavra: ", "Remover Palavra",
                                                    "Mostrar Dicionário", "Traduzir", "Sair"])
    if option_menu == 1:
        word = user_word('Palavra em inglês: ')
        translate_word = user_word('Tradução Palavra: ')
        tradutor.append([word, translate_word])
        sleep(0.5)
    elif option_menu == 2:
        print(tradutor)
        print('Para remover uma palavra, digite primeiro a Palavra em inglês'
              ' e depois a tradução da palavra para remover-lá da lista de tradução')
        del_word_user = user_word('Digite a palavra em inglês: ')
        del_word_user_transl = user_word('Digite a palavra em portugês: ')
        removed_list = [del_word_user, del_word_user_transl]
        if removed_list in tradutor:
            tradutor.remove(removed_list)
            print('Par de palavras retirado...')
        else:
            print('Não foi possivél remover o par de palavras')
        sleep(0.5)
    elif option_menu == 3:
        print(tradutor)
        sleep(1)
    elif option_menu == 4:
        new_string = word_translation('Digite algo a ser traduzido: ')
        frase = new_string.split()
        for palavra in frase:
            pos_j = 0
            final.append(palavra)
            nao_achados.append(palavra)
            for indice in tradutor[pos_j]:
                while pos_j < len(tradutor):
                    if palavra == tradutor[pos_j][0]:
                        final.pop()
                        final.append(tradutor[pos_j][1])
                        break
                    else:
                        pos_j += 1
                        
        print('\nEstá é a tradução: ')
        print(' '.join(final))

        if len(set(final) & set(nao_achados)) > 0:
            print('\nAs palavras não traduzidas são: \n', set(final) & set(nao_achados))
        
        final.clear()
        nao_achados.clear()    
    elif option_menu == 5:
        print("sair")
        sleep(1)
        break
    else:
        print("Digite Somente uma das Opções acima (1, 2, 3, 4)")

