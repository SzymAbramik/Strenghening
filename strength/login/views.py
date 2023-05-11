from token import RIGHTSHIFTEQUAL
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from diet.models import Diet, Review
from training.models import Training, TrainingReview
from forum.models import Post, Comment
from array import *


def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account ' + username + ' created successfully')
            return redirect('login:login')

    context = {'form':form}
    return render(request, 'login/register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login:login')


def profilePage(request, slug):
    post_array = []
    profile = Profile.objects.get(slug=slug)
    trainings = Training.objects.filter(author=profile.user)
    diets = Diet.objects.filter(author=profile.user)
    posts = Post.objects.filter(author=profile)
    diet_reviews = Review.objects.filter(author=profile).count()
    training_reviews = TrainingReview.objects.filter(author=profile).count()
    comments = Comment.objects.filter(author=profile).count()
    overall_reviews = diet_reviews + training_reviews

    for post in posts:
        post.number = Comment.objects.filter(post=post).count()

    for diet in diets:
        diet.number = Review.objects.filter(object=diet).count()

    for training in trainings:
        training.number = TrainingReview.objects.filter(object=training).count()

    context = {
        'profile': profile,
        'trainings': trainings,
        'diets': diets,
        'posts': posts,
        'comments': comments,
        'reviews': overall_reviews,
        'post_array': post_array,
    }
    return render(request, 'login/profile.html', context)
