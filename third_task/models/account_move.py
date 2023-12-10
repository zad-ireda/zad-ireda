from odoo import models, fields, api
from odoo.exceptions import RedirectWarning, UserError, ValidationError


class accounMoveInherit(models.Model):
    _inherit = 'account.move'

    account_move_discount = fields.Float(
        related='invoice_line_ids.discountt_inherit',
        readonly=True,
        store=True
    )
    
    @api.model
    def create(self, vals):
        move = super().create(vals)

        # Check if discount is applicable
        if move.partner_id.allowed_discount > 0:
            # Get configuration parameter values
            allowed_discount_product_id = int(
                self.env["ir.config_parameter"].sudo().get_param(
                    "third_task.allowed_discount_productt_id"
                )
            )
            allowed_discount_account_id = int(
                self.env["ir.config_parameter"].sudo().get_param(
                    "third_task.Allowed_discount_accountt_id"
                )
            )
            product = self.env["product.product"].sudo().browse(
                allowed_discount_product_id
            )

            # Create discount line
            discount_line = self.env["account.move.line"].create({
                "move_id": move.id,
                "name": "discount",
                "amount_currency": 0,
                "debit": move.account_move_discount,
                'price_unit':move.account_move_discount,
                "credit": 0,
                "product_id": product.id,
                "account_id": allowed_discount_account_id,
            })

            # Update existing lines
            for line in move.line_ids:
                if line.id != discount_line.id and line.debit != 0:
                    line.update({"debit": line.debit - self.account_move_discount})

        return move