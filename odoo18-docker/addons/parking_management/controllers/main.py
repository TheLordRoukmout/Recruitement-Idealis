from odoo import http
from odoo.http import request


class ParkingController(http.Controller):

    @http.route('/parking', type='http', auth='public', website=True)
    def parking_overview(self, **kwargs):
        places = request.env['parking.place'].sudo().search([], order='name')
        total = len(places)
        available = len(places.filtered(lambda p: p.is_available))
        occupied = total - available

        return request.render('parking_management.parking_overview', {
            'places': places,
            'total': total,
            'available': available,
            'occupied': occupied,
        })