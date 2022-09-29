import pyodbc

con = pyodbc.connect("Driver={SQL Server};Server=172.16.60.3;Database=SGMC_COS;UID=sa;PWD=********;") 
cursor = con.cursor()  
