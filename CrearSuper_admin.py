from datetime import datetime

class Super_admin:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()


    def consulta_super_admin(self):

        sql = "SELECT usuario, nombre, apellido, cedula, telefono, correo, rol, fecha_registro, user_registro, estado FROM operadores WHERE estado = 'activo' AND rol = 'admin' OR rol = 'super_admin'"
        self.cursor.execute(sql)
        resultado_super_Admin = self.cursor.fetchall()
        self.conexion.commit()
        return resultado_super_Admin

    def crear_super(self, super_admin):
        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        registro = 'cristian'

        sql = f"INSERT INTO operadores (usuario, nombre, apellido, cedula, telefono, correo, contrasena, rol, fecha_registro, user_registro, estado) VALUES ('{super_admin[0]}', '{super_admin[1]}', '{super_admin[2]}', '{super_admin[3]}', '{super_admin[4]}', '{super_admin[5]}', '{super_admin[6]}', '{super_admin[7]}', '{fecha_actual}', '{registro}', '{super_admin[8]}')"

        self.cursor.execute(sql)
        self.conexion.commit()