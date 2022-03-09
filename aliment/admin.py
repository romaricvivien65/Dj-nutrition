from django.contrib import admin
from .models import M_famille, M_aliment, M_categorie

class familleAdmin(admin.ModelAdmin):
  list_display = ('name', 'Catégories')

  def Catégories(self, obj: M_famille) -> str:
    f = M_famille.objects.get(id=obj.id)
    n = f.categories.count()
    return f'{n}'

class categorieAdmin(admin.ModelAdmin):
  list_display = ('name', 'famille', 'Aliments')

  def Aliments(self, obj: M_categorie) -> str:
    p = M_categorie.objects.get(id=obj.id)
    n = p.aliments.count()
    return f'{n}'


class alimentAdmin(admin.ModelAdmin):
  list_display = ('name', 'categorie')


admin.site.register(M_famille, familleAdmin)
admin.site.register(M_categorie, categorieAdmin)
admin.site.register(M_aliment, alimentAdmin)
