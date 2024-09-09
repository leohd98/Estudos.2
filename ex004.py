palavra = input('Digite algo: ')

# define TYPE -----------------------------------------------
try:
    val = int(palavra)
    print(f"O tipo de dado é: {type(val)} (inteiro)")
except ValueError:
    try:
        val = float(palavra)
        print(f"O tipo de dado é: {type(val)} (float)")
    except ValueError:
        if palavra.lower() in ["true", "false"]:
            val = bool(palavra.lower() == "true")
            print(f"O tipo de dado é: {type(val)} (booleano)")
        else:
            print(f"O tipo de dado é: {type(palavra)} (string)")

# só tem espaços? -------------------------------------------
print(f'Só tem espaços? {palavra.isspace()}')

# é um número? ----------------------------------------------
print(f'É um número? {palavra.isnumeric()}')

# é alfabético? ---------------------------------------------
print(f'É alfabético? {palavra.isalpha()}')

# é alfanumérico? -------------------------------------------
print(f'É alfanumérico? {palavra.isalnum()}')

# está em maiúsculas? ---------------------------------------
print(f'Está em maiúsculas? {palavra.isupper()}')

# está em minúsculas? ---------------------------------------
print(f'Está em minúsculas? {palavra.islower()}')

# está capitalizada? ----------------------------------------
print(f'Está capitalizada? {palavra.istitle()}')
