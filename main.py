from conexion_postgresql import insertaRegistro, seleccionaParametros, ultimoRegistro
from conexion_sqlserver import insertar, consultar

for i in range(len(seleccionaParametros())):
    docNums = seleccionaParametros()[i][0]
    docDates = seleccionaParametros()[i][1]

    insertar(docNums, docDates)
print("Se agregaron los registros exitosamente")
