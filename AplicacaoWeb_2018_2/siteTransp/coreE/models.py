# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# #
# # Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# # into your database.
# from __future__ import unicode_literals

# from django.db import models


# class Empenho(models.Model):
#     Especie = models.CharField(db_column='Especie', max_length=25)  # Field name made lowercase.
#     Orgao = models.CharField(db_column='Orgao', max_length=100)  # Field name made lowercase.
#     Projeto = models.CharField(db_column='Projeto', max_length=100)  # Field name made lowercase.
#     Elemento = models.CharField(db_column='Elemento', max_length=100)  # Field name made lowercase.
#     Licitacao = models.CharField(db_column='Licitacao', max_length=50)  # Field name made lowercase.
#     Processo = models.CharField(db_column='Processo', max_length=30)  # Field name made lowercase.
#     Dataempenho = models.DateField(db_column='DataEmpenho')  # Field name made lowercase.
#     Valor = models.DecimalField(db_column='Valor', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     Empenho_Numero = models.IntegerField(db_column='Empenho_Numero')  # Field name made lowercase.
#     IdFavorecido = models.ForeignKey('Favorecido', db_column='IdFavorecido')  # Field name made lowercase.
#     Funcao = models.CharField(db_column='Funcao', max_length=100)  # Field name made lowercase.
#     Subfuncao = models.CharField(db_column='SubFuncao', max_length=100)  # Field name made lowercase.
#     Programa = models.CharField(db_column='Programa', max_length=100)  # Field name made lowercase.
#     Destinacao = models.CharField(db_column='Destinacao', max_length=45)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Empenho'
#         unique_together = (('Empenho_Numero', 'IdFavorecido'),)


# class Favorecido(models.Model):
#     IdFavorecido = models.AutoField(db_column='IdFavorecido', primary_key=True)  # Field name made lowercase.
#     CPF_CNPJ = models.CharField(db_column='CPF_CNPJ', max_length=20)  # Field name made lowercase.
#     Nome = models.CharField(db_column='Nome', unique=True, max_length=100)  # Field name made lowercase.
#     Cargo = models.CharField(db_column='Cargo', max_length=45, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Favorecido'


# class Pagamento(models.Model):
#     Numero = models.IntegerField(db_column='Numero')  # Field name made lowercase.
#     DataPagamento = models.DateField(db_column='DataPagamento')  # Field name made lowercase.
#     ValorPagamento = models.DecimalField(db_column='ValorPagamento', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     Empenho_Numero = models.ForeignKey(Empenho, db_column='Empenho_Numero')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Pagamento'
#         unique_together = (('Numero', 'Empenho_Numero'),)


