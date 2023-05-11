from django.views import generic
from .models import Diet, Review
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ReviewForm
from django.core.paginator import Paginator


def indexView(request): 
    p = Paginator(Diet.objects.all().order_by('-date'), 6)
    page = request.GET.get('page')
    diets = p.get_page(page)
    for diet in diets:
        diet.cut_context = diet.context[0:200]
    context = {
        'diets': diets,
    }
    return render(request, 'diet/index.html', context)


def detailView(request, diet_id):
    reviews = Review.objects.filter(object__id=diet_id)
    diet = Diet.objects.get(id=diet_id)
    context = {
        'reviews': reviews,
        'diet': diet,
    }
    return render(request, 'diet/detail.html', context)


def submit_review(request, diet_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = Review.objects.get(author__id=request.user.profile.id, object__id=diet_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except Review.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Review()
                data.context = form.cleaned_data['context']
                data.rating = form.cleaned_data['rating']
                data.object_id = diet_id
                data.author = request.user.profile
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)