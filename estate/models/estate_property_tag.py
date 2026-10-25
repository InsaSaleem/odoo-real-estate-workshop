from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"

    name = fields.Char(required=True)
    color = fields.Integer("Color")

    _check_tag_name = models.Constraint(
    'UNIQUE(name)',
    'The name must be different',
)