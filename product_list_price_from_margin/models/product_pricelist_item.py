###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    base = fields.Selection(
        selection_add=[('variant_lst_price', 'Variant price list')],
    )
