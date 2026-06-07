from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    real_estate_project_id = fields.Many2one(
        'real.estate.project',
        string='Projet immobilier',
        tracking=True,
    )
    is_project_done = fields.Boolean(
        compute='_compute_is_project_done',
        store=False,
    )

    @api.depends('real_estate_project_id', 'real_estate_project_id.status')
    def _compute_is_project_done(self):
        for order in self:
            order.is_project_done = (
                order.real_estate_project_id.status == 'done'
            )

    @api.onchange('real_estate_project_id')
    def _onchange_real_estate_project(self):
        project = self.real_estate_project_id
        for line in self.order_line:
            if project and project.analytic_account_id:
                line.analytic_distribution = {
                    str(project.analytic_account_id.id): 100.0
                }
            elif not project:
                if len(line.analytic_distribution or {}) == 1:
                    line.analytic_distribution = {}

    def write(self, vals):
        res = super().write(vals)
        if 'real_estate_project_id' in vals:
            for order in self:
                project = order.real_estate_project_id
                for line in order.order_line:
                    if project and project.analytic_account_id:
                        line.analytic_distribution = {
                            str(project.analytic_account_id.id): 100.0
                        }
                    elif not project:
                        if len(line.analytic_distribution or {}) == 1:
                            line.analytic_distribution = {}
        return res