from django.db import models

class M_kom(models.Model):
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)

  class Meta:
    abstract = True


class M_famille(M_kom):#Catégorie des Aliments
  name = models.CharField('Nom de la famille', max_length=50)

  class Meta:
    ordering = ['name']
    db_table='famille'
    verbose_name = 'famille'
    verbose_name_plural = 'familles'

  def __str__(self):
    return self.name


class M_categorie(M_kom):#Aliments
  name = models.CharField("Nom de la catégorie", max_length=100)
  famille = models.ForeignKey(M_famille, on_delete=models.SET_NULL, related_name = 'categories', verbose_name="Famille de la catégorie", null=True, blank=True)

  class Meta:
    ordering = ['name']
    db_table='categorie'
    verbose_name = 'categorie'
    verbose_name_plural = 'categories'

  def __str__(self):
    return self.name

class M_aliment(M_kom):#Aliments
  name = models.CharField("Nom de l'aliment", max_length=100)
  categorie = models.ForeignKey(M_categorie, on_delete=models.SET_NULL, related_name = 'aliments', verbose_name="Catégorie de l'aliment", null=True, blank=True)

  class Meta:
    ordering = ['name']
    db_table='aliment'
    verbose_name = 'aliment'
    verbose_name_plural = 'aliments'

  def __str__(self):
    return self.name
    # return self.name + ' / ' + str(self.categorie) + ' / ' + str(self.categorie.famille)
