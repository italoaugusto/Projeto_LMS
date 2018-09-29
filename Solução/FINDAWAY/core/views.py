from django.shortcuts import render
from .models import Usuario

def cadastro(request):#criando a conexão  da pagila cadastro 
    if request.method == 'GET':
        return render(request, 'Cadastro.html')
    elif request.method == 'POST':
        if request.POST.get('login')and request.POST.get('senha'):
            print('teste.....')
            user = Usuario()
            user.login =  request.POST.get('login')
            user.senha= request.POST.get('senha')
            user.email =  request.POST.get('email')
            user.senha= request.POST.get('senha')
            user.celular=  request.POST.get('celular')
           

            print(user)
            user.save()
            print(user)
            return render(request,'Cadastro.html')
        else:
            return render(request,'Cadastro.html')

    return render(request,'Cadastro.html')
