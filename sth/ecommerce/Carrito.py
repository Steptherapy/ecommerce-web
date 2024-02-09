from .models import Producto

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        
        carrito = self.session.get("carrito")
        if carrito is None:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, id_producto):
        producto = Producto.objects.get(id=id_producto)
        id_producto = str(id_producto)  # Convertir a cadena si es necesario
        if id_producto not in self.carrito.keys():
            self.carrito[id_producto] = {
                "id_producto": producto.id,  # Utilizar el ID del producto
                "nombre": producto.nombreproducto,
                "Precio": float(producto.preciounitarioproducto),
                "Cantidad": 1,
            }
        else:
            self.carrito[id_producto]["Cantidad"] += 1
            self.carrito[id_producto]["Precio"] = float(producto.preciounitarioproducto)
        
        self.guardar_carrito()
            
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id_producto = str(producto.id)
        if id_producto in self.carrito:
            del self.carrito[id_producto]
        
        self.guardar_carrito()
        
    def restar(self, id_producto):
        producto = Producto.objects.get(id=id_producto)
        id_producto = str(id_producto)  # Convertir a cadena si es necesario
        if id_producto not in self.carrito.keys():
            self.carrito[id_producto] = {
                "id_producto": producto.id,  # Utilizar el ID del producto
                "nombre": producto.nombreproducto,
                "Precio": float(producto.preciounitarioproducto,0),
                "Cantidad": 1,
            }
        else:
            if self.carrito[id_producto]["Cantidad"] > 1:
                self.carrito[id_producto]["Cantidad"] -= 1
                self.carrito[id_producto]["Precio"] = float(producto.preciounitarioproducto)
            else:
                self.eliminar(producto)
        
        self.guardar_carrito()
        
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def obtener_productos_en_carrito(self):
        productos_en_carrito = []
        for detalle_producto in self.carrito.values():
            productos_en_carrito.append(detalle_producto)  # Agregar directamente el detalle del producto
        return productos_en_carrito

    
    
    def obtener_total_carrito(self):
        total = 0
        for detalle_producto in self.carrito.values():
            if isinstance(detalle_producto, dict):
                precio = int(detalle_producto.get('Precio', 0))
                cantidad = int(detalle_producto.get('Cantidad', 0))
                total += precio * cantidad
        return total
