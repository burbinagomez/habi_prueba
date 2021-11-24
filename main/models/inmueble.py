"""
Class inmueble contain the structure to use in the project
"""

class Inmueble:
    """
    INmueble is class that contain the structure like DB

    to_dict-> REturn this class like dict object
    """
    def __init__(self,
    inmueble_id: str,
    ciudad: str,
    direccion: str,
    precio: str,
    descripcion: str,
    ano_construccion: str,
    status=None
    ) -> None:
        self.inmueble_id = inmueble_id
        self.ciudad = ciudad
        self.direccion = direccion
        self.precio = precio
        self.descripcion = descripcion
        self.ano_construccion = ano_construccion
        self.status = status

    def to_dict(self):
        return dict(
            id = self.inmueble_id,
            ciudad = self.ciudad,
            direccion = self.direccion,
            precio = self.precio,
            descripcion = self.descripcion,
            ano_construccion = self.ano_construccion,
            status = self.status
            )
