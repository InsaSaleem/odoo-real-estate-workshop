from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"

    name = fields.Char(required=True)

    _check_type_name = models.Constraint(
        'UNIQUE(name)',
        'The name must be different',
    )