from .models import Producto

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id_producto = str(Producto.id)
        if id_producto not in self.carrito.keys():
            self.carrito[id_producto] = {
                "producto": producto,
                "cantidad": 1,
                "precio_total": Producto.preciounitarioproducto,
            }
        else:
            self.carrito[id_producto]["cantidad"] += 1
            self.carrito[id_producto]["precio_total"] += producto.preciounitarioproducto
        
        self.guardar_carrito()
            
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto_id):
        id_producto = str(producto_id)
        if id_producto in self.carrito:
            del self.carrito[id_producto]
        
        self.guardar_carrito()
        
    def restar(self, producto_id):
        id_producto = str(producto_id)
        if id_producto in self.carrito:
            if self.carrito[id_producto]["cantidad"] > 1:
                self.carrito[id_producto]["cantidad"] -= 1
                self.carrito[id_producto]["precio_total"] -= self.carrito[id_producto]["producto"].preciounitarioproducto
            else:
                self.eliminar(producto_id)

        self.guardar_carrito()
        
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
