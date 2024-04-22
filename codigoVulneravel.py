import mysql.connector

# Função para criar a tabela se ela não existir
def criar_tabela(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        usuario VARCHAR(255) NOT NULL,
                        senha VARCHAR(255) NOT NULL)''')

# Função para inserir um novo usuário e senha no banco de dados
def inserir_usuario(cursor, usuario, senha):
    cursor.execute('''INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)''', (usuario, senha))

# Função para recuperar os usuários do banco de dados
def recuperar_usuarios(cursor):
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print("ID:", usuario[0])
        print("Usuário:", usuario[1])
        print("Senha:", usuario[2])
        print("")

# Estabelece a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="usuario"
)

if conexao.is_connected():
    print("Conexão estabelecida com sucesso.")

    cursor = conexao.cursor()

    # Criar a tabela se ela não existir
    criar_tabela(cursor)

    # Exemplo de uso: inserir um novo usuário e senha
    novo_usuario = input("Digite o nome de usuário: ")
    nova_senha = input("Digite a senha: ")
    inserir_usuario(cursor, novo_usuario, nova_senha)

    # Recuperar e exibir os usuários do banco de dados
    print("\nUsuários no banco de dados:")
    recuperar_usuarios(cursor)

    conexao.commit()
    cursor.close()
    conexao.close()

    print("\nUsuário e senha foram salvos no banco de dados.")
else:
    print("Falha ao conectar ao banco de dados.")
