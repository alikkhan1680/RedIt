from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, TemplateView, CreateView, DetailView, View
from .models import *
from .forms import *


# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = BlogModel
    context_object_name = 'blog'

    paginate_by = 1


class BlogView(ListView):
    template_name = 'blog.html'
    context_object_name = 'blog'

    def get_queryset(self):
        if self.request.GET.get('search'):
            query = self.request.GET.get('search')
            blg = BlogModel.objects.filter(
                Q(title__icontains=query) |
                Q(category__cat_name__icontains=query) |
                Q(tag__tag__icontains=query)
            )
            return blg

        else:
            return BlogModel.objects.all()

    paginate_by = 3


class BlogSingleView(DetailView):
    template_name = 'blog-single.html'
    model = BlogModel
    context_object_name = 'blog'

    def post(self, request, pk):
        blg = BlogModel.objects.get(id=pk)
        form = MessageForm()

        if request.method == 'POST':
            form = MessageForm(request.POST or None)
            if form.is_valid():
                msg = form.save(commit=False)
                msg.user = request.user
                msg.blog = blg
                msg.save()

                return redirect('blog_single', pk)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['cat'] = Category.objects.all()[:8]
        contex['resblog'] = BlogModel.objects.all()[:3]
        contex['tag'] = Tag.objects.all()
        contex['message'] = Message.objects.filter(blog=self.object)
        contex['form'] = MessageForm

        return contex


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(CreateView):
    template_name = 'contact.html'
    model = ContactModel
    form_class = ContactForms


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        user = authenticate(request,
                            username=request.POST.get('username'),
                            password=request.POST.get('password'),
                            )
        if user is not None:
            login(request, user)
            return redirect('home')
        message = 'Login Failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


def logout_user(request):
    logout(request)

    return redirect('login')


class RegisterView(TemplateView):
    template_name = 'register.html'
    form_class = RegistrationForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self,request):
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        message = 'Registration Failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})

