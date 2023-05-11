from django.shortcuts import render
from diet.models import Diet, Review
from training.models import Training, TrainingReview
from forum.models import Post, Comment

def homeView(request):
    review1 = Review.objects.all().order_by('-date').first()
    review2 = TrainingReview.objects.all().order_by('-date').first()

    diets = Diet.objects.all()
    maxcount_diets = 0
    for diet in diets:
        reviews_diet = Review.objects.filter(object=diet).count()
        if(maxcount_diets<reviews_diet):
            maxcount_diets = reviews_diet
            max_diet = diet

    trainings = Training.objects.all()
    maxcount_training = 0
    for training in trainings:
        reviews_training = TrainingReview.objects.filter(object=training).count()
        if(maxcount_training<reviews_training):
            maxcount_training = reviews_training
            max_training = training

    posts = Post.objects.all()
    maxcount_post = 0
    for post in posts:
        reviews_post = Comment.objects.filter(post=post).count()
        if(maxcount_post<reviews_post):
            maxcount_post = reviews_post
            max_post = post

    context = {
        'diet': max_diet,
        'training': max_training,
        'post': max_post,
        'review_diet': review1,
        'review_training': review2,
    }
    return render(request, 'home/index.html', context)
