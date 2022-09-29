import services.bd_carregamento as bdcarr
from mysql.connector.errors import ProgrammingError
import streamlit as st
import pandas as pd

def triagem():
        costumerList_carr = []
        script = "SELECT * FROM VWDATASETRELATORIO WHERE CONVERT(DATE,TICKET_DATA) = CONVERT (date, GETDATE()) AND TICKET_ESTADO = 'Pre cadastro' AND EMISSOR_DESCRICAO <> 'BR - PAULÍNIA' AND ITEM <> 'RESIDUO INDUSTRIAL'"
        with bdcarr.con:
            try:
                    cursor = bdcarr.con.cursor()
                    cursor.execute(script)
                    contatos = cursor.fetchall()
            except ProgrammingError as e:
                        print(f'Erro: {e.msg}')
            else:
                for contato in contatos:
                        costumerList_carr.append([contato[1], contato[4], contato[3], contato[2], contato[12], contato[23]])

        df = pd.DataFrame(
        costumerList_carr,
        columns=('TICKET', 'CAVALO','CARRETA', 'PRODUTO', 'CLIENTE', 'MOTORISTA'),
        )

        # def highlight_survived(s):
        #     return ['background-color: #004700']*len(s) if s.CARREGAMENTO=="CARREGANDO" else ['background-color: #595959']*len(s)
        
        st.dataframe(df)
        # st.dataframe(df.style.apply(highlight_survived, axis=1))