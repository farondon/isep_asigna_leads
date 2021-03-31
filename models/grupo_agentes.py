from odoo import models, fields


class CrmLead(models.Model):
    _inherit = "crm.lead"
    
    grupo_agentes_venta = fields.Char(string="grupo de agentes asigna leads", required=False)
    