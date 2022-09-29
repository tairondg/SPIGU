import services.bd_cadpesagem as db;


def incluir(carregamento_placa):
    count = db.cursor.execute("""
    UPDATE (HORA_INI_CARREGAM_GU) 
    VALUES (?)""",
    carregamento_placa.placa).rowcount
    db.con.commit()

def incluir(carregamento_horarioinicial):
    db.count = db.cursor.execute("""
    UPDATE (HORA_INI_CARREGAM_GU) 
    VALUES (?)""",
    carregamento_horarioinicial.hrinicial).rowcount
    db.con.commit()

def incluir(carregamento_horariofinal):
    db.count = db.cursor.execute("""
    INSERT INTO DATASETSPIGU (PLACA_CAVALO_GU, HORA_INI_CARREGAM_GU, HORA_FIM_CARREGAM_GU, STATUS_GU) 
    VALUES (?,?,?,?)""",
    carregamento_horariofinal.placa).rowcount
    db.con.commit()