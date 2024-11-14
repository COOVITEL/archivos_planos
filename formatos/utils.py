import pandas as pd
import cx_Oracle
import os
from dotenv import load_dotenv

load_dotenv()

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
    checkExist = usersBase(pagare, cedula)
    if len(checkExist) == 0:
        return 404
    return f"{numAfiliacion}{numCedula}860015017{numPagare}RP"

def codigoIngresoCreditoColpensiones(afiliacion, cedula, pagare):
    numAfiliacion = str(afiliacion).rjust(12, "0")
    numCedula = str(cedula).rjust(12, "0")
    numPagare = str(pagare).rjust(9, "0")
    
    userData = usersBase(pagare, cedula)

    if len(userData) == 0:
        return 404

    cuota = str(int(userData[0]['V_CUOTA'])).rjust(8, "0") # 8 Caracteres
    plazo = str(int(userData[0]['PLAZO'])).rjust(3, "0") # 3 Caracteres
    
    constante1 = "PPRE000031380311"
    constante2 = "DIA000031380311"
    
    return f"{numAfiliacion}{numCedula}860015017{cuota}{plazo}{numPagare}{constante1}{constante2}"

def codigoFopep(typeDoc, document, application, aport, libranza):
    numCedula = str(document).rjust(12, "0")
    numPagare = str(libranza).rjust(12, "0")
    user = usersBase(libranza, document)
    if len(user) == 0:
        return 404
    date = user[0]['FECHA_LIQUIDACION'].strftime("%Y-%m-%d")
    month = date.split("-")[1]
    year = date.split("-")[0][-2:]
    value = int(user[0]['V_CUOTA'])
    cuotas = int(user[0]['PLAZO'])
    totalValue = str(int(value * cuotas)).rjust(9, "0")
    setValueMonth = str(value).rjust(8, "0")
    setAddress = str(user[0]['DIRECCION']).rjust(45, "0")
    cel = str(user[0]['CELULAR']).rjust(12, "0")
    setPhone = str(user[0]['TELEFONO'])[-7:] if user[0]['TELEFONO'] is not None else str(user[0]['CELULAR'])[-7:]
    city = user[0]['CIUDAD'][-3:]
    dep = user[0]['DEPARTAMENTO']
    email = str(user[0]['MAIL']).rjust(40, "0")
    return f"{typeDoc}{numCedula}0694{year}{month}{totalValue}00{setValueMonth}00{application}000000{aport}{numPagare}{setAddress}{setPhone}{city}{dep}{cel}{email}*"

def usersBase(pagare, cedula):
    """ This function calls the user for cc """
    query = f"""
            SELECT AP014.AANUMNIT CEDULA, CA090.A_OBLIGA PAGARE, ca093.q_cuota PLAZO, ca093.v_cuota v_CUOTA, ca090.F_LIQUID fecha_liquidacion,
            GR005.D_TERCER DIRECCION, GR005.T_TERCER TELEFONO, GR005.K_CIUDAD CIUDAD, GR005.K_DEPART DEPARTAMENTO, GR005.T_TERCEL CELULAR, GR005.D_EMAIL MAIL
            FROM AP014MCLIENTE AP014, CA090MGSOLCRED CA090, CA093MDSOLCRED CA093, GR005MDIRECCIO gr005
            WHERE AP014.K_IDTERC = CA090.K_IDTERC
            AND CA090.K_NOMINA IN ('FOP','131')
            AND CA090.K_NUMDOC = CA093.K_NUMDOC
            AND GR005.I_TIPDIR = 'C'
            AND AP014.K_IDTERC = GR005.K_IDTERC
            AND TRIM (ca090.k_tipodr) = TRIM (ca093.k_tipodr)
            AND TRIM (ca090.q_reestr) = TRIM (ca093.k_idrees)
            AND ca090.i_estsol = 'C'
            AND ca093.i_tipcuo = 'O'
            AND ca090.i_cancel <> 'H'
            and CA090.A_OBLIGA = '{pagare}'
            and AP014.AANUMNIT = '{cedula}'
        """
    dsn_tns = cx_Oracle.makedsn(os.getenv('NAME_SERVER'), os.getenv('PORT'), service_name=os.getenv('SERVICE'))
    # dsn_tns = cx_Oracle.makedsn('10.100.200.38', '1521', service_name='lnxcvt')
    try:
        with cx_Oracle.connect(user=os.getenv('USER'), password=os.getenv('PASSWORD'), dsn=dsn_tns) as conn:
        # with cx_Oracle.connect(user='CONSUL', password='CONSULTAR', dsn=dsn_tns) as conn:
            with conn.cursor() as cursor:
                query = query
                # query = "SELECT * FROM bi_ahorro_vista_mes"
                cursor.execute(query)
                # data = cursor.fetchmany(800)
                data = cursor.fetchall()
                print(data)
                columns = [desc[0] for desc in cursor.description]
                users = [dict(zip(columns, row)) for row  in data]
                return users
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 1017:
            print('Error en las credenciales')
        else:
            print(f'Error en la conexión en la base de datos: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')


if __name__ == '__main__':
    usersBase()