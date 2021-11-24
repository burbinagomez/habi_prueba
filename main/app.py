from config import app
from dao.inmuebledao import get_by_filter,get_by_id,get_all
from flask import request,jsonify

@app.route("/inmueble/filter/", methods=["POST"])
def get_inmuebles_by_filter():
    r = request.get_json()
    res = get_by_filter(**r)
    return jsonify(res)

@app.route("/inmueble/")
def get_inmuebles():
    return jsonify(get_all())

@app.route("/inmueble/<id>")
def get_inmueble(id):
    return jsonify(get_by_id(id))

if __name__ == "__main__":
    app.run()
