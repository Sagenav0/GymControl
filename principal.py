from flask import Flask, render_template, request,redirect
from flaskext.mysql import MySQL
from CrearSuper_admin import Super_admin
import hashlib

programa = Flask(__name__)

mysql = MySQL()

programa.config['MYSQL_DATABASE_HOST'] = 'localhost'
programa.config['MYSQL_DATABASE_PORT'] = 3306
programa.config['MYSQL_DATABASE_USER'] = 'root'
programa.config['MYSQL_DATABASE_PASSWORD'] = ''
programa.config['MYSQL_DATABASE_DB'] = 'gymcontrol'
mysql.init_app(programa)


conexion = mysql.connect()
cursor = conexion.cursor()

Elsuper_admin = Super_admin(mysql)


@programa.route('/')
def inicio():

    return render_template('prueba.html')



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