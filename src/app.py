from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ListaClientes')
def ListaClientes():
    return render_template('ListaClientes.html')

@app.route('/ListaFacturas')
def ListaFacturas():
    return render_template('ListaFacturas.html')

@app.route('/ListaProductos')
def ListaProductos():
    return render_template('ListaProductos.html')

@app.route('/ListaUsuarios')
def ListaUsuarios():
    return render_template('ListaUsuarios.html')

@app.route('/NuevaFactura')
def NuevaFactura():
    return render_template('NuevaFactura.html')

@app.route('/NuevoCliente')
def NuevoCliente():
    return render_template('NuevoCliente.html')

@app.route('/NuevoProducto')
def NuevoProducto():
    return render_template('NuevoProducto.html')

@app.route('/NuevoUsuario')
def NuevoUsuario():
    return render_template('NuevoUsuario.html')

if __name__ == '__main__':
    app.run(debug=True)
    
