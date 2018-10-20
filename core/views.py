from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from .models import *

def cadastro(request):#criando a conexão  da pagina cadastro 
    if request.method == 'GET':
        return render(request, 'cadastroPessoa.html', context = { 'title':'Cadastro - Find A Way',})
    elif request.method == 'POST':
        if request.POST.get('login')and request.POST.get('senha'):
            user = Usuario()
            user.login =  request.POST.get('login')
            user.senha= request.POST.get('senha')
            user.email =  request.POST.get('email')
            user.senha= request.POST.get('senha')
            user.celular=  request.POST.get('celular')
           

            print(user)
            user.save()
            print(user)
            return render(request,'cadastroPessoa.html', context = { 'title':'Cadastro - Find A Way',})
        else:
            return render(request,'cadastroPessoa.html', context = { 'title':'Cadastro - Find A Way',})

    return render(request,'cadastroPessoa.html')
def index(request):
    return render(request,'index.html',  context = { 'title':'Find A Way',})

def login(request):
    return render(request, 'login.html', context = {'title':'Login - Find A Way'})

def sobre(request):
    return render(request, 'sobre.html', context = {'title':'Sobre - Find A Way'})

def recuperaSenha(request):
    return render(request, 'recuperaSenha.html', context = {'title':'Recuperar senha - Find A Way'})

def contato(request):
    return render(request,'contato.html', context={'title':'Contato - Find A Way'})

def cursos(request):
    return render(request, 'cursos.html', context={'title':'Cursos - Find A Way'})

def cadastroCurso(request):
    return render(request, 'CadastroCurso.html', context={'title': 'Cadastrar Curso - Find A Way'})
