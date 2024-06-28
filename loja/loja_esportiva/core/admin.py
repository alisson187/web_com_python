from django.contrib import admin

# Register your models here.
from .models import Produto, NotaFiscal, Cliente, Fornecedor, Funcionario

admin.site.register(Produto)
admin.site.register(NotaFiscal)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Funcionario)
