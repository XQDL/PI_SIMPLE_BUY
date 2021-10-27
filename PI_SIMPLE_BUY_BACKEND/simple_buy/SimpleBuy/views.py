from django.http import HttpResponse
from django.shortcuts import render

from .dao.GenericDao import GenericDao
from .dao.DaoLogin import DaoLogin
from .dao.DaoItem import DaoItem
from .dao.DaoItensNf import DaoItemNf
from .dao.DaoItemOf import DaoItemOf
from .dao.DaoOrdemFornecimento import DaoOrdemFornecimento
from .dao.DaoFornecedor import DaoFornecedor
from .dao.DaoItemCotacao import DaoItemCotacao
from .dao.DaoComprador import DaoComprador

from .utils.validations import Profile_validate

from django.db import IntegrityError

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
    estados = dao.selectAll(Estado)
    err = None
    fornecedor = None
    comprador = dao.get_by_username(Comprador, nomeUsuario)
    classes = dao.selectAll(Classe)

    try:
        if request.POST.get('cidade'):
            estado = dao.get(Estado, request.POST.get('estado'))

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



    except Exception as e:
        comprador = dao.get_by_username(Comprador, nomeUsuario)

        if 'UNIQUE constraint' in str(e.args):
            err = 'EMPRESA JÁ CADASTRADA!'
        else:
            err = e
        fornecedor = None

    context = {
        "user": comprador,
        "classes": classes,
        "fornecedor": fornecedor,
        "estados": estados,
        "err": err
    }

    return render(request, 'SimpleBuy/cadastrar-fornecedor.html', context)


def cadastrar_item(request, nomeUsuario):
    dao = GenericDao()
    try:
        comprador = dao.get_by_username(Comprador, nomeUsuario)
        user = comprador
    except:
        comprador = False
        administrador = dao.get_by_username(Administrador, nomeUsuario)
        user = administrador

    err = None
    item = None

    try:
        if request.POST.get('descricao'):
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
    except Exception as e:
        if 'UNIQUE constraint' in str(e.args):
            err = 'ITEM JÁ CADASTRADA!'
        else:
            err = e


    itens = dao.selectAll(Item)
    classes = dao.selectAll(Classe)

    if len(itens) != 0:
        id = itens[-1].id + 1
    else:
        id = 1

    context = {
        "id": id,
        "classes": classes,
        "item": item,
        "user": user,
        "err": err
    }
    return render(request, 'SimpleBuy/cadastrar-item.html', context)


def compradores_cadastrados(request, nomeUsuario, comprador_id=0):
    dao = GenericDao()
    daoComprador = DaoComprador()
    daoEmpresa = DaoEmpresaCompradora()
    comprador_remove = None

    adm = dao.get_by_username(Administrador, nomeUsuario)
    empresa = daoEmpresa.get_empresa_by_adm(EmpresaCompradora, adm)



    if comprador_id != 0:
        comprador_remove = dao.get(Comprador, comprador_id)
        comprador_remove = dao.delete(comprador_remove)



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
        "cont_compradores": cont_compradores,
        "comprador_remove": comprador_remove
    }

    return render(request, 'SimpleBuy/compradores-cadastrados.html', context)


def contratar_plano(request):
    return render(request, 'SimpleBuy/contratar-plano.html')


def editar_of(request, nomeUsuario, of_id, item_id=0, of_exclude_id=0, of_enviar_aprovacao_id=0):
    dao = GenericDao()
    daoItemOf = DaoItemOf()
    of_exclude = None
    item = None
    of_enviada= None

    user = dao.get_by_username(Comprador, nomeUsuario)

    of = dao.get(OrdemFornecimento, of_id)

    itens_of = daoItemOf.get_itens_by_of(of)

    if item_id != 0:
        item = dao.get(Itens_of, item_id)


        itens_of = daoItemOf.get_itens_by_of(of)

        item_pendentes_cotacao = Item_pendente_cotacao(
            cod_item=item.cod_item,
            quantidade=item.quantidade,
            data=item.dataEntrega,
            solicitante_comprador=item.solicitante_comprador,
            solicitante_adm=item.solicitante_adm
        )
        dao.create(item_pendentes_cotacao)

        dao.delete(item)

        if len(itens_of) == 0:
            of_exclude = dao.delete(of)


    if of_exclude_id != 0:
        itens_of = daoItemOf.get_itens_by_of(of)
        for i in itens_of:
            item_pendentes_cotacao = Item_pendente_cotacao(
                cod_item=i.cod_item,
                quantidade=i.quantidade,
                data=i.dataEntrega,
                solicitante_comprador=i.solicitante_comprador,
                solicitante_adm=i.solicitante_adm
            )
            dao.create(item_pendentes_cotacao)
            dao.delete(i)

        of_exclude = dao.delete(of)

    if of_enviar_aprovacao_id != 0:
        of.situacao = SituacaoOf.AGUARDANDO_APROVACAO.value
        of_enviada = dao.update(of)


    context = {
        "user": user,
        "of": of,
        "itens_of": itens_of,
        "item_exclude": item,
        "of_exclude": of_exclude,
        "of_enviada": of_enviada
    }

    return render(request, 'SimpleBuy/editar-of.html', context)


