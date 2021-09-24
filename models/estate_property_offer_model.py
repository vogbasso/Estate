from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate_property_offer.model"
    _description = "La table Estate property Offer"

    price = fields.Float()
    status = fields.Selection(copy=False,selection=[('Accepted','Accepted'), ('Refused','Refused')])
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("estate_property.model",required=True)