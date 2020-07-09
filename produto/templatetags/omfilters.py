from django.template import Library
from utils import formatapreco
from utils import cartsum


register = Library()


@register.filter
def formata_preco(val):
    return formatapreco.formata_preco(val)

@register.filter
def cart_total_sum(carrinho):
    return cartsum.cart_total_sum(carrinho)

@register.filter
def cart_totals(carrinho):
    return cartsum.cart_totals(carrinho)