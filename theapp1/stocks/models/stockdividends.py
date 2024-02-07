# from django.contrib.auth.models import User
from django.db import models
from models.stockportfolio import StockPortfolio


class StockDividend(models.Model):
    symbol = models.OneToOneField(StockPortfolio, on_delete=models.CASCADE, default=0)
    dividend_amount = models.FloatField(default=0, null=True)
    dividend_amount_in_euro = models.FloatField(default=0, null=True)  # currency
    dividend_declaration_date = models.DateField(null=True)
    dividend_ex_date = models.DateField(null=True)
    dividend_record_date = models.DateField(null=True)
    dividend_payment_date = models.DateField(null=True)
    dividend_currency_symbol = models.CharField(max_length=20, null=True)
    dividend_pay_rate = models.CharField(
        max_length=2,
        choices=[("0", "0"), ("4", "4"), ("12", "12"), ("1", "1"), ("2", "2")],
    )
    dividend_proximet_in_year = models.FloatField(default=0, null=True)
    dividend_proximet_in_month = models.FloatField(default=0, null=True)
    dividend_proximet_in_year_in_euro = models.FloatField(
        default=0, null=True
    )  # currency
    dividend_proximet_in_month_in_euro = models.FloatField(
        default=0, null=True
    )  # currency
