from django.http import HttpResponse
from django.shortcuts import render

from .dao.GenericDao import GenericDao
from .dao.DaoLogin import DaoLogin
from .dao.DaoItem import DaoItem
from .dao.DaoItemOf import DaoItemOf
from .dao.DaoOrdemFornecimento import DaoOrdemFornecimento
from .dao.DaoFornecedor import DaoFornecedor
from .dao.DaoItemCotacao import DaoItemCotacao
from .dao.DaoComprador import DaoComprador

from .enum.SituacaoOf import SituacaoOf

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
            "user": adm,
            "administrador": 1
        }
        return render(request, 'SimpleBuy/login.html', context)



    except:
        try:
            comprador = dao.validate_login(Comprador, user, password)
            context = {
                "user": comprador,
                "comprador": 1
            }
            return render(request, 'SimpleBuy/login.html', context)
        except:
            context = {
                "err": "LOGIN INVÁLIDO!"
            }
            return render(request, 'SimpleBuy/login.html', context)


def aprovacoes_pendentes(request, nomeUsuario, res='', of_id=0):
    dao = GenericDao()
    daoOf = DaoOrdemFornecimento()

    administrador = dao.get_by_username(Administrador, nomeUsuario)

    ofs = daoOf.get_by_situacao(SituacaoOf.AGUARDANDO_APROVACAO.value)

    of_aprovada = None
    of_reprovada = None

    if of_id != 0:
        if res == 'aprovar':
            of_aprovada = dao.get(OrdemFornecimento, of_id)
            of_aprovada.situacao = SituacaoOf.ABERTA.value
            of_aprovada = dao.update(of_aprovada)
        if res == 'reprovar':
            of_reprovada = dao.get(OrdemFornecimento, of_id)
            of_reprovada.situacao = SituacaoOf.REPROVADA.value
            of_reprovada = dao.update(of_reprovada)


    context = {
        "user": administrador,
        "ofs": ofs,
        "of_aprovada": of_aprovada,
        "of_reprovada": of_reprovada
    }


    return render(request, 'SimpleBuy/aprovacoes-pendentes.html', context)


def cadastrar_fornecedor(request, nomeUsuario):
    dao = GenericDao()
    try:
        estado = Estado(nome=request.POST.get('estado'))

        dao.create(estado)

        cidade = Cidade(nome=request.POST.get('cidade'), estado=estado)

        dao.create(cidade)

        endereco = Endereco(rua=request.POST.get('rua'),
                            numero=request.POST.get('numero'),
                            cep=request.POST.get('cep'),
                            cidade=cidade
                            )

        dao.create(endereco)

        classe = dao.get(Classe, request.POST.get('classe'))


        fornecedor = Fornecedor(
            nome=request.POST.get('name'),
            cnpj=request.POST.get('cnpj'),
            endereco=endereco,
            telefone=request.POST.get('phone_number'),
            classe=classe,
            email= request.POST.get('email')

        )

        dao.create(fornecedor)

        comprador = dao.get_by_username(Comprador, nomeUsuario)

        context = {
            "user": comprador,
            "fornecedor": fornecedor
        }

        return render(request, 'SimpleBuy/cadastrar-fornecedor.html', context)

    except:
        comprador = dao.get_by_username(Comprador, nomeUsuario)
        classes = dao.selectAll(Classe)

        context = {
            "user": comprador,
            "classes": classes
        }

        return render(request, 'SimpleBuy/cadastrar-fornecedor.html', context)


def cadastrar_item(request, nomeUsuario):
    dao = GenericDao()
    try:
        user = dao.get_by_username(Comprador, nomeUsuario)
    except:
        user = dao.get_by_username(Administrador, nomeUsuario)

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
            "item": item,
            "user": user
        }
        return render(request, 'SimpleBuy/cadastrar-item.html', context)
    except:
        itens = dao.selectAll(Item)
        classes = dao.selectAll(Classe)

        id = itens[-1].id + 1

        context = {
            "id": id,
            "classes": classes,
            "user": user

        }
        return render(request, 'SimpleBuy/cadastrar-item.html', context)


