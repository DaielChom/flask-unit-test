import json
from flask import request
from flask import Flask
from config import Config
from pagos import Pagos
from flask import Response
from flask import jsonify

from pagos import db

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/api/pagos", methods=['GET', 'POST'])
def pagos():

    if request.method == 'GET':
        pagos = Pagos.query.all()
        response = [i.serialize for i in pagos]

        return jsonify(results=response), 200

    elif request.method == "POST":
    
        try:
            requested_pago = Pagos(**request.get_json())    
            db.session.add(requested_pago)
            db.session.commit()
            
            if requested_pago.valorPagado == 1000000:
                response = {"respuesta": "gracias por pagar todo tu arriendo"}
            else:
                response = {"respuesta": f"gracias por tu abono, sin embargo recuerda que te hace falta pagar {1000000-requested_pago.valorPagado}"}
            
            return jsonify(response), 200

        except Exception as e:
            return str(e), 400


if __name__ == '__main__':
    
    db.init_app(app)
    app.run(host='0.0.0.0', port=8084)
    