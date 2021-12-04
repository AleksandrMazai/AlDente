from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import Contact, CategoryPortfolio, Portfolio
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = ContactForm()

    portfolio = Portfolio.objects.all()
    categoryportfolio = CategoryPortfolio.objects.all()

    data = {
        'form': form,
        'portfolio': portfolio,
        'categoryportfolio': categoryportfolio
    }

    return render(request, 'index.html', data)