def compradores_cadastrados(request, nomeUsuario):
    dao = GenericDao()
    daoComprador = DaoComprador()
    daoEmpresa = DaoEmpresaCompradora()

    adm = dao.get_by_username(Administrador, nomeUsuario)
    empresa = daoEmpresa.get_empresa_by_adm(EmpresaCompradora, adm)

    compradores = daoComprador.get_compradores_by_empresa(Comprador, empresa)

    if adm.plano == 1:
        max = 1
    elif adm.plano == 2:
        max = 3
    elif adm.plano == 3:
        max = 10

    cont_compradores = len(compradores)

    context = {
        "user": adm,
        "compradores": compradores,
        "max": max,
        "cont_compradores": cont_compradores
    }

    return render(request, 'SimpleBuy/compradores-cadastrados.html', context)


def contratar_plano(request):
    return render(request, 'SimpleBuy/contratar-plano.html')


def editar_of(request):
    return render(request, 'SimpleBuy/editar-of.html')


def gerar_cotacao(request, nomeUsuario, item_id, fornecedor_id=0, of_id=0):
    dao = GenericDao()
    daoOrdemFornecimento = DaoOrdemFornecimento()

    comprador = dao.get_by_username(Comprador, nomeUsuario)
    item_pendente_cotacao = dao.get(Item_pendente_cotacao, item_id)
    ordemFornecimento = None


    try:
        fornecedor = dao.get(Fornecedor, fornecedor_id)


        ipi = float(request.POST.get('ipi'))
        icms = float(request.POST.get('icms'))
        quantidade = float(item_pendente_cotacao.quantidade)
        valor_unitario = float(request.POST.get('unitario'))
        frete = request.POST.get('frete')

        print('ok')

        if of_id != 0:
            ordemFornecimento = dao.get(OrdemFornecimento, of_id)
        else:
            ordemFornecimento = OrdemFornecimento(
                fornecedor=fornecedor,
                contratante=comprador.empresa,
                comprador=comprador
            )
            ordemFornecimento = dao.create(ordemFornecimento)

        valor = (valor_unitario * quantidade) * (1+(ipi/100)) * (1+(icms/100))

        itens_of = Itens_of(
            cod_item=item_pendente_cotacao.cod_item,
            num_of=ordemFornecimento,
            valor_unitario=valor_unitario,
            valor=valor,
            quantidade=quantidade,
            ipi=ipi,
            icms=icms,
            dataEntrega=item_pendente_cotacao.data,
            frete=frete
        )

        dao.create(itens_of)



        context = {
            "user": comprador,
            "item_pendente_cotacao": item_pendente_cotacao.cod_item,
            "item": item_pendente_cotacao.cod_item,
            "quantidade": item_pendente_cotacao.quantidade,
            "of": ordemFornecimento,
            "itens_of": itens_of

        }

        dao.delete(item_pendente_cotacao)


        return render(request, 'SimpleBuy/gerar-cotacao.html', context)

    except:
        if of_id != 0:
            ordemFornecimento = dao.get(OrdemFornecimento, of_id)

        if fornecedor_id != 0:
            fornecedor = dao.get(Fornecedor, fornecedor_id)

            ofs = daoOrdemFornecimento.get_by_fornecedor(fornecedor)

            cont_ofs = len(ofs)

            if cont_ofs > 0:
                ofs_disponiveis = True
            else:
                ofs_disponiveis = False


            context = {
                "user": comprador,
                "item_pendente_cotacao": item_pendente_cotacao,
                "item": item_pendente_cotacao.cod_item,
                "quantidade": item_pendente_cotacao.quantidade,
                "fornecedor": fornecedor,
                "of": ordemFornecimento,
                "ofs_disponiveis": ofs_disponiveis,

            }

            return render(request, 'SimpleBuy/gerar-cotacao.html', context)
        else:
            context = {
                "user": comprador,
                "item_pendente_cotacao": item_pendente_cotacao.cod_item,
                "item": item_pendente_cotacao.cod_item,
                "of": ordemFornecimento,
                "quantidade": item_pendente_cotacao.quantidade

            }

            return render(request, 'SimpleBuy/gerar-cotacao.html', context)


