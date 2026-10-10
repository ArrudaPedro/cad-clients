def rodar_terminal():
    import sqlite3
    
    # Conexão ao db SQLlite
    conn = sqlite3.connect("dataclients.db")
    cursor = conn.cursor()

    # Cria a tabela se ela não existir
    cursor.execute("""
        CREATE TABLE if NOT EXISTS clients (
            id INT ,
            name TEXT,
            endereco TEXT,
            qtd_pedidos INT,
            valor_pedidos INT
            )
    """)



    

def todos_clientes():
    import sqlite3

    conn = sqlite3.connect("dataclients.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    client_data = cursor.fetchall()

    conn.close()

    clientes = []
    for client_data in client_data:
        clientes.append({
            "id": client_data[0],
            "name": client_data[1],
            "endereco": client_data[2],
            "qtd_pedidos": client_data[3],
            "valor_pedidos": client_data[4]
        })
    return clientes
    
    

def add_client(dados: dict):
    import sqlite3
    
    conn = sqlite3.connect("dataclients.db")
    cursor = conn.cursor()


    cursor.execute("""
        INSERT INTO clients (name, endereco, qtd_pedidos, valor_pedidos)
                VALUES (?, ?, ?, ?)
        """,(
                dados["name"],
                dados["endereco"],
                dados.get("qtd_pedidos",0), 
                dados.get("valor_pedidos",0.0)
            ))
    novo_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return {"id": novo_id, **dados}


