from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Trainer
from .forms import ClientForm, TrainerForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'gym/client_list.html', {'clients': clients})

def client_add(request):
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientForm()
    return render(request, 'gym/client_edit.html', {'form': form, 'title': 'Додати клієнта'})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientForm(instance=client)
    return render(request, 'gym/client_edit.html', {'form': form, 'client': client})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'gym/trainer_list.html', {'trainers': trainers})

# НОВА ФУНКЦІЯ: ДОДАТИ ТРЕНЕРА
def trainer_add(request):
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    else:
        form = TrainerForm()
    return render(request, 'gym/trainer_edit.html', {'form': form})

# НОВА ФУНКЦІЯ: ТОП 5 ЗІРОК
def top_trainers(request):
    # Фільтруємо лише тренерів з рейтингом 5
    top_list = Trainer.objects.filter(rating=5)
    return render(request, 'gym/top_trainers.html', {'top_list': top_list})