def gerar_pedido(request, nomeUsuario, item_id=0):
    dao = GenericDao()
    try:
        comprador = dao.get_by_username(Comprador, nomeUsuario)
        user = comprador
    except:
        comprador = False
        administrador = dao.get_by_username(Administrador, nomeUsuario)
        user = administrador

    try:
        codigo = request.POST.get('codigo')
        quantidade = request.POST.get('quantidade')
        data_entrega = request.POST.get('data-entrega')

        item = dao.get(Item, codigo)

        if comprador:
            item_cotacao = Item_pendente_cotacao(
                cod_item=item,
                quantidade=quantidade,
                data=data_entrega,
                solicitante_comprador=comprador
            )

        else:
            item_cotacao = Item_pendente_cotacao(
                cod_item=item,
                quantidade=quantidade,
                data=data_entrega,
                solicitante_adm=administrador
            )

        dao.create(item_cotacao)
        context = {
            "user": user,
            "item_cotacao": item_cotacao
        }
        return render(request, 'SimpleBuy/gerar-pedido.html', context)

    except:
        if item_id != 0:
            item = dao.get(Item, item_id)
            context = {
                "user": user,
                "item": item
            }
            return render(request, 'SimpleBuy/gerar-pedido.html', context)
        else:
            context = {
                "user": user
            }
            return render(request, 'SimpleBuy/gerar-pedido.html', context)


def historico_compras(request, nomeUsuario):
    dao = GenericDao()
    dao_itens_of = DaoItemOf()

    try:
        comprador = dao.get_by_username(Comprador, nomeUsuario)
        user = comprador
    except:
        comprador = False
        administrador = dao.get_by_username(Administrador, nomeUsuario)
        user = administrador

    ofs = dao.selectAll(OrdemFornecimento)


    context = {
        "user": user,
        "ofs": ofs
    }



    return render(request, 'SimpleBuy/historico-compras.html', context)


def info_of(request, nomeUsuario, of_id):
    dao = GenericDao()
    daoItensOf = DaoItemOf()
    try:
        comprador = dao.get_by_username(Comprador, nomeUsuario)
        user = comprador
    except:
        comprador = False
        administrador = dao.get_by_username(Administrador, nomeUsuario)
        user = administrador


    of = dao.get(OrdemFornecimento, of_id)
    itens_of = daoItensOf.get_itens_by_of(of)

    context = {
        "user": user,
        "of": of,
        "itens_of": itens_of
    }


    return render(request, 'SimpleBuy/info-of.html', context)


def inicio_administrador(request, nomeUsuario):
    dao = GenericDao()
    adm = dao.get_by_username(Administrador, nomeUsuario)
    context = {
        "user": adm
    }
    return render(request, 'SimpleBuy/inicio-administrador.html', context)


def inicio_comprador(request, nomeUsuario):
    dao = GenericDao()
    comprador = dao.get_by_username(Comprador, nomeUsuario)
    context = {
        "user": comprador
    }
    return render(request, 'SimpleBuy/inicio-comprador.html', context)


def integrar_nota_fiscal(request, nomeUsuario):
    dao = GenericDao()
    adm = dao.get_by_username(Administrador, nomeUsuario)
    context = {
        "user": adm
    }

    return render(request, 'SimpleBuy/integrar-nota-fiscal.html', context)


def itens_pendentes_cotacao(request, nomeUsuario):
    dao = GenericDao()
    dao_itens = DaoItemCotacao()
    comprador = dao.get_by_username(Comprador, nomeUsuario)
    empresa = comprador.empresa



    itens_pendentes = dao_itens.select_by_empresa(Item_pendente_cotacao, empresa)

    print(itens_pendentes)




    context = {
        "user": comprador,
        "itens_pendentes": itens_pendentes
    }
    return render(request, 'SimpleBuy/itens-pendentes-cotacao.html', context)


