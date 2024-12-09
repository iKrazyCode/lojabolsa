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

    produto_parte = models.CharField(verbose_name='Qual parte esse produto representa', choices=PARTES_CHOICES, max_length=45)
    cor_nome = models.CharField(verbose_name='Nome da Cor', max_length=50)
    cor_hex = models.CharField(verbose_name='Hexadecimal dessa cor', max_length=50, help_text='Ex: #3b2a29')
    product_url = models.URLField(verbose_name='URL completa do produto', max_length=500, unique=True, help_text="Coloque o link do produto. Ex: https://minhaloja.com.br/produtos/bolsa-preta/")
    ativo = models.BooleanField(verbose_name='Produto disponível para compra', default=True)
    
    def __str__(self):
        return f"produto: {self.produto_parte} - cor: {self.cor_nome}"