def menu_header(txt):
    print("-" * 42)
    print(txt.center(42))
    print("-" * 42)


def menu(option_list):
    menu_header("Menu principal")
    counter = 1
    for item in option_list:
        print(f"\033[33m{counter}\033[m - \033[34m{item}\033[m")
        counter += 1
    print("-"*42)
    user_option = user_value("\033[32mEscolha uma das opções acima: \033[m")
    return user_option


def user_value(msg_value):
    while True:
        try:
            choose_user = int(input(msg_value))
        except(ValueError, TypeError):
            print('\033[31mErro: por favor, digite somente os numeros inteiros válidos.\033m')
        else:
            return choose_user
