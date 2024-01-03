import pymysql

host = 'localhost'
usuario = 'root'
senha = 'Vitinho07'
banco = 'controle_gastos'

# Conectar ao banco de dados
conexao = pymysql.connect(host=host, user=usuario, password=senha, database=banco)

# Criar um cursor
cursor = conexao.cursor()

def adicionar_gasto(nome, valor):
    comando = f'INSERT INTO gastos (Nome, Valor) VALUES ("{nome}", "{valor}")'                   
    cursor.execute(comando)
    conexao.commit()

def remover_gasto(id):
    comando = f'DELETE FROM gastos WHERE IdGasto = {id}'
    cursor.execute(comando)
    conexao.commit()

def limpar_tabela():
    comando = f'TRUNCATE TABLE gastos'
    cursor.execute(comando)
    conexao.commit()

def linhas():
    comando = f'SELECT * FROM gastos'
    cursor.execute(comando)
    conexao.commit()
    return cursor.fetchall()

def mudarUsuario(novo_usuario):
    comando = f'TRUNCATE TABLE user'
    cursor.execute(comando)
    conexao.commit()

    comando = f'INSERT INTO user (user) VALUES ("{novo_usuario}")'
    cursor.execute(comando)
    conexao.commit()

def mudarRendaMensal(nova_renda):
    comando = f'TRUNCATE TABLE renda_mensal'
    cursor.execute(comando)
    conexao.commit()

    comando = f'INSERT INTO renda_mensal (renda_mensal) VALUES ("{nova_renda}")'
    cursor.execute(comando)
    conexao.commit()

def renda_mensal():
    comando = f'SELECT * FROM renda_mensal'
    cursor.execute(comando)
    conexao.commit()
    return cursor.fetchall()[0][0]

def user_name():
    comando = f'SELECT * from user'
    cursor.execute(comando)
    conexao.commit()
    return cursor.fetchall()[0][0]