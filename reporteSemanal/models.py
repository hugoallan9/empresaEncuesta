from django.db import models
import datetime

# Create your models here.

class Reporte(models.Model):
    NO_INICIADO = 'NI'
    EN_PROCESO = 'EP'
    ENTREGADO = 'E'
    EN_REVISION = 'ER'
    FINALIZADO = 'F'
    PRODUCTO1_OP = (
        (NO_INICIADO, 'No iniciado'),
        (EN_PROCESO,'En progreso'),
        (ENTREGADO,'Entregado'),
        (EN_REVISION,'En revisión'),
        (FINALIZADO,'Finalizado'),
    )

    PRODUCTO2_OP = (
        (NO_INICIADO, 'No iniciado'),
        (EN_PROCESO,'En progreso'),
        (ENTREGADO,'Entregado'),
        (EN_REVISION,'En revisión'),
        (FINALIZADO,'Finalizado'),
    )

    PRODUCTO3_OP = (
        (NO_INICIADO, 'No iniciado'),
        (EN_PROCESO,'En progreso'),
        (ENTREGADO,'Entregado'),
        (EN_REVISION,'En revisión'),
        (FINALIZADO,'Finalizado'),
    )

    producto1 = models.CharField(
        max_length = 2,
        choices = PRODUCTO1_OP,
        default = NO_INICIADO
    )


    producto2 = models.CharField(
        max_length = 2,
        choices = PRODUCTO1_OP,
        default = NO_INICIADO
    )


    producto3 = models.CharField(
        max_length = 2,
        choices = PRODUCTO1_OP,
        default = NO_INICIADO
    )

    inicio_semana = models.DateField( default = datetime.date.today)

    MM_CONTRATACION_MUESTRISTA = 0.1
    MM_DIRECTORIO_AGEXPORT = 0.1
    MM_DIRECTORIO_PRONACOM = 0.1
    MM_DIRECTORIO_MINECO = 0.2
    MM_LIMPIAR_INTEGRAR = 0.3
    MM_ESTRATIFICAR = 0.1
    MM_ELABORAR_MUESTRA = 0.1


    C_CONTRATACION_CUESTIONARIOS = 0.1
    C_CUESTIONARIO_TRAVERA = 0.05
    C_PREGUNTAS_SIN_MODIFICACION = 0.3
    C_TRADUCIR_PREGUNTAS = 0.1
    C_ADAPTACION_PREGUNTAS = 0.15
    C_TALLER_INE = 0.2
    C_APARTADO_CONSENTIMIENTO = 0.1

    EC_COORDINADOR_CAMPO = 0.1
    EC_CONTRATACION_CAMPO = 0.15
    EC_ELABORACION_MANUALES = 0.2
    EC_CAPACITACION = 0.2
    EC_SERVICIO_TRANSPORTE = 0.1
    EC_PRUEBA_PILOTO = 0.2

    OC_RUTAS_TIEMPOS = 0.3
    OC_INSUMOS = 0.1
    OC_LEVANTAMIENTO = 0.3
    OC_MONITOREO = 0.3

    DCD_CONTRATACION_IT = 0.1
    DCD_PAUTAS = 0.3
    DCD_BASE_DATOS = 0.3
    DCD_PROGRAMA_CAPTURA = 0.3

    GBM_PLAN_TABULACION = 0.25
    GBM_DEF_SALIDAS = 0.1
    GBM_SALIDA_SCRIPT = 0.05
    GBM_DICCIONARIO = 0.1
    GBM_GENERAR_TABULADOS = 0.2
    GBM_ANALISIS_CONSISTENCIA = 0.3

    contratacion_muestrista = models.IntegerField(default = 0)
    directorio_agexport = models.IntegerField(default = 0)
    directorio_pronacom = models.IntegerField(default = 0)
    directorio_mineco = models.IntegerField(default = 0)
    limpiar_integrar = models.IntegerField(default = 0)
    estratificar = models.IntegerField(default = 0)
    elaborar_muestra = models.IntegerField(default = 0)

    contratacion_experto_cuestionario = models.IntegerField(default = 0)
    obtencion_cuestionario_travera = models.IntegerField(default = 0)
    preguntas_sin_modificacion = models.IntegerField(default = 0)
    traduccion_preguntas = models.IntegerField(default = 0)
    adaptacion_preguntas = models.IntegerField(default = 0)
    taller_validacion_INE = models.IntegerField(default = 0)
    apartado_consentimiento = models.IntegerField(default = 0)

    contratacion_equipo_campo = models.IntegerField(default = 0)
    contratacion_personal_campo = models.IntegerField(default = 0)
    elaboracion_manuales = models.IntegerField(default = 0)
    capacitacion_campo = models.IntegerField(default = 0)
    servicio_transporte = models.IntegerField(default = 0)
    prueba_piloto = models.IntegerField(default = 0)


    contratacion_expertoIT = models.IntegerField(default = 0)
    pautas_consistencia = models.IntegerField(default = 0)
    preparacion_base_datos = models.IntegerField(default = 0)
    programa_captura = models.IntegerField(default = 0)

    elaborar_plan_tabulacion = models.IntegerField(default = 0)
    def_formato_salida = models.IntegerField(default = 0)
    script_salida = models.IntegerField(default = 0)
    diccionario_salida = models.IntegerField(default = 0)
    tabulados = models.IntegerField(default = 0)
    analisis_consistencia = models.IntegerField(default = 0)