def lista_fornecedores(request, nomeUsuario, classe):
    dao = GenericDao()
    daoFornecedor = DaoFornecedor()
    comprador = dao.get_by_username(Comprador, nomeUsuario)
    classe = dao.get(Classe, classe)

    fornecedores = daoFornecedor.get_fornecedor_by_classe(classe)


    context = {
        "user": comprador,
        "classe": classe,
        "fornecedores": fornecedores
    }






    return render(request, 'SimpleBuy/lista-fornecedores.html', context)


def login(request):
    return render(request, 'SimpleBuy/login.html')


def ofs_pendentes(request, nomeUsuario, of_id=0):
    dao = GenericDao()
    daoOf = DaoOrdemFornecimento()
    ofs = daoOf.get_by_situacao(SituacaoOf.COMPRADOR_NEGOCIANDO.value)
    comprador = dao.get_by_username(Comprador, nomeUsuario)

    of_enviada = None

    if of_id != 0:
        of_enviada = dao.get(OrdemFornecimento, of_id)
        of_enviada.situacao = SituacaoOf.AGUARDANDO_APROVACAO.value
        of_enviada = dao.update(of_enviada)


    context = {
        "user": comprador,
        "ofs": ofs,
        "of_enviada": of_enviada
    }

    return render(request, 'SimpleBuy/ofs-pendentes.html', context)


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


def registrar_comprador(request, nomeUsuario):
    dao = GenericDao()
    daoEmpresa = DaoEmpresaCompradora()

    adm = dao.get_by_username(Administrador, nomeUsuario)
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

        adm = dao.get_by_username(Administrador, nomeUsuario)
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


def selecionar_item(request, nomeUsuario):
    dao = GenericDao()
    daoItem = DaoItem()

    try:
        comprador = dao.get_by_username(Comprador, nomeUsuario)
        user = comprador
    except:
        comprador = False
        administrador = dao.get_by_username(Administrador, nomeUsuario)
        user = administrador

    classes = dao.selectAll(Classe)

    try:
        codigo = request.POST.get('codigo')
        descricao = request.POST.get('descricao')
        classe_id = request.POST.get('classe')
        unidade_medida = request.POST.get('unidade-medida')

        try:
            classe = dao.get(Classe, classe_id)
        except:
            classe = ""

        itens = daoItem.filter(Item, id=codigo, desc=descricao, classe=classe, unidade_medida=unidade_medida)

        context = {
            "user": user,
            "itens": itens,
            "classes": classes
        }
        return render(request, 'SimpleBuy/selecionar-item.html', context)

    except:
        itens = dao.selectAll(Item)

        context = {
            "user": user,
            "itens": itens,
            "classes": classes
        }

        return render(request, 'SimpleBuy/selecionar-item.html', context)


def selecionar_of(request, nomeUsuario, item_id, fornecedor_id):
    dao = GenericDao()
    daoOrdemFornecimento = DaoOrdemFornecimento()

    comprador = dao.get_by_username(Comprador, nomeUsuario)
    item_pendente_cotacao = dao.get(Item_pendente_cotacao, item_id)
    fornecedor = dao.get(Fornecedor, fornecedor_id)


    ofs = daoOrdemFornecimento.get_by_fornecedor(fornecedor)




    context = {
        "user": comprador,
        "item_pendente_cotacao": item_pendente_cotacao,
        "ofs": ofs,
        "fornecedor": fornecedor
    }

    return render(request, 'SimpleBuy/selecionar-of.html', context)









def selecionar_fornecedor(request, nomeUsuario, item_id):
    dao = GenericDao()
    daoFornecedor = DaoFornecedor()


    item_pendente_cotacao = dao.get(Item_pendente_cotacao, item_id)

    comprador = dao.get_by_username(Comprador, nomeUsuario)

    fornecedores = daoFornecedor.get_fornecedor_by_classe(item_pendente_cotacao.cod_item.classe)

    context = {
        "user": comprador,
        "item_pendente_cotacao": item_pendente_cotacao,
        "fornecedores": fornecedores
    }
    return render(request, 'SimpleBuy/selecionar-fornecedor.html', context)