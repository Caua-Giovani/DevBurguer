from database.conexao import conectar

def recuperar_lanches():
    conexao,cursor = conectar()

    cursor.execute("SELECT codigo,produto,descricao,preco,destaque,foto,disponibilidade FROM hamburguers;")
    
    lanches=cursor.fetchall()

    conexao.close()

    return lanches