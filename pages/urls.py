from django.urls import path
from .views import (
    HomeView, AboutView, SignUpView,
    CreatePostView, PostDetailView,
    PostUpdateView, PostDeleteView,
    articulos_view, noticias_view, normas_view
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),                     # /pages/
    path('about/', AboutView.as_view(), name='about'),            # /pages/about/
    path('signup/', SignUpView.as_view(), name='signup'),         # /pages/signup/
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # /pages/3/
    path('crear/', CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='edit_post'),   # /pages/3/editar/
    path('<int:pk>/eliminar/', PostDeleteView.as_view(), name='delete_post'), # /pages/3/eliminar/
    path('articulos/', articulos_view, name='articulos'),
    path('noticias/', noticias_view, name='noticias'),
    path('normas/', normas_view, name='normas'),
]




