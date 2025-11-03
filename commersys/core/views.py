from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def home(request):
    if request.method == "GET":
        return render(request, "core/home.html")
    
def dashboard(request):
    if request.method == "GET":
        return render(request, "core/dashboard.html")

def pedidos(request):
    if request.method == "GET":
        return render(request, "core/pedidos.html")

def produtos(request):
    if request.method == "GET":
        return render(request, "core/produtos.html")

def clientes(request):
    if request.method == "GET":
        return render(request, "core/clientes.html")

def clientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        return render(request, "core/clientes.html", {"clientes": clientes})
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes")