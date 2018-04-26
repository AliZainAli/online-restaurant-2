from django.http import Http404
from  .models import Profile, Category, Item , Order
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate , login
from django.views import generic
from django.views.generic import View
from .forms import SignUpForm


class IndexView(generic.ListView) :
    template_name = 'res/index.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()


def detail(request, category_name):
    try:
        category = Category.objects.get(category_title = category_name)
        all_categories = Category.objects.all()
        items = category.items.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    return render(request, 'res/menu.html', {'items': items,'all_categories': all_categories})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'res/login.html')
    else:
        return render(request, 'res/home.html')



def reg(request):
    return render(request, 'res/registration.html', {})





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.mobile = form.cleaned_data.get('mobile')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('res:menu')
    else:
        form = SignUpForm()
    return render(request, 'res/registration.html', {'form': form})