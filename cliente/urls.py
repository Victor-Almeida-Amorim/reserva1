from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('cadastrar', views.cadastro, name='cadastrar'),
    path('consultar', views.consultar, name='consultar'),
    path('consultar/<int:id>/', views.excluir, name='excluir'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name='logout'),
    path('escolha-super', views.escolhaSuper, name='escolha-super'),
    path('reset_password/', views.reset_password, name='reset_password')

]