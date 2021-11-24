import sys
sys.path.append("..")
from config import db_engine
from models.inmueble import Inmueble
from models.status import Status
from sqlalchemy import text

table = "property"

def get_by_filter(**kwargs):
    inmuebles = []
    status = Status()
    if len(kwargs) > 0:
        if len(kwargs) == 1 and "status" in kwargs:
            query = f"SELECT * FROM {table} "
        else:
            query = f"SELECT * FROM {table} WHERE "
    for kwarg in kwargs:
        if kwarg == "status":
            continue
        query+= f"{kwarg}='{kwargs[kwarg]}',"
    query = query[:-1]
    query = query.replace(","," AND ")
    with db_engine.connect() as conn:
        
        result = conn.execute(
            text(query)
        )
        for row in result:
            status_history_result = conn.execute(
                text(f"SELECT status_id FROM status_history WHERE property_id={row.id} ORDER BY update_date DESC LIMIT 1")
            )
            row_status_history = status_history_result.fetchone()
            try:
                if status.verify_status(status.get_status_by_value(row_status_history.status_id)):
                    r_inmueble = Inmueble(
                        id = row.id,
                        ciudad = row.city,
                        direccion = row.address,
                        precio = row.price,
                        descripcion = row.description,
                        ano_construccion = row.year,
                        status = status.get_status_by_value(row_status_history.status_id)
                    )
                elif status.verify_status(kwargs["status"]) and status.get_value_by_status(kwargs["status"]) == row_status_history.status_id:
                    r_inmueble = Inmueble(
                        id = row.id,
                        ciudad = row.city,
                        direccion = row.address,
                        precio = row.price,
                        descripcion = row.description,
                        ano_construccion = row.year,
                        status = status.get_status_by_value(row_status_history.status_id)
                    )
                
                else:
                    continue
                inmuebles.append(r_inmueble.to_dict())
            except Exception as e:
                continue
    return inmuebles

def get_by_id(id):
    r_inmueble = None
    status = Status()
    with db_engine.begin() as conn:
        inmueble_result = conn.execute(
            text(f"SELECT * FROM {table} WHERE id={id}")
        )
        row = inmueble_result.fetchone()
        status_history_result = conn.execute(
            text(f"SELECT status_id FROM status_history WHERE property_id={id} ORDER BY update_date DESC LIMIT 1")
        )
        row_status_history = status_history_result.fetchone()

        if status.verify_status(status.get_status_by_value(row_status_history.status_id)):
            r_inmueble = Inmueble(
                id = row.id,
                ciudad = row.city,
                direccion = row.address,
                precio = row.price,
                descripcion = row.description,
                ano_construccion = row.year,
                status = status.get_status_by_value(row_status_history.status_id)
            ).to_dict()
        else:
            r_inmueble = "Can't show"
    return r_inmueble


def get_all():
    inmuebles = []
    query = f"SELECT * FROM {table}"
    status = Status()
    with db_engine.connect() as conn:
        result = conn.execute(
            text(query)
        )
        for row in result:
            status_history_result = conn.execute(
                text(f"SELECT status_id FROM status_history WHERE property_id={row.id} ORDER BY update_date DESC LIMIT 1")
            )
            row_status_history = status_history_result.fetchone()
            try:
                if status.verify_status(status.get_status_by_value(row_status_history.status_id)):
                    r_inmueble = Inmueble(
                        id = row.id,
                        ciudad = row.city,
                        direccion = row.address,
                        precio = row.price,
                        descripcion = row.description,
                        ano_construccion = row.year,
                        status = status.get_status_by_value(row_status_history.status_id)
                    )
                else:
                    continue
                inmuebles.append(r_inmueble.to_dict())
            except Exception as e:
                continue

    return inmuebles
