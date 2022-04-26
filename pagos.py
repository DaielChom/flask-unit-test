from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import datetime

db = SQLAlchemy()

class Pagos(db.Model):

    __tablename__ = 'pagos'

    documentoIdentificacionArrendatario = db.Column(db.Integer,  primary_key=True)
    fechaPago = db.Column(db.DateTime)
    codigoInmueble = db.Column(db.String)
    valorPagado = db.Column(db.Integer)

    def __init__(self, fechaPago, documentoIdentificacionArrendatario, codigoInmueble, valorPagado):
        self.valorPagado = int(valorPagado)
        self.fechaPago = fechaPago
        self.documentoIdentificacionArrendatario = documentoIdentificacionArrendatario
        self.codigoInmueble = codigoInmueble

    @property
    def serialize(self):
        return {
            'fechaPago': self.fechaPago,
            'documentoIdentificacionArrendatario': self.documentoIdentificacionArrendatario,
            'codigoInmueble': self.codigoInmueble,
            'valorPagado': self.valorPagado,   
        }

    @validates('valorPagado')
    def validate_valor_pagado(self, key, value):
        
        if value>1000000 or value<1:
            raise ValueError("Valor pagado invalido")

        return value

    @validates('fechaPago')
    def validate_fecha_pago(self, key, value):
        
        try:
            
            datetime.datetime.strptime(value, '%d/%m/%Y')

        except ValueError:
            raise ValueError("Formato de fecha incorrecto")
            
        day = int(value.split('/')[0])
        
        if day%2==0:
            raise ValueError("Lo siento pero no se puede recibir el pago por decreto de la administracion")
            return value

        