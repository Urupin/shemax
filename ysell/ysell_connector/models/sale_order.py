from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ysell_delivery_status = fields.Char(string="Ysell Delivery Status")
    ysell_order_id = fields.Char(string="Ysell Order ID")

    @api.model
    def create(self, vals):
        order = super().create(vals)
        if order.warehouse_id.name == 'ShemaxGlobal':
            success = self.env['ysell.client'].check_stock(order)
            if success:
                order.state = 'sent'
            else:
                raise UserError("Недостаточно товара на складе ShemaxGlobal")
        return order

    def action_sent_to_sale(self):
        for order in self:
            if order.state == 'sent' and order.warehouse_id.name == 'ShemaxGlobal':
                success = self.env['ysell.client'].send_delivery(order)
                if success:
                    order.state = 'sale'
                else:
                    order.state = 'sent'

    @api.model
    def _cron_update_ysell_delivery_status(self):
        orders = self.search([('state', '=', 'sale'), ('ysell_delivery_status', '!=', 'full'), ('warehouse_id.name', '=', 'ShemaxGlobal')])
        for order in orders:
            status = self.env['ysell.client'].update_delivery_status(order)
            order.ysell_delivery_status = status