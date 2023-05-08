from django.shortcuts import render, redirect
from pessoas.models import Pessoa

# OK
def home(request):
    dsPessoas = Pessoa.objects.all()
    return render(request, 'assets/index.html', {'dsPessoas': dsPessoas})

# OK
def editar(request, pessoa_id):
    pessoas = Pessoa.objects.get(id=pessoa_id)
    return render(request, 'assets/update.html', {"pessoas": pessoas})

# OK
def update(request, update_id):
    pnome = request.POST.get("nome")
    pidade = request.POST.get("idade")
    pcpf = request.POST.get("cpf")

    pessoas = Pessoa.objects.get(id=update_id)

    pessoas.nome = pnome
    pessoas.idade = pidade
    pessoas.cpf = pcpf
    pessoas.save()

    return redirect(home)

# OK
def salvar(request):
    pnome = request.POST.get("nome")
    pidade = request.POST.get("idade")
    pcpf = request.POST.get("cpf")

    Pessoa.objects.create(nome=pnome, idade=pidade, cpf=pcpf)

    dsPessoas = Pessoa.objects.all()
    return render(request, "assets/index.html", {"pessoas": dsPessoas})

# OK
def remover(request, remover_id):
    pessoa = Pessoa.objects.get(pk=remover_id)
    pessoa.delete()
    return redirect(home)
