from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('aprovacoes-pendentes', views.aprovacoes_pendentes, name='aprovacoes_pendentes'),
    path('inicio-comprador/<str:nomeUsuario>/cadastrar-fornecedor', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('inicio-administrador/<str:nomeUsuario>/cadastrar-item', views.cadastrar_item, name='cadastrar_item'),
    path('inicio-comprador/<str:nomeUsuario>/cadastrar-item', views.cadastrar_item, name='cadastrar_item'),
    path('inicio-administrador/<str:nomeUsuario>/compradores-cadastrados', views.compradores_cadastrados, name='compradores_cadastrados'),
    path('contratar-plano', views.contratar_plano, name='contratar_plano'),
    path('editar-of', views.editar_of, name='editar_of'),
    path('inicio-comprador/<str:nomeUsuario>/gerar-cotacao/<int:item_id>/', views.gerar_cotacao, name='gerar_cotacao'),
    path('inicio-comprador/<str:nomeUsuario>/gerar-cotacao/<int:item_id>/<int:fornecedor_id>/', views.gerar_cotacao, name='gerar_cotacao'),
    path('inicio-comprador/<str:nomeUsuario>/gerar-cotacao/<int:item_id>/<int:fornecedor_id>/<int:of_id>', views.gerar_cotacao, name='gerar_cotacao'),
    path('inicio-comprador/<str:nomeUsuario>/gerar-pedido/', views.gerar_pedido, name='gerar_pedido'),
    path('inicio-administrador/<str:nomeUsuario>/gerar-pedido/', views.gerar_pedido, name='gerar_pedido'),
    path('inicio-comprador/<str:nomeUsuario>/gerar-pedido/<int:item_id>', views.gerar_pedido, name='gerar_pedido'),
    path('inicio-administrador/<str:nomeUsuario>/gerar-pedido/<int:item_id>', views.gerar_pedido, name='gerar_pedido'),
    path('historico-compras', views.historico_compras, name='historico_compras'),
    path('info-of', views.info_of, name='info_of'),
    path('inicio-administrador', views.inicio_administrador, name='inicio_administrador'),
    path('inicio-administrador/<str:nomeUsuario>/', views.inicio_administrador, name='inicio_administrador'),
    path('inicio-comprador/<str:nomeUsuario>/', views.inicio_comprador, name='inicio_comprador'),
    path('inicio-administrador/<str:nomeUsuario>/integrar-nota-fiscal', views.integrar_nota_fiscal, name='integrar_nota_fiscal'),
    path('inicio-comprador/<str:nomeUsuario>/itens-pendentes-cotacao', views.itens_pendentes_cotacao, name='itens_pendentes_cotacao'),
    path('inicio-comprador/<str:nomeUsuario>/lista-fornecedores/<int:classe>', views.lista_fornecedores, name='lista_fornecedores'),
    path('login', views.login, name='login'),
    path('inicio-comprador/<str:nomeUsuario>/ofs-pendentes', views.ofs_pendentes, name='ofs_pendentes'),
    path('registrar-administrador/<str:plan>', views.registrar_administrador, name='registrar_administrador'),
    path('registrar-administrador/<str:plan>/', views.registrar_administrador, name='registrar_administrador'),
    path('inicio-administrador/<str:nomeUsuario>/registrar-comprador', views.registrar_comprador, name='registrar_comprador'),
    path('registrar-empresa', views.registrar_empresa, name='registrar_empresa'),
    path('registrar-empresa/<int:adm_id>/', views.registrar_empresa, name='registrar_empresa'),
    path('validate-login', views.validate_login, name='validate-login'),
    path('inicio-comprador/<str:nomeUsuario>/gerar-pedido/selecionar-item', views.selecionar_item, name='selecionar-item'),
    path('inicio-comprador/<str:nomeUsuario>/gerar-cotacao/<int:item_id>/selecionar-fornecedor', views.selecionar_fornecedor, name='selecionar-item'),
    path('inicio-comprador/<str:nomeUsuario>/gerar-cotacao/<int:item_id>/<int:fornecedor_id>/selecionar-of/', views.selecionar_of, name='selecionar_of')


]