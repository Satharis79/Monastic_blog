from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.detail import DetailView 
from django.views.generic import UpdateView
from .forms import SignUpForm
from .models import Monk

class MonkView(DetailView):
    queryset = Monk.objects
    template_name = 'main/profile.html'

class MonkUpdateView(UpdateView):
    model = Monk
    fields = ['first_name', 'city_of_origin', 'title', 'userpic', 'is_literate', 'is_ordained', 'about']
    template_name = 'main/update.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):                
        pk = self.request.user.id
        return reverse('profile', args=[pk])

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)        
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

def monk_list(request):
    monks = Monk.objects.order_by('first_name')    
    return render(request, 'main/monastery.html', {'monks':monks})