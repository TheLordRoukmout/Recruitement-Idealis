from odoo import models, fields, api

class ParkingClient(models.Model):
    _name = 'parking.client'
    _description = 'Client Parking'
    _rec_name = 'full_name'

    first_name = fields.Char(string='Prénom', required=True)
    last_name = fields.Char(string='Nom', required=True)
    license_plate = fields.Char(string='Immatriculation', required=True)
    subscription_paid = fields.Boolean(string='Abonnement payé', default=False)

    full_name = fields.Char(
        string='Nom complet',
        compute='_compute_full_name',
        store=True,
    )

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = f"{rec.first_name or ''} {rec.last_name or ''}".strip()