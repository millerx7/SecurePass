import secrets
import string

tamanho = int(input("Digite a quantidade de caracteres que você quer na senha: "))

def gerar_senha(tamanho = tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range (tamanho))
    return senha


senha_gerada = gerar_senha()
print(f"A senha forte gerada foi a {senha_gerada}")