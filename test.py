from flask_sqlalchemy import SQLAlchemy
from main import app
import json

db = SQLAlchemy()
db.init_app(app)

def test_get_users():
    
    response = app.test_client().get('/api/pagos')
    assert response.status_code == 200

    res = json.loads(response.data).get("results")[0]
    assert res['codigoInmueble']=="8870"
    assert res['documentoIdentificacionArrendatario']==1036946622
    assert res['fechaPago']=="25/09/2020"

def test_post_usres():
    
    # test wrong date
    data = {"documentoIdentificacionArrendatario":1036946628,
            "codigoInmueble":8870,
            "valorPagado":1000000,
            "fechaPago":"32/09/2020"}
    response = app.test_client().post('/api/pagos', data=data)
    
    assert response.status_code == 400

    data = {"documentoIdentificacionArrendatario":1036946628,
            "codigoInmueble":8870,
            "valorPagado":1000000,
            "fechaPago":"28/09/2020"}
    response = app.test_client().post('/api/pagos', data=data)
    
    assert response.status_code == 400

    # test wrong value
    data = {"documentoIdentificacionArrendatario":1036946628,
            "codigoInmueble":8870,
            "valorPagado":10000000000,
            "fechaPago":"27/09/2020"}
    response = app.test_client().post('/api/pagos', data=data)
    
    assert response.status_code == 400
    
    

