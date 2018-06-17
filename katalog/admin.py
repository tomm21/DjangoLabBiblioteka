from django.contrib import admin

# Register your models here.

from .models import Autor, Gatunek, Ksiazka, InstancjaKsiazki

#admin.site.register(Autor)
admin.site.register(Gatunek)
#admin.site.register(Ksiazka)
#admin.site.register(InstancjaKsiazki)


class AutorAdmin(admin.ModelAdmin):
	list_display = ('nazwisko', 'imie', 'data_urodzenia', 'data_smierci')

admin.site.register(Autor, AutorAdmin)

@admin.register(Ksiazka)
class KsiazkaAdmin(admin.ModelAdmin):
	list_display = ('tytul', 'autor', 'display_gatunek')

@admin.register(InstancjaKsiazki)
class InstancjaKsiazkiAdmin(admin.ModelAdmin):
	list_filter = ('status', 'data_zwrotu')



