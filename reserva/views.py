from gc import get_objects
from django.shortcuts import HttpResponseRedirect, redirect
import json
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from . models import Reserva
from cliente.models import Cliente

# Create your views here.

def index(request):
    return render(request, 'escolha.html')


def cadastrarReserva(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    user = request.user.id

    reservas = Reserva.objects.all().order_by('data')
    reservas_list = [
        {'mesa': reserva.mesa, 'data': reserva.data.strftime('%Y-%m-%d')}
        for reserva in reservas
    ]
    reservas_json = json.dumps(reservas_list)
    context = {
        'reservas': reservas_json,
        'id': user,
    }
    
    if request.method == "POST":
        
        cliente_id = int(request.POST.get('cliente'))
        mesa = request.POST.get('mesa')
        data = request.POST.get('data')

        reserva = Reserva(id_cliente=cliente_id, mesa=mesa, data=data)

        print(reserva)
        reserva.save()
        return HttpResponseRedirect(reverse('reservas-clientes'))
     
    return render(request, 'pagina-realiza-reserva.html', context)

def minhas_reservas(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    nome_usuario = request.user.username
    user = request.user.id
    reservas = Reserva.objects.filter(id_cliente=user).order_by('data')
    context = {
        'reservas': reservas,
        'nome': nome_usuario
    }
    return render(request, 'consultar-reserva.html', context)

def deleteReservation(request, reserva_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    
    user = request.user.id
    reserva = get_object_or_404(Reserva, id=reserva_id, id_cliente=user)
    reserva.delete()
    return HttpResponseRedirect(reverse('reservas-clientes'))

def reservasRestaurante(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    if not request.user.is_staff:
        return HttpResponseForbidden('You need staff privileges to access this page.')
    reservas = Reserva.objects.all()
    return render(request, 'consultar-reserva-restaurante.html', {'reservas': reservas})

def deleteReservaRestaurante(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    reservas = Reserva.objects.all()
    return HttpResponseRedirect(reverse('reservas-restaurante'))
