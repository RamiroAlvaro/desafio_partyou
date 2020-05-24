from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Identificador", max_length=255)
    description = models.TextField("Descrição", blank=True)
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2)

    created = models.DateTimeField("Criado em", auto_now_add=True)
    modified = models.DateTimeField("Modificado em", auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        (0, "Em depósito"),
        (1, "Em trânsito"),
        (2, "Entregue"),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="Usuário")
    status = models.IntegerField("Rastreamento", choices=STATUS, default=0, blank=True)

    created = models.DateTimeField("Criado em", auto_now_add=True)
    modified = models.DateTimeField("Modificado em", auto_now=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido número {self.id}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name="Pedido", related_name="items", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name="Produto", on_delete=models.PROTECT)
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Quantidade", default=1)

    class Meta:
        verbose_name = "Item do pedido"
        verbose_name_plural = "Itens dos pedidos"
        unique_together = ("order", "product")

    def __str__(self):
        return f"Número do pedido: {self.order} | Produto: {self.product} | Quantidade: {self.quantity} | " \
               f"Preço: R${self.price} "
