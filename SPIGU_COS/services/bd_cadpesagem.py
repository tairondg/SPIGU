import pyodbc

con = pyodbc.connect("Driver={SQL Server};Server=172.16.60.3;Database=SPIGU_COS;UID=sa;PWD=********;") 
cursor = con.cursor()  


# teste_pesq = "SELECT * FROM DATASETSPIGU"
# cursor.execute(teste_pesq)  
# row = cursor.fetchone()  
# while row:  
#     print(str(row))     
#     row = cursor.fetchone()  