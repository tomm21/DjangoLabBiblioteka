from django.shortcuts import render

# Create your views here.

from .models import Autor, Gatunek, Ksiazka, InstancjaKsiazki

def index(request):
	num_ks=Ksiazka.objects.all().count()
	num_in=InstancjaKsiazki.objects.all().count()
	num_in_d=InstancjaKsiazki.objects.filter(status__exact='d').count()
	num_au=Autor.objects.count()
	
	return render(
		request,
		'index.html',
		context={'num_ks':num_ks,'num_in':num_in,'num_in_d':num_in_d,'num_au':num_au}
	)


from django.views import generic

class AutorListView(generic.ListView):
	model = Autor

class KsiazkaListView(generic.ListView):
	model = Ksiazka
	context_object_name = 'moja_ksiazka_list'
	#queryset = Ksiazka.objects.filter(tytul__icontains =' ')[:5]
	template_name = 'katalog/ksiazka_moja_list.html'
	paginate_by = 3
class KsiazkaSzczegolView(generic.DetailView):
	model = Ksiazka
