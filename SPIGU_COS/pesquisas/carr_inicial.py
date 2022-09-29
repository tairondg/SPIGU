import services.bd_carregamento as bdcarr
from mysql.connector.errors import ProgrammingError
import streamlit as st
import pandas as pd
from datetime import datetime

def carregamento_inicial():        
        costumerList_carr = []
        script = "SELECT * FROM VWDATASETRELATORIO WHERE CONVERT(DATE,TICKET_DATA) = CONVERT (date, GETDATE()) AND TICKET_ESTADO = 'Pesagem Inicial' AND EMISSOR_DESCRICAO <> 'BR - PAULÍNIA' AND ITEM <> 'RESIDUO INDUSTRIAL'"
        
        col1, col2, col3, col4 = st.columns(4)
        
        with bdcarr.con:
            try:
                    cursor = bdcarr.con.cursor()
                    cursor.execute(script)
                    contatos = cursor.fetchall()
            except ProgrammingError as e:
                        print(f'Erro: {e.msg}')
            else:
                for contato in contatos:
                        costumerList_carr.append([contato[1], contato[8], contato[4], contato[3], contato[2], contato[12], contato[23], contato[25]])
        
                # with st.form('form1'):
                #         with col1:
                #                 teste_carreta = st.selectbox("Carreta carregando", carretas)

                #         with col2:
                #                 data_e_hora_atuais = datetime.now()
                #                 data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                                
                #                 if st.button("Hora Inicial"):
                #                         st.write(data_e_hora_em_texto)

                                
                #         with col3:
                #                 data_e_hora_atuais = datetime.now()
                #                 data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

                #                 if st.button("Hr Final"):
                #                         st.write(data_e_hora_em_texto)

                #         with col4:
                #                 st.button("CONCLUÍDO")
        
        df = pd.DataFrame(
        costumerList_carr,
        columns=('TICKET','PESO', 'CAVALO','CARRETA', 'PRODUTO', 'CLIENTE', 'MOTORISTA', 'DATA'),
        )
        df['DATA'] = pd.to_datetime(df.DATA, format='%Y-%m-%d %H:%M')
        df['DATA'] = df['DATA'].dt.strftime('%d/%m/%y %H:%M')
        # df.insert(8, "CARREGAMENTO", 'AGUARDANDO')

        # def highlight_survived(s):
        #         return ['background-color: #005200']*len(s) if s.CARREGAMENTO=="AGUARDANDO" else ['background-color: ']*len(s)

        # st.dataframe(df.style.apply(highlight_survived, axis=1))

        st.dataframe(df)

        

