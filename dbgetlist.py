import sqlite3

# print("DB Command")
# print()
# Databases

# Create a database or connector to one
conn = sqlite3.connect("metrogoDB.db")

# Create a cursor to enter data
c = conn.cursor()

# Create table
# use triple quotes to enter multiline string/comment

c.execute("""SELECT linhas_estacoes.nome_conexao,
            linhas_estacoes.id_linha,
            linhas.nome_linha 
            FROM linhas_estacoes,
            linhas,
            estacoes
            where linhas.id_linha = linhas_estacoes.id_linha
            and estacoes.id_estacao = linhas_estacoes.id_estacao
            and (linhas.nome_linha = "Azul"
            or linhas.nome_linha = "Rubi"
            or linhas.nome_linha = "Amarela");""")

stations_list_query = c.fetchall()
# print(stations_list_query)

stations_db_list = []
for x in stations_list_query:
    stations_db_list.append([x[2], x[0]])

# print()
# print(stations_db_list)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

# print()
# print("Done")
