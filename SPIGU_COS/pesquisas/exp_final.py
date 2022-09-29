import services.bd_carregamento as bdcarr
from mysql.connector.errors import ProgrammingError
import streamlit as st
import pandas as pd
import time
from datetime import date
import datetime



def expedicao_final():
        costumerList_carr = []
        carretas = []
        script = "SELECT * FROM VWDATASETRELATORIO WHERE FINAL_OPERACAO_DATA BETWEEN GETDATE()-10 AND GETDATE() AND TICKET_ESTADO = 'Pesagem final' AND EMISSOR_DESCRICAO <> 'BR - PAULÍNIA'"
        with bdcarr.con:
            try:
                    cursor = bdcarr.con.cursor()
                    cursor.execute(script)
                    contatos = cursor.fetchall()
            except ProgrammingError as e:
                        print(f'Erro: {e.msg}')
            else:
                for contato in contatos:
                        costumerList_carr.append([contato[1], contato[8], contato[4], contato[3], contato[2], contato[12], contato[35], contato[10], contato[23], contato[29]])
                        carretas.append(contato[3])
        
        df = pd.DataFrame(
        costumerList_carr,
        columns=('TICKET','PESO', 'CAVALO','CARRETA', 'PRODUTO', 'CLIENTE','PESO LIQUIDO','TRANSPORTADORA', 'MOTORISTA', 'DATA'),
        )
        df['DATA'] = pd.to_datetime(df.DATA, format='%Y-%m-%d %H:%M')
        df['DATA'] = df['DATA'].dt.strftime('%d/%m/%y %H:%M')

        # def highlight_survived(s):
        #     return ['background-color: #004700']*len(s) if s.CARREGAMENTO=="CARREGANDO" else ['background-color: #595959']*len(s)
        
        # st.dataframe(df)
        # # st.dataframe(df.style.apply(highlight_survived, axis=1))

        col1, col2, col3, col4 = st.columns(4)
        data_ = date.today()
        data_hoje_inicio_exp = data_.strftime('%d/%m/%y 00:00')
        data_hoje_fim_exp = data_.strftime('%d/%m/%y 23:59')

        date_now = datetime.datetime.now()
        seven_days_ago = date_now - datetime.timedelta(days=7)
        data_7dias = seven_days_ago.strftime('%d/%m/%y')
        data_relatorio = seven_days_ago.strftime('%d-%m-%y')

        with col1:
                data_inicio_exp = st.text_input('Data Inicio', data_hoje_inicio_exp)
        
        with col2:
                data_fim_exp = st.text_input('Data Fim', data_hoje_fim_exp)
        
        with col3:
                st.write('')
                st.write('')
                st.caption(f'Pesquisa disponivel até {data_7dias}')

        
        dataframe_expfinal = df[df['DATA'].between(data_inicio_exp, data_fim_exp)]  
        
               
        # def highlight_survived(s):
        #     return ['background-color: #004700']*len(s) if s.CARREGAMENTO=="CARREGANDO" else ['background-color: #595959']*len(s)
        if st.button('Pesquisar'):
                st.dataframe(dataframe_expfinal)
                dataframe_expfinal.to_excel('relatorios\Relatorio_exp_final.xlsx')
                file2 =  open('relatorios\Relatorio_exp_final.xlsx', "rb")
                time.sleep(3)
                st.download_button(
                        label="Download para excel",
                        data=file2,
                        file_name=f"Relatorio_exp_final{data_relatorio}.xlsx",
                        )