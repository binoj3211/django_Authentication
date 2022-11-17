from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import ImageForm
from myapp.models import User
from myapp.forms import CustomUserCreationForm


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'myapp/userpage.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'myapp/main.html', {'form': form})    


def home(request):
    count = User.objects.count()
    return render(request, "myapp/home.html", {"count": count})
def main(request):
    count = User.objects.count()
    return render(request, "myapp/main.html", {"count": count})

def signup(request):
    if request.method == "POST":
        form =CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def secret_page(request):
    return render(request, "myapp/secret_page.html")


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = "myapp/secret_page.html"






