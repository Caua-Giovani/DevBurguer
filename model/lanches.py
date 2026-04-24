from database.conexao import conectar

def recuperar_lanches():
    conexao,cursor = conectar()
    
    cursor.execute("""SELECT codigo,produto,descricao,preco,destaque,foto,disponibilidade FROM hamburguers
                        WHERE disponibilidade = 1;""")

    lanches=cursor.fetchall()

    conexao.close()

    return lanches

def recuperar_lanches_destaque():
    conexao,cursor = conectar()
    cursor.execute("""SELECT codigo,produto,descricao,preco,destaque,foto,disponibilidade FROM hamburguers
                        WHERE destaque = 1 and disponibilidade = 1;""")  
    
    lanches=cursor.fetchall()

    conexao.close()

    return lanches

def recuperar_lanches_unit(cod):
    conexao,cursor = conectar()

    cursor.execute("""SELECT codigo,produto,descricao,preco,destaque,foto,disponibilidade FROM hamburguers
                        WHERE codigo = %s;""",(cod, ))  
    
    lanches=cursor.fetchone()

    conexao.close()

    return lanches

def recuperar_lanches_carrinho(cod):
    conexao,cursor = conectar()

    cursor.execute("""SELECT hamburguers.codigo,hamburguers.produto,hamburguers.preco,hamburguers.foto, COUNT(carrinho.cod) AS quantidade FROM hamburguers
                        INNER JOIN carrinho ON carrinho.lanche = hamburguers.codigo
                        WHERE carrinho.usuario = %s
                        GROUP BY carrinho.lanche;""",(cod,)) 
    
    lanches=cursor.fetchall()

    conexao.close()

    return lanches

def adicionar_lanche_carrinho(cod, usuario):
    try:
        conexao,cursor = conectar()

        cursor.execute("""INSERT INTO carrinho(lanche,usuario) VALUES(%s,%s)""",(cod,usuario)) 
        
        conexao.commit()

        conexao.close()

        return True
    except:
        return False
    

def remover_lanche_carrinho(cod, usuario):
    try:
        conexao,cursor = conectar()

        cursor.execute("""DELETE FROM carrinho WHERE lanche = %s AND usuario = %s LIMIT 1;""",(cod,usuario)) 
        
        conexao.commit()

        conexao.close()

        return True
    except:
        return False

