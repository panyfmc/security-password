from string import ascii_letters, digits, punctuation      #biblioteca que me dá acesso a todas as letras a-z, A-Z, números 0-9, e símbolos (32)

for i in ascii_letters + digits + punctuation:          #verifica a 1° posição da senha
    for j in ascii_letters + digits + punctuation:          #verifica a 2° posição da senha
        for k in ascii_letters + digits + punctuation:          #verifica a 3° posição da senha
            for l in ascii_letters + digits + punctuation:          #verifica a 4° posição da senha
                print(i, j, k, l)
                