def gerar_cotacao(request, nomeUsuario, item_id, fornecedor_id=0, of_id=0):
    dao = GenericDao()
    daoOrdemFornecimento = DaoOrdemFornecimento()
    daoItensOf = DaoItemOf()

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
            frete=frete,
            solicitante_adm=item_pendente_cotacao.solicitante_adm,
            solicitante_comprador= item_pendente_cotacao.solicitante_comprador

        )

        dao.create(itens_of)

        # Atualizando o valor total da OF
        itens_of_temp = daoItensOf.get_itens_by_of(ordemFornecimento)

        vlr_tot = 0
        for i in itens_of_temp:
            vlr_tot += i.valor

        ordemFornecimento.valor_total = vlr_tot

        dao.update(ordemFornecimento)

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

            ofs = daoOrdemFornecimento.get_by_fornecedor(fornecedor, SituacaoOf.COMPRADOR_NEGOCIANDO.value)

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
    daoItemOf = DaoItemOf()
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


            try:
                valor_un = daoItemOf.get_valor_aproximado(item)
            except:
                valor_un = "INDEFINIDO"



            context = {
                "user": user,
                "item": item,
                "valor_un": valor_un
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


def integrar_nota_fiscal(request, nomeUsuario, fornecedor_id=0, item_id=0, of_id=0, num_nf=0, item_exclude=0, integrar=0):
    dao = GenericDao()
    daoOrdemFornecimento = DaoOrdemFornecimento()
    daoItemOf = DaoItemOf()
    daoEmpresa = DaoEmpresaCompradora()
    daoItensNf = DaoItemNf()
    administrador = None

    try:
        comprador = dao.get_by_username(Comprador, nomeUsuario)
        user = comprador
    except:
        comprador = False
        administrador = dao.get_by_username(Administrador, nomeUsuario)
        user = administrador

    item = None
    fornecedor = None
    ofs_disponiveis = None
    of = None
    empresa = None
    nf_created = None
    nf = None
    itens_nf = None
    item_nf_created = None
    item_excluir = None
    err = None

    if fornecedor_id != 0:
        fornecedor = dao.get(Fornecedor, fornecedor_id)


    if item_id != 0:
        item = dao.get(Item, item_id)
        print(item)

    if fornecedor and item:
        ofs_disponiveis = daoOrdemFornecimento.get_by_fornecedor_situacao_and_item(fornecedor, SituacaoOf.ABERTA.value, item)

    if of_id != 0:
        of = dao.get(OrdemFornecimento, of_id)
        ofs_disponiveis = None



    if administrador:
        empresa = daoEmpresa.get_empresa_by_adm(EmpresaCompradora, administrador)
    else:
        empresa = comprador.empresa


    if request.POST.get('nf') and num_nf==0:
        nf = NotaFiscal(
            numeroNota=request.POST.get('nf'),
            empresaEmitente=fornecedor,
            empresaDestinada=empresa
        )
        nf = dao.create(nf)
        nf_created = nf
    elif num_nf != 0:
        nf = dao.get(NotaFiscal, num_nf)
        itens_nf = daoItensNf.get_itens_by_nf(nf)


    if request.POST.get('valor_unitario'):
        try:
            ipi = float(request.POST.get('ipi'))
            icms = float(request.POST.get('icms'))
            quantidade = float(request.POST.get('quantidade'))
            valor_unitario = float(request.POST.get('valor_unitario'))
            frete = request.POST.get('frete')
            valor_total = (valor_unitario * quantidade) * (1+(ipi/100)) * (1+(icms/100))


            itens_of = daoItemOf.get_itens_by_of(of)

            for i in itens_of:

                if i.cod_item.id == item.id:
                    item_of = i


            if quantidade > (item_of.quantidade - item_of.recebido):
                err = 'SALDO DA OF INSUFICIENTE!!'
            if valor_unitario != item_of.valor_unitario or ipi != item_of.ipi or icms != item_of.icms:
                err = 'VALORES DIVERGENTES'

            if not err:
                item_nf = Itens_nf(
                    cod_item=item,
                    num_nf=nf,
                    num_of=of,
                    valor_unitario=valor_unitario,
                    valor=valor_total,
                    quantidade=quantidade,
                    ipi=ipi,
                    icms=icms,
                    frete=frete
                )

                item_nf_created = dao.create(item_nf)


        except Exception as e:
            print(e)


    if item_exclude != 0:
        item_excluir = dao.get(Itens_nf, item_exclude)
        item_excluir = dao.delete(item_excluir)

    if integrar == 'integrar':
        for item_nf in itens_nf:
            itens_of = daoItemOf.get_itens_by_of(item_nf.num_of.id)
            for item_of in itens_of:
                if item_of.cod_item.id == item_nf.cod_item.id:
                    item_of.recebido += item_nf.quantidade


                    of = item_nf.num_of


                    itens_of_temp = daoItemOf.get_itens_by_of(of)
                    tem_saldo = False
                    for i in itens_of_temp:
                        if i.recebido <= i.quantidade:
                           tem_saldo = True

                    if not tem_saldo:
                        of.situacao = SituacaoOf.FECHADA.value
                        dao.update(of)
                        of = None


    else:
        integrar = False


    context = {
        "user": user,
        "item": item,
        "fornecedor": fornecedor,
        "ofs_disponiveis": ofs_disponiveis,
        "of": of,
        "nf": nf,
        "nf_created": nf_created,
        "itens_nf": itens_nf,
        "item_nf_created": item_nf_created,
        "item_exclude": item_excluir,
        "integrar": integrar,
        "err": err

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
    dao = GenericDao()
    err = None
    administrador = None


    try:
        if request.POST.get('user_name'):
            administrador = Administrador(
                nomeUsuario=request.POST.get('user_name'),
                senha=request.POST.get('password'),
                nome=request.POST.get('complete_name'),
                email=request.POST.get('email'),
                telefone=request.POST.get('phone_number'),
                plano=plan
            )
            profile_validate = Profile_validate()
            existing_profile = profile_validate.verify_existing_profile(administrador.nomeUsuario)

            if not existing_profile:
                print('passando')
                administrador = dao.create(administrador)
                print(administrador)
            else:
                administrador = None
                err = 'INFORMAÇÕES JÁ UTILIZADAS EM UM PERFIL EXISTENTE'
    except Exception as e:
        err = 'INFORMAÇÕES JÁ UTILIZADAS EM UM PERFIL EXISTENTE'
        administrador = None

    context = {
        'plan': plan,
        'administrador': administrador,
        'err': err
    }
    return render(request, 'SimpleBuy/registrar-administrador.html', context=context)


def registrar_comprador(request, nomeUsuario):
    dao = GenericDao()
    daoEmpresa = DaoEmpresaCompradora()

    adm = dao.get_by_username(Administrador, nomeUsuario)
    empresa = daoEmpresa.get_empresa_by_adm(EmpresaCompradora, adm)
    err = None

    try:
        if request.POST.get('user_name'):
            comprador = Comprador(
                nomeUsuario=request.POST.get('user_name'),
                senha=request.POST.get('password'),
                nome=request.POST.get('complete_name'),
                email=request.POST.get('email'),
                telefone=request.POST.get('phone_number'),
                empresa=empresa
            )

            profile_validate = Profile_validate()

            existing_profile = profile_validate.verify_existing_profile(comprador.nomeUsuario)


            daoComprador = DaoComprador()

            compradores = daoComprador.get_compradores_by_empresa(Comprador, empresa)

            if adm.plano == 1:
                max = 1
            elif adm.plano == 2:
                max = 3
            elif adm.plano == 3:
                max = 10

            print('TESTANDO:')


            if len(compradores) >= max:
                err = "Numero máximo de compradores alcançado!\nImpossivel cadastrar!"
                comprador = None


            if not existing_profile and err == None:
                comprador = dao.create(comprador)
            elif err == None:
                comprador = None
                err = 'INFORMAÇÕES JÁ UTILIZADAS EM UM PERFIL EXISTENTE'



            context = {
                "user": adm,
                "err": err,
                'comprador': comprador
            }
            return render(request, 'SimpleBuy/registrar-comprador.html', context=context)
    except:
        adm = dao.get_by_username(Administrador, nomeUsuario)
        context = {
            "user": adm
        }
        return render(request, 'SimpleBuy/registrar-comprador.html', context)


    adm = dao.get_by_username(Administrador, nomeUsuario)
    context = {
        "user": adm
    }
    return render(request, 'SimpleBuy/registrar-comprador.html', context)


def registrar_empresa(request, adm_id):
    dao = GenericDao()

    err = None
    estado = None
    empresa_compradora = None
    try:
        if request.POST.get('rua'):
            estado = dao.get(Estado, request.POST.get('estado'))

            cidade = Cidade(nome=request.POST.get('cidade'), estado=estado)

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

            print('AKII')
            empresa_compradora = dao.create(empresa_compradora)
            print(empresa_compradora)


    except Exception as e:
        if 'UNIQUE constraint' in str(e.args):
            err = 'EMPRESA JÁ CADASTRADA!'
        else:
            err = e
        empresa_compradora = None

    estados = dao.selectAll(Estado)

    context = {
        'err': err,
         "estados": estados,
        'empresa_compradora': empresa_compradora

    }
    return render(request, 'SimpleBuy/registrar-empresa.html', context=context)



def selecionar_item(request, nomeUsuario, fornecedor_id=0, num_nf=0):
    dao = GenericDao()
    daoItem = DaoItem()

    print('[Selecionar Item] > ')


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


def selecionar_of(request, nomeUsuario, item_id=0, fornecedor_id=0, item_filter_id=0, num_nf=0):
    dao = GenericDao()
    daoOrdemFornecimento = DaoOrdemFornecimento()

    try:
        comprador = dao.get_by_username(Comprador, nomeUsuario)
        user = comprador
    except:
        comprador = False
        administrador = dao.get_by_username(Administrador, nomeUsuario)
        user = administrador





    if item_id !=0:
        item_pendente_cotacao = dao.get(Item_pendente_cotacao, item_id)
        fornecedor = dao.get(Fornecedor, fornecedor_id)
        ofs = daoOrdemFornecimento.get_by_fornecedor(fornecedor, SituacaoOf.COMPRADOR_NEGOCIANDO.value)


        context = {
            "user": user,
            "item_pendente_cotacao": item_pendente_cotacao,
            "ofs": ofs,
            "fornecedor": fornecedor
        }

    else:
        fornecedor = dao.get(Fornecedor, fornecedor_id)
        item = dao.get(Item, item_filter_id)
        ofs = daoOrdemFornecimento.get_by_fornecedor_situacao_and_item(fornecedor, SituacaoOf.ABERTA.value, item)

        context = {
            "user": user,
            "ofs": ofs,
            "fornecedor": fornecedor
        }



    return render(request, 'SimpleBuy/selecionar-of.html', context)









def selecionar_fornecedor(request, nomeUsuario, item_id=0):
    dao = GenericDao()
    daoFornecedor = DaoFornecedor()
    item_pendente_cotacao = None

    try:
        comprador = dao.get_by_username(Comprador, nomeUsuario)
        user = comprador
    except:
        comprador = False
        administrador = dao.get_by_username(Administrador, nomeUsuario)
        user = administrador



    if item_id != 0:
        item_pendente_cotacao = dao.get(Item_pendente_cotacao, item_id)
        fornecedores = daoFornecedor.get_fornecedor_by_classe(item_pendente_cotacao.cod_item.classe)
    else:
        fornecedores = dao.selectAll(Fornecedor)

    context = {
        "user": user,
        "item_pendente_cotacao": item_pendente_cotacao,
        "fornecedores": fornecedores
    }
    return render(request, 'SimpleBuy/selecionar-fornecedor.html', context)