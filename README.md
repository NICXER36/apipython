# apipython
-
metodos:

get
-URL: http://127.0.0.1:5000/productos

post
-http://127.0.0.1:5000/productos
-en boy seleccionar raw y cambiar de texto a json 
-y ingresar un producto de la siguiente forma: {
                                                   "nombre":"nombre producto"
                                                   "precio":"precio producto"
                                             }

put
-http://127.0.0.1:5000/productos/idproducto a modificar
-ingrear nuevos valores:{
  "nombre": "Laptop actualizada",
  "precio": 1500
}

patch
-http://127.0.0.1:5000/productos/idproducto
-ingresar dato a actualizado: {
  "precio": 30
}

delete
-http://127.0.0.1:5000/productos/idproducto a borrar

head
-http://127.0.0.1:5000/productos/3

options
-http://127.0.0.1:5000/productos-options
