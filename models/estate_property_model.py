from odoo import api, models, fields

class EstateProperty(models.Model):
    _name = "estate_property.model"
    _description = "La table Estate property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default = lambda self : fields.Datetime.now())
    excepted_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False,readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Type',selection=[('North','North'),('South','South'),('East','East'),('West','West')])
    active = fields.Boolean(default=True)
    state = fields.Selection(default='New',required=True,copy=False,selection=[('New','New'),('Offer received', 'Offer received'), ('Offer accepted','Offer accepted'),('Sold','Sold'),('Canceled','Canceled')])
    property_type_id = fields.Many2one("estate_property_type.model",string="Type de propriétés",required=True)
    buyer_id=fields.Many2one("res.partner",required=True,copy=False,string="Acheteur")
    salesperson_id=fields.Many2one("res.users",required=True,default= lambda self:self.env.user,string="Vendeur")
    tag_ids = fields.Many2many("estate_property_tag.model", string="Tags Property")
    offer_ids = fields.One2many("estate_property_offer.model","property_id")
    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Integer(compute="_compute_best_price_offer")

    @api.depends("garden_area","living_area")
    def _compute_total_area (self):
        for record in self:
            record.total_area = record.garden_area + record.living_area
    
    @api.depends("offer_ids.price")
    def _compute_best_price_offer (self):
        for record in self:
            record.best_price = max(offer.price.mapped('amount_currency') for offer in record.offer_ids)