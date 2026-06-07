from odoo import models, fields

class RealEstateProject(models.Model):
    _name = 'real.estate.project'
    _description = 'Projet immobilier'
    _rec_name = 'name'

    name = fields.Char(string='Nom', required=True)
    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Compte analytique',
    )
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('planned', 'Planifié'),
        ('in_progress', 'En cours'),
        ('done', 'Terminé'),
    ], string='Statut', default='planned', required=True)