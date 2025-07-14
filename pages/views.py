from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, CreateView
from .models import Post
from .forms import PostForm

# 🏠 Vista principal con buscador y destacados
class HomeView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).order_by('-created_at')
        return Post.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_posts'] = Post.objects.order_by('-views')[:5]  # Más leídos
        return context

# ℹ️ Página "Acerca de"
class AboutView(TemplateView):
    template_name = 'pages/about.html'

# 📝 Registro de usuarios
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# 🆕 Crear nuevo post
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/create_post.html'
    success_url = '/pages/'

from django.views.generic.detail import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

from django.views.generic.edit import UpdateView

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/edit_post.html'
    success_url = '/pages/'

from django.views.generic.edit import DeleteView

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'pages/delete_post.html'
    success_url = '/pages/'    

from django.shortcuts import render

# 📚 Vista para mostrar artículos/libros
def articulos_view(request):
    libros = [
        {'titulo': 'Python para principiantes', 'precio': '$25.000'},
        {'titulo': 'Django en acción', 'precio': '$30.000'},
        {'titulo': 'Impuestos y programación', 'precio': '$20.000'},
    ]
    return render(request, 'pages/articulos.html', {'libros': libros})

# 🗞️ Vista para noticias
def noticias_view(request):
    noticias = [
        {'titulo': 'Nueva versión de Django lanzada', 'fecha': '2025-07-01'},
        {'titulo': 'Argentina impulsa educación digital', 'fecha': '2025-06-28'},
        {'titulo': 'Entrevista a desarrollador Django en Buenos Aires', 'fecha': '2025-06-25'},
    ]
    return render(request, 'pages/noticias.html', {'noticias': noticias})

# 📑 Vista para mostrar normas o políticas
def normas_view(request):
    normas = [
        'Respetar a todos los usuarios y autores',
        'No publicar contenido ofensivo ni discriminatorio',
        'Mantener la calidad y claridad de los posts',
        'Citar fuentes externas correctamente',
    ]
    return render(request, 'pages/normas.html', {'normas': normas})

from django.shortcuts import render

# 📚 Artículos / libros simulados
def articulos_view(request):
    libros = [
        {'titulo': 'Python para principiantes', 'precio': '$25.000'},
        {'titulo': 'Django en acción', 'precio': '$30.000'},
        {'titulo': 'Impuestos y programación', 'precio': '$20.000'},
    ]
    return render(request, 'pages/articulos.html', {'libros': libros})

# 🗞️ Noticias simuladas
def noticias_view(request):
    noticias = [
        {'titulo': 'Lanzamiento de Django 5.2', 'fecha': '2025-07-10'},
        {'titulo': 'Argentina impulsa educación digital', 'fecha': '2025-07-07'},
        {'titulo': 'Entrevista con desarrollador Django local', 'fecha': '2025-07-03'},
    ]
    return render(request, 'pages/noticias.html', {'noticias': noticias})

# 📑 Normas del blog
def normas_view(request):
    normas = [
        'Respetar a todos los usuarios y autores.',
        'No publicar contenido ofensivo ni discriminatorio.',
        'Citar correctamente cualquier fuente externa.',
        'Evitar el spam o contenido repetido sin valor.',
    ]
    return render(request, 'pages/normas.html', {'normas': normas})






