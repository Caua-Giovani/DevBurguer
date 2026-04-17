from database.conexao import conectar

def autenticar_usuario(login:str, senha:str) -> bool:
    try:
        conexao, cursor = conectar()

        cursor.execute(""" SELECT usuario,senha FROM usuarios WHERE usuario = %s AND senha = %s """,(login,senha))

        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return True
        else:
            return False
    except:
        return False

def adicionar_usuario(login:str,senha:str,nome:str) -> bool:
    try:
        conexao,cursor = conectar()

        cursor.execute("""INSERT INTO usuarios 
                    VALUES(%s,%s,%s)""",(login,senha,nome))
        
        conexao.commit()
        conexao.close()
        return True
    except:
        return False