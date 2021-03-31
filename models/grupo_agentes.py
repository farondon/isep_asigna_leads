from odoo import models, fields


class ResUsers(models.Model):
    _inherit = "res.users"
    
    grupo_agentes_venta = fields.Char(string="grupo de agentes asigna leads", required=False)
    