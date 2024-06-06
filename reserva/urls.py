from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='reserva'),
    path('realizar-reserva', views.cadastrarReserva, name='realizar-reserva'),
    path('minhas-reservas', views.minhas_reservas, name= 'reservas-clientes'),
    path('consultar-reserva/<int:reserva_id>/', views.deleteReservation, name= 'excluir'),
    path('consultar-reserva-restaurante/', views.reservasRestaurante, name='reservas-restaurante'),
    path('consultar-reserva-restaurante/consultar-reserva-restaurante/<int:reserva_id>/', views.deleteReservaRestaurante, name='delete')
]