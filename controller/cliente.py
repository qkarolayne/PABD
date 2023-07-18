#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(matricula, nome, idade, id_turma):
    db.cur.execute("""
                   INSERT into public.tbaluno (matricula, nome, idade, id_turma)
                   VALUES ('%s','%s','%s', '%s')
                   """ % (matricula, nome, idade, id_turma))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM public.tbaluno
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para deletar registro no banco de dados
def deletar(matricula):
    db.cur.execute("""
                    DELETE FROM tbaluno WHERE matricula = '%s';
                    """ % (matricula))
    db.con.commit()