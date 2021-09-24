from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name="estate_property_tag.model"
    _description = "La table des tags de estate property"

    name = fields.Char(required=True)
    
