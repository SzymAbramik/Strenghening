from .models import Training, TrainingReview
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ReviewForm
from django.core.paginator import Paginator


def indexView(request): 
    p = Paginator(Training.objects.all().order_by('-date'), 6)
    page = request.GET.get('page')
    trainings = p.get_page(page)
    for training in trainings:
        training.cut_context = training.context[0:200]
    context = {
        'trainings': trainings,
    }
    return render(request, 'training/index.html', context)


def detailView(request, training_id):
    reviews = TrainingReview.objects.filter(object__id=training_id)
    training = Training.objects.get(id=training_id)
    context = {
        'reviews': reviews,
        'training': training,
    }
    return render(request, 'training/detail.html', context)


def submit_review(request, training_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = TrainingReview.objects.get(author__id=request.user.profile.id, object__id=training_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except TrainingReview.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = TrainingReview()
                data.context = form.cleaned_data['context']
                data.rating = form.cleaned_data['rating']
                data.object_id = training_id
                data.author = request.user.profile
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)