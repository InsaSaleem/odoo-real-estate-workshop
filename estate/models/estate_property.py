#Odoo Model: Basically it is the SQL Table in backend

from odoo import models,fields,api
from odoo.exceptions import UserError

class EstateProperty(models.Model): #enable the odoo ORM (Object Relational Mapping)
    _name='estate.property' #SQL Table Name

    name = fields.Char(required=True) #char is a single line entry
    description = fields.Text() #Text is a multi line entry
    date_available = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    garden_area = fields.Integer()



    total_area = fields.Integer(compute="_compute_total_area")

    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    property_type_id = fields.Many2one("estate.property.type")
    tags_id = fields.Many2many("estate.property.tag")
    sales_person_id = fields.Many2one("res.users", string="SalesPerson")
    buyer_id = fields.Many2one("res.partner", string="Buyer")


    state = fields.Selection(selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], default = 'new' , required=True)



    def sell_property(sell):
     for record in sell:
        if record.state == 'canceled':
           raise UserError('Canceled properties cannot be sold')
        else:
           record.state = 'canceled'

    def cancel_property(sell):
         for record in sell:
            if record.state == 'sold':
               raise UserError('Sold properties cannot be canceled')
            else:
               record.state = 'sold'      
    offer_id = fields.One2many('estate.property.offer', 'property_id')
    _check_expected_price = models.Constraint(
        'CHECK(expected_price > 0)',
        'The expected price must be positive',
    )

    _check_selling_price = models.Constraint(
        'CHECK(selling_price >= 0)',
        'The selling price must be positive',
    ) # we are only limiting s.p to not be negative
    