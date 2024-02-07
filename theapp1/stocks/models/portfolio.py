from django.db import models


class ExternalSymbol(models.Model):
    external_id = models.BigAutoField(primary_key=True)


class Industry(models.Model):
    name = models.CharField(max_length=100)


class Stock(models.Model):
    symbol_external = models.OneToOneField(ExternalSymbol, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    last_price = models.FloatField()
    market_cap = models.FloatField()
    volume = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    monthly_dividend = models.FloatField()
    yearly_dividend = models.FloatField()


class Investor(models.Model):
    name = models.CharField(max_length=100)


class Dividend(models.Model):
    month = models.CharField(
        max_length=2,
        choices=[
            ("Jan", "Jan"),
            ("Feb", "Feb"),
            ("Mar", "Mar"),
            ("Apr", "Apr"),
            ("May", "May"),
            ("Jun", "Jun"),
            ("Jul", "Jul"),
            ("Aug", "Aug"),
            ("Sep", "Sep"),
            ("Oct", "Oct"),
            ("Nov", "Nov"),
            ("Dec", "Dec"),
        ],
    )
    year = models.IntegerField()
    amount = models.FloatField()


class Portfolio(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    owner = models.ForeignKey(Investor, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateField(auto_now_add=True)
    dividends = models.ManyToManyField(Dividend)
