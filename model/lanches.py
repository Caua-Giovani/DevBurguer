from database.conexao import conectar

def recuperar_lanches():
    conexao,cursor = conectar()
    
    cursor.execute("SELECT codigo,produto,descricao,preco,destaque,foto,disponibilidade FROM hamburguers;")

    lanches=cursor.fetchall()

    conexao.close()

    return lanches

def recuperar_lanches_destaque():
    conexao,cursor = conectar()
    cursor.execute("""SELECT codigo,produto,descricao,preco,destaque,foto,disponibilidade FROM hamburguers
                        WHERE destaque = 1;""")  
    
    lanches=cursor.fetchall()

    conexao.close()

    return lanches

def recuperar_lanches_unit(cod):
    conexao,cursor = conectar()

    cursor.execute("""SELECT codigo,produto,descricao,preco,destaque,foto,disponibilidade FROM hamburguers
                        WHERE codigo = %s;""",(cod, ))  
    
    lanches=cursor.fetchall()

    conexao.close()

    return lanches