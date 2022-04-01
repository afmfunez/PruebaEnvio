import psycopg2
import pyodbc
import tkinter as tk

try:
    conPSQL = psycopg2.connect(
        host='localhost',
        port='5433',
        user='postgres',
        password='Grupo@2022',
        database='PruebaEnvio'
    )

    print("Conexión exitosa PostgreSQL")

    cursor = conPSQL.cursor()
    cursor.execute("SELECT * FROM \"Factura\"")
    rows = cursor.fetchall()
    #print(rows)

    def insertaRegistro(docnum, docdate):

        #docnum = input("Ingrese número de documento: ")
        #docdate = input("Ingrese fecha de documento: ")

        cursor.execute('CALL SP_INSERTAR_REGISTRO(%s,%s,%s,%s)',
                       (3, 'FACT', docnum, docdate))
        conPSQL.commit()
        cursor.close()
        print("Se insertaron los registros exitosamente")
    #for row in rows:
    #    print(row)

    """cursor.execute("SELECT table_name "
                   "FROM information_schema.tables"
                   "WHERE table_schema='public' AND table_type='BASE TABLE'")
    tablas = cursor.fetchall()

    OptionList = tablas

    app = tk.Tk()

    app.geometry('200x300')

    variable = tk.StringVar(app)
    variable.set(OptionList[0])

    opt = tk.OptionMenu(app, variable, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    app.mainloop()"""
    #insertaRegistro(input("Número documento: "), input("Fecha documento: "))
except DatabaseError as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    conPSQL.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")

