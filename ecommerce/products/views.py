from django.shortcuts import render, Http404

# Create your views here.

from .models import Product

def home(request):
	products = Product.objects.all()	
	template = 'products/home.html'
	context = {'products': products}
	return render(request, template, context)


def all(request):
	products = Product.objects.all()
	template = 'products/all.html'
	context = {'products': products}
	return render(request, template, context)


def single(request, slug):
	try:
		product = Product.objects.get(slug=slug)
		images = product.productimage_set.all()
		template = 'products/single.html'
		context = {'product': product, 'images': images}
		return render(request, template, context)
	except:
		raise Http404

def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:	
		products = Product.objects.filter(title__icontains=q)
		template = 'products/results.html'
		context = {'query': q, 'products': products}
	else:
		template = 'home.html'
		context = {}
	
	return render(request, template, context)