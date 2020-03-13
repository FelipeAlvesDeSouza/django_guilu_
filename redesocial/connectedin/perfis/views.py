from django.shortcuts import render , redirect
from perfis.models import Perfil , Convite
def index(request):
    return render(request,'index.html' , {'perfis' : Perfil.objects.all()})

def exibir(request , perfil_id):
    perfil = Perfil.objects.get(id = perfil_id)
    return render(request , 'perfil.html' , {'perfil' : perfil , 'ja_eh_contato' : ja_eh_contato})

def convidar(request , perfil_id):
    perfil_a_convidar = Perfil.objects.get(id = perfil_id)
    return redirect('index')

def aceitar(request,convite_id):
    convite = Convite.objects.get(id = convite_id)
    convite.aceitar()
    return redirect('index')
    
