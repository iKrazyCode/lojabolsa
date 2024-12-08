from django.db import models

# Create your models here.
class Produto(models.Model):
    """
    Model responsável por armazenar as cores que terão disponíveis para escolha
    """

    PARTES_CHOICES = [
        ('frente', 'Frente'),
        ('atras', 'Atras'),
        ('alca', 'Alça'),
        ('transversal', 'Transversal')
    ]

    produto_nome = models.CharField(verbose_name='Nome do produto', max_length=130)
    produto_parte = models.CharField(verbose_name='Qual parte esse produto representa', choices=PARTES_CHOICES, max_length=45)
    cor_nome = models.CharField(verbose_name='Nome da Cor', max_length=50)
    cor_hex = models.CharField(verbose_name='Hex dessa cor', max_length=50)
    product_url = models.URLField(verbose_name='URL completa do produto', max_length=500, unique=True)
    ativo = models.BooleanField(verbose_name='Produto disponível para compra', default=True)
    
    def __str__(self):
        return f"produto: {self.nome} - cor: {self.cor_nome}"