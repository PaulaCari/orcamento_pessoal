def ver_receitas():
    lista_itens = []
    with con: 
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens
print(ver_receitas())