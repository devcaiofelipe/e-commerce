from django.urls import path
from .views import ListaProduto, DetalheProduto,AdicionarAoCarrinho, RemoverDoCarrinho, Carrinho, ResumoDaCompra

app_name = 'produto'

urlpatterns = [
    path('', ListaProduto.as_view(), name="lista"),
    path('adicionaraocarrinho/', AdicionarAoCarrinho.as_view(), name="adicionaraocarrinho"),
    path('removerdocarrinho/', RemoverDoCarrinho.as_view(), name="removerdocarrinho"),
    path('carrinho/', Carrinho.as_view(), name="carrinho"),
    path('resumo/', ResumoDaCompra.as_view(), name="resumodacompra"),
    path('detalhe/<slug>/', DetalheProduto.as_view(), name="detalhe"),
]