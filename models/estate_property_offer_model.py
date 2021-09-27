from odoo import api, models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate_property_offer.model"
    _description = "La table Estate property Offer"

    price = fields.Float()
    status = fields.Selection(copy=False,selection=[('Accepted','Accepted'), ('Refused','Refused')])
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("estate_property.model",required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline")


    @api.depends("create_date","validity")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.validity +record.create_date
    
    def _inverse_date_deadline(self):
        for record in self:
            record.validity = record.date_dealine - record.create_date
