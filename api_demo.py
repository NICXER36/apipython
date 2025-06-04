from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Datos simulados (mock)
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Mouse", "precio": 25},
    {"id": 3, "nombre": "Teclado", "precio": 45}
]

# GET: Obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos), 200

# POST: Crear un nuevo producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    nuevo = request.get_json()
    nuevo["id"] = len(productos) + 1
    productos.append(nuevo)
    return jsonify({"mensaje": "Producto creado", "producto": nuevo}), 201

# PUT: Reemplazar completamente un producto
@app.route('/productos/<int:id_producto>', methods=['PUT'])
def modificar_producto(id_producto):
    data = request.get_json()
    for producto in productos:
        if producto["id"] == id_producto:
            producto["nombre"] = data.get("nombre", producto["nombre"])
            producto["precio"] = data.get("precio", producto["precio"])
            return jsonify({"mensaje": f"Producto con ID {id_producto} modificado", "nuevo_producto": producto}), 200
    return jsonify({"error": "Producto no encontrado"}), 404

# PATCH: Modificar parcialmente un producto
@app.route('/productos/<int:id_producto>', methods=['PATCH'])
def modificar_parcialmente_producto(id_producto):
    data = request.get_json()
    for producto in productos:
        if producto["id"] == id_producto:
            producto.update(data)
            return jsonify({"mensaje": f"Producto con ID {id_producto} modificado parcialmente", "cambios": data}), 200
    return jsonify({"error": "Producto no encontrado"}), 404

# DELETE: Eliminar un producto
@app.route('/productos/<int:id_producto>', methods=['DELETE'])
def eliminar_producto(id_producto):
    global productos
    productos = [p for p in productos if p["id"] != id_producto]
    return jsonify({"mensaje": f"Producto con ID {id_producto} eliminado"}), 200

# HEAD: Solo obtener encabezados
@app.route('/productos-head', methods=['HEAD'])
def encabezados_productos():
    response = make_response("", 200)
    response.headers["Content-Type"] = "application/json"
    response.headers["X-Total-Productos"] = str(len(productos))
    return response

# OPTIONS: Ver qué métodos están permitidos en la ruta
@app.route('/productos-options', methods=['OPTIONS'])
def opciones_permitidas():
    response = make_response()
    response.headers["Allow"] = "GET,POST,PUT,PATCH,DELETE,OPTIONS,HEAD"
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
