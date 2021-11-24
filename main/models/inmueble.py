class Inmueble:
    def __init__(self,
    id: str,
    ciudad: str,
    direccion: str,
    precio: str,
    descripcion: str,
    ano_construccion: str,
    status=None
    ) -> None:
        self.id = id
        self.ciudad = ciudad
        self.direccion = direccion
        self.precio = precio
        self.descripcion = descripcion
        self.ano_construccion = ano_construccion
        self.status = status

    def to_dict(self):
        return dict(
            id = self.id,
            ciudad = self.ciudad,
            direccion = self.direccion,
            precio = self.precio,
            descripcion = self.descripcion,
            ano_construccion = self.ano_construccion,
            status = self.status
            )