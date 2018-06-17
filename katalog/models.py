from django.db import models
from django.urls import reverse
import uuid 
# Create your models here.
class Gatunek(models.Model):
	nazwa = models.CharField(max_length=200, help_text="Gatunek, kategoria (np. poezja, fantastyka)")
	def __str__(self):
		return self.nazwa

class Ksiazka(models.Model):
	tytul = models.CharField(max_length=200)
	autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True, help_text='Autor tej ksiazki')
	opis = models.TextField(max_length=1000, help_text='Opis ksiazki')
	isbn = models.CharField('ISBN', max_length = 13, help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>')
	gatunek = models.ManyToManyField(Gatunek, help_text='Gatunek tej ksiazki')


	def __str__(self):
		return self.tytul

	def get_absolute_url(self):
		return reverse('ksiazka-detail', args=[str(self.id)])
	
	def display_gatunek(self):
		return ', '.join([ gatunek.nazwa for gatunek in self.gatunek.all()[:3] ])
		display_gatunek.short_description = 'Gat.'

from django.contrib.auth.models import User

class InstancjaKsiazki(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID tej ksiazki")
	ksiazka = models.ForeignKey('Ksiazka', on_delete=models.SET_NULL, null=True)
	wydawca = models.CharField(max_length=200)
	data_zwrotu = models.DateField(null=True, blank=True)
	wypozycza = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	STATUS_WYPOZYCZENIA = (
		('n','Naprawa'),
		('w','Wypozyczona'),
		('d','Dostepna'),
		('z','Zarezerwowana'),
	)

	status = models.CharField(max_length=1, choices=STATUS_WYPOZYCZENIA, blank=True, default='n', help_text='Dostepnosc ksiazki')
	
	class Meta:
		ordering = ['data_zwrotu']

	def __str__(self):
		return '{0} ({1})'.format(self.id, self.ksiazka.tytul)

class Autor(models.Model):
	imie = models.CharField(max_length=100)
	nazwisko = models.CharField(max_length=100)
	data_urodzenia = models.DateField(null=True, blank=True)
	data_smierci = models.DateField('Zmarl', null=True, blank=True)
	class Meta:
		ordering = ["nazwisko","imie"]
	def get_absolute_url(self):
		return reverse('autor-detail', args=[str(self.id)])

	def __str__(self):
		return '{0}, {1}'.format(self.nazwisko, self.imie)
