from database.conexao import conectar

def autenticar_usuario(login:str, senha:str) -> bool:
    try:
        conexao, cursor = conectar()

        cursor.execute(""" SELECT login,nome FROM usuarios WHERE login = %s AND senha = %s """,(login,senha))

        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return resultado
        else:
            return False
    except:
        return False

def adicionar_usuario(login:str,senha:str,nome:str) -> bool:
    try:
        conexao,cursor = conectar()

        cursor.execute("""INSERT INTO usuarios (login,nome,senha) VALUES(%s,%s,%s)""",(login,nome,senha))
        
        conexao.commit()
        conexao.close()
        return True
    except:
        return False