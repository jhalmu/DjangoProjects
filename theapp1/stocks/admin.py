from django.contrib import admin
from .models.stockportfolio import StockPortfolio
from .models.stockitem import StockItem
# from models.stockdividend import StockDividend

admin.site.register(StockItem)
admin.site.register(StockPortfolio)
# admin.site.register(StockDividend)
