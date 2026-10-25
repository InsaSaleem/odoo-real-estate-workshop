from odoo import models,fields
from odoo.exceptions import ValidationError
class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"

    price = fields.Float()
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('rejected', 'Rejected')])

    def accept_offer(self):
        for record in self:
            if record.property_id.state == 'offer_accepted':
                raise ValidationError("This property already has an offer, reject or delete to proceed")
            else:
                record.status = 'accepted'
                record.property_id.write({
                    "buyer_id" : record.partner_id.id,
                    "selling_price" : record.price,
                    "state" : "offer_accepted"
                })

    def refuse_offer(self):
            for record in self:
                if record.status == 'accepted':
                    raise ValidationError("Accepted offers can't be rejected")
                else:
                    record.status = 'rejected'