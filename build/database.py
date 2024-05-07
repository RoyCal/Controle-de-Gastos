import sqlite3

# Cria o banco de dados
banco = sqlite3.connect("banco_de_dados.db")

# Criar um cursor
cursor = banco.cursor()

# Cria as tabelas se ainda não existem
cursor.execute("CREATE TABLE IF NOT EXISTS gastos (IdGasto INTEGER PRIMARY KEY AUTOINCREMENT, Nome VARCHAR(45), Valor FLOAT)")
cursor.execute("CREATE TABLE IF NOT EXISTS renda_mensal (renda_mensal FLOAT)")
cursor.execute("CREATE TABLE IF NOT EXISTS user (user VARCHAR(50))")

def adicionar_gasto(nome, valor):
    comando = f'INSERT INTO gastos (Nome, Valor) VALUES ("{nome}", "{valor}")'                   
    cursor.execute(comando)
    banco.commit()

def remover_gasto(id):
    comando = f'DELETE FROM gastos WHERE IdGasto = {id}'
    cursor.execute(comando)
    banco.commit()

def limpar_tabela():
    comando = f'DELETE FROM gastos'
    cursor.execute(comando)
    banco.commit()

def linhas():
    comando = f'SELECT * FROM gastos'
    cursor.execute(comando)
    banco.commit()
    return cursor.fetchall()

def mudarUsuario(novo_usuario):
    comando = f'DELETE FROM user'
    cursor.execute(comando)
    banco.commit()

    comando = f'INSERT INTO user (user) VALUES ("{novo_usuario}")'
    cursor.execute(comando)
    banco.commit()

def mudarRendaMensal(nova_renda):
    comando = f'DELETE FROM renda_mensal'
    cursor.execute(comando)
    banco.commit()

    comando = f'INSERT INTO renda_mensal (renda_mensal) VALUES ("{nova_renda}")'
    cursor.execute(comando)
    banco.commit()

def renda_mensal():
    comando = f'SELECT * FROM renda_mensal'
    cursor.execute(comando)
    banco.commit()

    try:
        return cursor.fetchall()[0][0] # Se a tabela ainda estiver vazia
    except:
        comando = f'INSERT INTO renda_mensal (renda_mensal) VALUES ("100")' # Define a renda mensal como 100 
        cursor.execute(comando)
        banco.commit()
        comando = f'SELECT * FROM renda_mensal'
        cursor.execute(comando)
        banco.commit()

    return cursor.fetchall()[0][0]

def user_name():
    comando = f'SELECT * from user'
    cursor.execute(comando)
    banco.commit()

    try:
        return cursor.fetchall()[0][0] # Se a tabela ainda estiver vazia
    except:
        comando = f'INSERT INTO user (user) VALUES ("usuario")' # Define o usuário como 'usuario'
        cursor.execute(comando)
        banco.commit()
        comando = f'SELECT * from user'
        cursor.execute(comando)
        banco.commit()

    return cursor.fetchall()[0][0]