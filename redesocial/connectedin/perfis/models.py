from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length = 255 , null = False)
    email = models.CharField(max_length = 255 , null = False)
    telefone = models.CharField(max_length = 15 , null = False)
    nome_empresa = models.CharField(max_length = 255 , null = False)

    def convidar(self , perfil_convidado):
        Convite(solicitante = self, convidado = perfil_convidado).save()

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.PROTECT , related_name = 'convites feitos+')
    convidado = models.ForeignKey(Perfil, on_delete=models.PROTECT , related_name = 'convites recebidos+')