from string import ascii_letters, punctuation

tradutor = [['car', 'carro'], ['house', 'casa'], ['red', 'vermelho'], ['pink', 'rosa'],
            ['black', 'preto'], ['is', 'é'], ['this', 'isto']]


def user_word(word):
    while True:
        word_user = str(input(word))
        if not all(letter in ascii_letters or punctuation for letter in word_user):
            print('\033[31mErro: por favor, Digite somente letras.\033')
            continue
        else:
            return word_user


def word_translation(txt):
    entrada = input(txt)
    return entrada
  
