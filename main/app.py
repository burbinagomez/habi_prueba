"""
This file contain the run server and the request controllers
"""

from config import app
from dao.inmuebledao import get_by_filter,get_by_id,get_all
from flask import request,jsonify

@app.route("/inmueble/filter/", methods=["POST"])
def get_inmuebles_by_filter():
    """
    Method for get inmuebles by a filter
    Receive json
    Return json
    """
    r_json = request.get_json()
    res = get_by_filter(**r_json)
    return jsonify(res)

@app.route("/inmueble/")
def get_inmuebles():
    """
    Method for get all inmuebles
    """
    return jsonify(get_all())

@app.route("/inmueble/<id>")
def get_inmueble(inmueble_id):
    """
    MEthod for get a inmueble by id
    """
    return jsonify(get_by_id(inmueble_id))

if __name__ == "__main__":
    app.run()
