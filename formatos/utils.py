def codigoRetiroAportesColpensiones(afiliacion, cedula):
    numAfiliacion = str(afiliacion).rjust(12, "0")
    numCedula = str(cedula).rjust(12, "0")
    return f"{numAfiliacion}{numCedula}860015017R"

def codigoIngresoAportesColpensiones(afiliacion, cedula):
    numAfiliacion = str(afiliacion).rjust(12, "0")
    numCedula = str(cedula).rjust(12, "0")
    return f"{numAfiliacion}{numCedula}860015017A0000AFI000024313829"

def codigoRetiroCreditoColpensiones(afiliacion, cedula, pagare):
    numAfiliacion = str(afiliacion).rjust(12, "0")
    numCedula = str(cedula).rjust(12, "0")
    numPagare = str(pagare).rjust(9, "0")
    return f"{numAfiliacion}{numCedula}860015017{numPagare}RP"


def codigoIngresoCreditoColpensiones(afiliacion, cedula, pagare):
    numAfiliacion = str(afiliacion).rjust(12, "0")
    numCedula = str(cedula).rjust(12, "0")
    numPagare = str(pagare).rjust(9, "0")
    
    # Consulta para traer la cuota y el plazo
    cuota = "00000000" # 8 caracteres debe tener
    plazo = "000" # 3 caracteres
    
    constante1 = "PPRE000031380311"
    constante2 = "DIA000031380311"
    
    return f"{numAfiliacion}{numCedula}860015017{cuota}{plazo}{numPagare}{constante1}{constante2}"