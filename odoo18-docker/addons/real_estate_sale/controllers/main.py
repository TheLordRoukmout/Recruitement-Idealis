from odoo import http
from odoo.http import request


class WebsiteSaleProject(http.Controller):

    @http.route('/shop/project', type='http', auth='public', website=True)
    def shop_project_step(self, project_id=None, **kwargs):
        order = request.website.sale_get_order(force_create=True)

        if project_id is not None:
            if int(project_id) == 0:
                order.sudo().write({'real_estate_project_id': False})
            else:
                project = request.env['real.estate.project'].sudo().browse(int(project_id))
                if project.exists():
                    order.sudo().write({'real_estate_project_id': project.id})

        projects = request.env['real.estate.project'].sudo().search([])
        selected_project = order.real_estate_project_id if order else False

        # Debug temporaire
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(">>> selected_project: %s, status: %s", selected_project, selected_project.status if selected_project else 'none')

        return request.render('real_estate_sale.shop_project_step', {
            'projects': projects,
            'selected_project': selected_project,
            'order': order,
        })