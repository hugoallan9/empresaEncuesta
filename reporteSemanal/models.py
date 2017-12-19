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

    inicio_semana = models.DateField(_("Date"), default = datetime.date.today)