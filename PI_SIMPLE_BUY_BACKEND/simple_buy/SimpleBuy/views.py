from django.http import HttpResponse
from django.shortcuts import render

from .dao.GenericDao import GenericDao
from .dao.DaoLogin import DaoLogin
from .dao.DaoEmpresaCompradora import DaoEmpresaCompradora
from .models import *


def index(request):
    return render(request, 'SimpleBuy/index.html')

def validate_login(request):
    user = request.POST.get('user')
    password = request.POST.get('password')

    dao = DaoLogin()

    try:

        adm = dao.validate_login(Administrador, user, password)
        context = {
            "user": adm
        }
        return render(request, 'SimpleBuy/inicio-administrador.html', context)

    except:
        try:
            comprador = dao.validate_login(Comprador, user, password)
            context = {
                "user": comprador
            }
            return render(request, 'SimpleBuy/inicio-comprador.html', context)
        except:
            context = {
                "err": "LOGIN INVÁLIDO!"
            }
            return render(request, 'SimpleBuy/login.html', context)








def aprovacoes_pendentes(request):
    return render(request, 'SimpleBuy/aprovacoes-pendentes.html')

def cadastrar_fornecedor(request):
    return render(request, 'SimpleBuy/cadastrar-fornecedor.html')

def cadastrar_item(request):
    dao = GenericDao()

    try:
        class_id = request.POST.get('classe')

        if class_id is None:
            classe = dao.get(Classe, 1)
        else:
            classe = dao.get(Classe, class_id)


        item = Item(
            descricao=request.POST.get('descricao'),
            unidadeMedida=request.POST.get('unidade_medida'),
            classe=classe
        )
        item = dao.create(item)
        context = {
            "item": item
        }
        return render(request, 'SimpleBuy/cadastrar-item.html', context)
    except:
        itens = dao.selectAll(Item)
        classes = dao.selectAll(Classe)

        id = itens[-1].id+1

        context = {
            "id": id,
            "classes": classes

        }
        return render(request, 'SimpleBuy/cadastrar-item.html', context)





def compradores_cadastrados(request):
    return render(request, 'SimpleBuy/compradores-cadastrados.html')

def contratar_plano(request):
    return render(request, 'SimpleBuy/contratar-plano.html')


def editar_of(request):
    return render(request, 'SimpleBuy/editar-of.html')


def gerar_cotacao(request):
    return render(request, 'SimpleBuy/gerar-cotacao.html')


def gerar_pedido(request):
    return render(request, 'SimpleBuy/gerar-pedido.html')


def historico_compras(request):
    return render(request, 'SimpleBuy/historico-compras.html')


def info_of(request):
    return render(request, 'SimpleBuy/info-of.html')


def inicio_administrador(request, id):
    dao = GenericDao()
    adm = dao.get(Administrador, id)
    context = {
        "user":adm
    }
    return render(request, 'SimpleBuy/inicio-administrador.html', context)


def inicio_comprador(request):
    return render(request, 'SimpleBuy/inicio-comprador.html')

def integrar_nota_fiscal(request):
    return render(request, 'SimpleBuy/integrar-nota-fiscal.html')

def itens_pendentes_cotacao(request):
    return render(request, 'SimpleBuy/itens-pendentes-cotacao.html')

def lista_fornecedores(request):
    return render(request, 'SimpleBuy/lista-fornecedores.html')

def login(request):
    return render(request, 'SimpleBuy/login.html')

def ofs_pendentes(request):
    return render(request, 'SimpleBuy/ofs-pendentes.html')

def registrar_administrador(request, plan):
    try:
        administrador = Administrador(
            nomeUsuario=request.POST.get('user_name'),
            senha=request.POST.get('password'),
            nome=request.POST.get('complete_name'),
            email=request.POST.get('email'),
            telefone=request.POST.get('phone_number'),
            plano=plan
        )

        dao = GenericDao()
        administrador = dao.create(administrador)

        context = {
            'plan': plan,
            'administrador': administrador
        }
        return render(request, 'SimpleBuy/registrar-empresa.html', context=context)
    except:
        context = {
            'plan': plan
        }
        return render(request, 'SimpleBuy/registrar-administrador.html', context=context)


def registrar_comprador(request, id):
    dao = GenericDao()
    daoEmpresa = DaoEmpresaCompradora()

    adm = dao.get(Administrador, id)
    empresa = daoEmpresa.get_empresa_by_adm(EmpresaCompradora, adm)

    try:
        comprador = Comprador(
            nomeUsuario=request.POST.get('user_name'),
            senha=request.POST.get('password'),
            nome=request.POST.get('complete_name'),
            email=request.POST.get('email'),
            telefone=request.POST.get('phone_number'),
            empresa=empresa
        )


        comprador = dao.create(comprador)

        context = {
            "user": adm,
            'comprador': comprador
        }
        return render(request, 'SimpleBuy/registrar-comprador.html', context=context)
    except:

        adm = dao.get(Administrador, id)
        context = {
            "user": adm
        }

        return render(request, 'SimpleBuy/registrar-comprador.html', context)


def registrar_empresa(request, adm_id):


    dao = GenericDao()
    try:
        estado = Estado(nome=request.POST.get('estado'))

        dao.create(estado)

        cidade = Cidade(nome=request.POST.get('estado'), estado=estado)

        dao.create(cidade)

        endereco = Endereco(rua=request.POST.get('rua'),
                            numero=request.POST.get('numero'),
                            cep=request.POST.get('cep'),
                            complemento=request.POST.get('complemento'),
                            cidade=cidade
                            )

        dao.create(endereco)

        empresa_compradora = EmpresaCompradora(
            nome=request.POST.get('name'),
            cnpj=request.POST.get('cnpj'),
            endereco=endereco,
            telefone=request.POST.get('phone_number'),
            administrador=dao.get(Administrador, adm_id)
        )

        dao.create(empresa_compradora)

        return render(request, 'SimpleBuy/index.html')

    except:
        return render(request, 'SimpleBuy/registrar-empresa.html/')




def selecionar_of(request):
    return render(request, 'SimpleBuy/selecionar-of.html')



