from pymongo import MongoClient
client = MongoClient("mongodb://root:senac123@127.0.0.1:37452")

# Seleção do banco de dados
db = client.loga_db
# print(db)

'''
Estamos obtendo os dados qie estão cadastrados na tabela(coleção) usuario. Usamos db[""].find() 
O comando find locariza os dados e retorna com todos eles para vilariavel 'us'. Depois, fazemos a leitura de todas as linhas com o for e exibimos na tela
'''
# for us in db.usuario.find(): - dois modos de pegar os dados 
# for us in db["usuario"].find():
#     print(us)


# Abaixo, a consulta realiza o cadastro de um novo usuario e retorna o id do usuario cadastrado 
usuario_id = db["usuario"].insert_one({"nomeusuario":"cadu","senha":"pythonisgud","nivel":"ADM"}).inserted_id
print(usuario_id)


# Abaixo, locarizar apenas um usuario no banco de dados
# rs = db["usuario"].find_one({"nivel":"usuario"})
# print(rs)


# Abaixo, locarizar tdos os dados com o nivel de aceeso 'usuario'
for rs in db["usuario"].find({"nivel":"usuario"}):
    print(rs)