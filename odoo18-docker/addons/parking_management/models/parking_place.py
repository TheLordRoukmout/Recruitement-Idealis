from odoo import models, fields

class ParkingPlace(models.Model):
    _name = 'parking.place'
    _description = 'Place de Parking'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string='Numéro de place', required=True)
    is_available = fields.Boolean(string='Disponible', default=True)