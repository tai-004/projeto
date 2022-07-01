from django.shortcuts import render



def template(request):
    return render(request, "publico/index.html", {})


def index(request):
    return render(request, 'publico/index.html', {})


def historico(request):
    return render(request, 'publico/historico.html', {})
    
def agroindrustria(request):
    return render(request, 'publico/agroindrustria.html', {})
      
def agropecuaria(request):
    return render(request, 'publico/agropecuaria.html', {})
      
def informatica(request):
    return render(request, 'publico/informatica.html', {})
     
def hierarquia(request):
    return render(request, 'publico/hierarquia.html', {})

def engresso(request):
    return render(request, 'publico/engresso.html', {})


def contato(request):
    return render(request, 'publico/contato.html', {})

def desenvolvedores(request):
    return render(request, 'publico/desenvolvedores.html', {})

def superior(request):
    return render(request, 'publico/superior.html', {})