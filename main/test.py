import unittest
import sys
sys.path.append("..")
from config import db_engine
from sqlalchemy import text
import requests

class Test(unittest.TestCase):
    status = {
            "pre_venta":3,
            "en_venta":4,
            "vendido":5,
        }

    def test_get_all(self):
        inmuebles = 0
        with db_engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM property")
            )
            for row in result:
                status_id = conn.execute(
                    text(f"SELECT status_id FROM status_history WHERE property_id={row.id} ORDER BY update_date DESC LIMIT 1")
                ).fetchone()
                for _ in self.status:
                    if status_id:
                        if self.status[_] == status_id.status_id:
                            inmuebles +=1

        req = requests.get("http://localhost:5000/inmueble/")
        self.assertEqual(inmuebles,len(req.json()))

    def test_filter_status_pre_venta(self):
        inmuebles = 0
        with db_engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM property")
            )
            for row in result:
                status_id = conn.execute(
                    text(f"SELECT status_id FROM status_history WHERE property_id={row.id} ORDER BY update_date DESC LIMIT 1")
                ).fetchone()
                if status_id:
                    if status_id.status_id == self.status["pre_venta"]:
                        inmuebles +=1

        req = requests.post("http://localhost:5000/inmueble/filter/",
        json=dict(status="pre_venta")
        )
        self.assertEqual(inmuebles,len(req.json()))

    def test_filter_status_en_venta(self):
        inmuebles = 0
        with db_engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM property")
            )
            for row in result:
                status_id = conn.execute(
                    text(f"SELECT status_id FROM status_history WHERE property_id={row.id} ORDER BY update_date DESC LIMIT 1")
                ).fetchone()
                if status_id:
                    if status_id.status_id == self.status["en_venta"]:
                        inmuebles +=1

        req = requests.post("http://localhost:5000/inmueble/filter/",
        json=dict(status="en_venta")
        )
        self.assertEqual(inmuebles,len(req.json()))

    def test_filter_status_vendido(self):
        inmuebles = 0
        with db_engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM property")
            )
            for row in result:
                status_id = conn.execute(
                    text(f"SELECT status_id FROM status_history WHERE property_id={row.id} ORDER BY update_date DESC LIMIT 1")
                ).fetchone()
                if status_id:
                    if status_id.status_id == self.status["vendido"]:
                        inmuebles +=1

        req = requests.post("http://localhost:5000/inmueble/filter/",
        json=dict(status="vendido")
        )
        self.assertEqual(inmuebles,len(req.json()))

    def test_filter_status_other(self):
        inmuebles = 0
        with db_engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM property")
            )
            for row in result:
                status_id = conn.execute(
                    text(f"SELECT status_id FROM status_history WHERE property_id={row.id} ORDER BY update_date DESC LIMIT 1")
                ).fetchone()
                if status_id:
                    if status_id.status_id in [i for i in self.status.values]:
                        inmuebles +=1

        req = requests.post("http://localhost:5000/inmueble/filter/",
        json=dict(status="comprando")
        )
        self.assertEqual(inmuebles,len(req.json()))

    def test_filter_city(self):
        inmuebles = 0
        with db_engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM property WHERE city='bogota'")
            )
            for row in result:
                status_id = conn.execute(
                    text(f"SELECT status_id FROM status_history WHERE property_id={row.id} ORDER BY update_date DESC LIMIT 1")
                ).fetchone()
                for _ in self.status:
                    if status_id:
                        if self.status[_] == status_id.status_id:
                            inmuebles +=1

        req = requests.post("http://localhost:5000/inmueble/filter/",
        json=dict(city="bogota")
        )
        self.assertEqual(inmuebles,len(req.json()))

    def test_filter_year(self):
        pass

    def test_multiple_filters(self):
        pass

    def test_get_by_inmueble_id(self):
        pass

if __name__ == '__main__':
    unittest.main()