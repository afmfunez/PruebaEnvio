import pyodbc
from datetime import datetime

def conexion():
    conSQL = pyodbc.connect('DRIVER={SQL Server};SERVER=GV-TGU-AFMF\SQLEXPRESS;DATABASE=PruebaEnvio;Trusted_Connection=yes')
    return conSQL

def insert(docnUm, docdAte):
    try:
        cursor = conexion().cursor()

        fecha_doc = datetime.strptime(docdAte, '%d-%m-%Y')
        proc = """EXEC SP_INSERTAR_REGISTRO @P_DOCTYPE = %s, @P_DOCID = '%s', @P_DOCNUM = '%s', @P_DOCDATE = '%s'"""%(1,'FACT',docnUm,fecha_doc)

        cursor.execute(proc)

        conexion().commit()
        cursor.close()
        print("Registros agregados EExitosamente")
    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion().close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

insert('001','30-03-2022')