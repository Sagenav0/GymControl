from flask import Flask, render_template, request,redirect
from flaskext.mysql import MySQL
from CrearSuper_admin import Super_admin
import hashlib

programa = Flask(__name__)

mysql = MySQL()

programa.config['MYSQL_DATABASE_HOST'] = 'gymcontrol.mysql.database.azure.com'
programa.config['MYSQL_DATABASE_PORT'] = 3306
programa.config['MYSQL_DATABASE_USER'] = 'horux69'
programa.config['MYSQL_DATABASE_PASSWORD'] = 'gym_control2525'
programa.config['MYSQL_DATABASE_DB'] = 'gym_control'
mysql.init_app(programa)


conexion = mysql.connect()
cursor = conexion.cursor()

Elsuper_admin = Super_admin(mysql)


@programa.route('/')
def inicio():

    resultado_super_Admin = Elsuper_admin.consulta_super_admin()

    return render_template('prueba.html', admin_super = resultado_super_Admin)



@programa.route('/operadores/crear/super_admin', methods= ["post"])
def crear_Superadmin():

    usuario = request.form['usuario']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    cedula = request.form ['cedula']
    telefono = request.form['telefono']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    rol = 'super_admin'
    estado = 'activo'
    cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()

    Elsuper_admin.crear_super([usuario, nombre, apellido, cedula, telefono, correo, cifrada,  rol,  estado])

    return redirect('/')





if __name__ == '__main__':
    programa.run(debug=True)