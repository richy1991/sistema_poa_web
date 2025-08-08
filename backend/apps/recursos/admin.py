from django.contrib import admin
from .models import TipoIndicador, PartidasPresupuestarias, Indicadores, ItemsPOA, EjecucionPresupuestaria

admin.site.register(TipoIndicador)
admin.site.register(PartidasPresupuestarias)
admin.site.register(Indicadores)
admin.site.register(ItemsPOA)
admin.site.register(EjecucionPresupuestaria)
