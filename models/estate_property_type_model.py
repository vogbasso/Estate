from odoo import models,fields

class EstatePropertyType(models.Model):
    _name="estate_property_type.model"
    _description = "La table des types de Estate Property Type"

    name = fields.Char(required=True)
    
