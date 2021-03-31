from odoo import models, fields
# Se creo un modelo para segmentar a los agentes a los que se les asignara los leads
# El cual agrega un campo nuevo a la tabla res_user
#
# Queda pentiene la funcion que asigna el lead


# Clase creada para segmentar a los agentes a los cuales se les asignan los leads
class GrupoAgentes(models.Model):   
    grupo_agentes = fields.Char(string="grupo de agentes asigna leads", required=True)

class ResUsers(models.Model):
    _inherit = "res.users"
    
    grupo_agentes = fields.Many2one(GrupoAgentes, string="grupo de agentes asigna leads", on_delete=models.CASCADE, required=False)

    
class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, values): # Aqui se agrega el agente asignado al lead
        agente = values.get('user_id')
        
        if agente:
            agente = self.asigna_agente()
        
        return agente

    def asigna_agente(): # Aqui va la funcion que asigna el agente al lead
     
        # Aqui va la funcion que asigna el agente al lead

        return agente