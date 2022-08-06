
login = input("Digite seu Login: ")
senha = input("Diigte sua senha: ")

hash_login = hash(login)
hash_senha = hash(senha)

hash_teste_login = hash("icaro") #Variavel hash_teste_login foi incluida nesse contexto para simbolizar os dados de um BD
hash_teste_senha = hash("123")   #Variavel hash_teste_senha foi incluida nesse contexto para simbolizar os dados de um BD

print(hash_login)           #Debug
print(hash_senha)           #Debug
print(hash_teste_login)     #Debug
print(hash_teste_senha)     #Debug

if hash_login == hash_teste_login and hash_senha == hash_teste_senha:   #Verificando se a hash da senha enviada pelo usuario eh a mesma do "BD"
    print("ACCESS GRANTED!")
else:
    print("ACCESS DENIED")
