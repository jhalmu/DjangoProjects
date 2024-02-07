from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .stockitem import StockItem


class StockPortfolio(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ticker = models.ForeignKey(
        StockItem, related_name="Ticker", on_delete=models.SET_NULL, null=True
    )
    currency = models.ForeignKey(
        StockItem, related_name="Currency", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(_("Name"), max_length=100, null=True)
    quantity = models.FloatField(_("Quantity"), default=0, null=True)
    # ISIN = models.CharField(max_length=12, null=False, unique=True)
    # country_code = models.CharField(max_length=4, null=True)

    # currency = models.CharField(_("Currency"), max_length=100)

    avg_price = models.FloatField(_("Avg price"), default=0, null=True)

    total_price = models.FloatField(_("Total"), default=0, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner
