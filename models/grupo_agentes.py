from odoo import models, fields
# Modulo para asignar automaticamente leads a agentes de ventas
#
# Se creo un modelo para segmentar a los agentes  que se les asignara 
# leads el cual agrega un campo nuevo a la tabla res_user "grupo_agentes"
#
# Queda pentiene:
# -Crear los grupo_agentes en la bdd y asignar los agentes a estos grupos 
#  (Los agentes estan en el excel)
# -La funcion que asigna el lead
# -Corregir errores en los modelos
#
# Estructura:
# -Clase Modelo GrupoAgentes
# -Clase Acciones al crear lead
# -Clases con datos de dias festivos (Para calcular la asignacion del lead)
#--------------------------------------------------------------------------


# -Clase Modelo GrupoAgentes
# Clase creada para segmentar a los agentes a los cuales se les asignan los leads
class GrupoAgentes(models.Model):   
    grupo_agentes = fields.Char(string="grupo de agentes asigna leads", required=True)

class ResUsers(models.Model):
    _inherit = "res.users"
    
    grupo_agentes = fields.Many2one(GrupoAgentes, string="grupo de agentes asigna leads", on_delete=models.CASCADE, required=False)
#-----------------------------------------------------------

# -Clase Acciones al crear lead    
class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, values): # Aqui se agrega el agente asignado al lead
        agente = values.get('user_id')
        global localidad = values.get('country_id')

        if agente:
            agente = self.asigna_agente()
        
        return agente

    def asigna_agente(localidad): # Aqui va la funcion que asigna el agente al lead
     
        # Aqui va la funcion que asigna el agente al lead

        return agente
#-----------------------------------------------------------

# -Clases con datos de dias festivos (Para calcular la asignacion del lead)
# España
class EsBusinessCalendar(AbstractHolidayCalendar):
   rules = [
     Holiday('Año Nuevo', month=1, day=1),
     Holiday('Epifanía del Señor', month=1, day=6),
     Holiday('Viernes Santo', month=4, day=2),
     Holiday('Día del Trabajador', month=5, day=1),
     Holiday('Asunción de la Virgen', month=8, day=15),
     Holiday('Día de la Hispanidad', month=10, day=12),
     Holiday('Todos los Santos', month=11, day=1),
     Holiday('Día Constitución', month=12, day=6),
     Holiday('Inmaculada Concepción', month=12, day=8),
     Holiday('Navidad', month=12, day=25)
   ]
# Mexico
class EsBusinessCalendar2(AbstractHolidayCalendar):
   rules = [
     Holiday('Año Nuevo', month=1, day=1),
     Holiday('Día de la Constitución Mexicana', month=2, day=1),
     Holiday('Natalicio de Benito Juárez', month=3, day=15),
     Holiday('Domingo de Resurreción', month=4, day=4),
     Holiday('Día del Trabajador', month=5, day=1),
     Holiday('Día de la Independencia', month=9, day=16),
     Holiday('Revolución Mexicana', month=11, day=15),
     Holiday('Navidad', month=12, day=25)
   ]
# Colombia
class EsBusinessCalendar3(AbstractHolidayCalendar):
   rules = [
     Holiday('Año Nuevo', month=1, day=1),
     Holiday('Día de los Reyes Magos', month=1, day=11),
     Holiday('Día de San José', month=3, day=22),
     Holiday('Jueves Santo', month=4, day=1),
     Holiday('Viernes Santo', month=4, day=2),
     Holiday('Día del Trabajador', month=5, day=1),
     Holiday('Día de la Ascensión', month=5, day=17),
     Holiday('Corpus Cristi', month=6, day=7),
     Holiday('Sagrado Corazón', month=6, day=14),
     Holiday('San Pedro y San Pablo', month=7, day=5),
     Holiday('Día de la Independencia', month=7, day=20),
     Holiday('Batalla de Boyacá', month=8, day=7),
     Holiday('La asunción de la Virgen', month=8, day=16),
     Holiday('Día de la Raza', month=10, day=18),
     Holiday('Día de los Difuntos', month=11, day=1),
     Holiday('Independencia de Cartagena', month=11, day=15),
     Holiday('Día de la Inmaculada Concepción', month=12, day=8),
     Holiday('Navidad', month=12, day=25)
   ]
# El Salvador
class EsBusinessCalendar4(AbstractHolidayCalendar):
   rules = [
     Holiday('Año Nuevo', month=1, day=1),
     Holiday('Jueves Santo', month=4, day=1),
     Holiday('Viernes Santo', month=4, day=2),
     Holiday('Sábado Santo', month=4, day=3),
     Holiday('Domingo Santo', month=4, day=4),
     Holiday('Día del Trabajador', month=5, day=1),
     Holiday('Día de la Madre', month=5, day=10),
     Holiday('Día del Padre', month=6, day=17),
     Holiday('Fiestas de San Salvador', month=8, day=5),
     Holiday('Celebración del Divino Salvador del Mundo', month=8, day=6),
     Holiday('Día de la Independencia', month=9, day=15),
     Holiday('Día de los Difuntos', month=11, day=2),
     Holiday('Navidad', month=12, day=25)
   ]
# Nicaragua
class EsBusinessCalendar5(AbstractHolidayCalendar):
   rules = [
     Holiday('Año Nuevo', month=1, day=1),
     Holiday('Jueves Santo', month=4, day=1),
     Holiday('Viernes Santo', month=4, day=2),
     Holiday('Domingo Santo', month=4, day=4),
     Holiday('Día del Trabajador', month=5, day=1),
     Holiday('Día de la Revolución', month=7, day=19),
     Holiday('Traída de Santo Domingo de Guzmán', month=8, day=1),
     Holiday('Dejada de Santo Domingo de Guzmán', month=8, day=10),
     Holiday('Batalla de San Jacinto', month=9, day=14),
     Holiday('Independencia de Nicaragua', month=9, day=15),
     Holiday('Inmaculada Concepción de María', month=12, day=8),
     Holiday('Navidad', month=12, day=25)
   ]