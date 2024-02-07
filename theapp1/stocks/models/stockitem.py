from django.db import models
from django.utils.translation import gettext_lazy as _


CURRRENCY_CHOICES = (
    ("USD", "USD"),
    ("EUR", "EUR"),
    ("SEK", "SEK"),
    ("CAD", "CAD"),
    ("GBP", "GBP"),
    ("AUD", "AUD"),
    ("NOK", "NOK"),
    ("DKK", "DKK"),
    ("HKD", "HKD"),
    # ('JPY', 'JPY'),
    # ('CHF', 'CHF'),
    # ('CNY', 'CNY'),
    # ('HUF', 'HUF'),
    # ('ILS', 'ILS'),
    # ('INR', 'INR'),
    # ('ISK', 'ISK'),
    # ('KRW', 'KRW'),
    # ('MXN', 'MXN'),
    # ('MYR', 'MYR'),
    # ('NZD', 'NZD'),
    # ('PLN', 'PLN'),
    # ('SGD', 'SGD'),
    # ('THB', 'THB'),
    # ('TRY', 'TRY'),
    # ('TWD', 'TWD'),
    # ('ZAR', 'ZAR'),
)

SECTOR_CHOICES = (
    (_("Not set"), "Not set"),
    (_("Energy"), "Energy"),
    (_("Materials"), "Materials"),
    (_("Industrials"), "Industrials"),
    (_("Utilities"), "Utilities"),
    (_("Healthcare"), "Healthcare"),
    (_("Financials"), "Financials"),
    (_("Consumer Discretionary"), "Consumer Discretionary"),
    (_("Consumer Staples"), "Consumer Staples"),
    (_("Information Technology"), "Information Technology"),
    (_("Communication Services"), "Communication Services"),
    (_("Real Estate"), "Real Estate"),
)


class StockItem(models.Model):
    ticker = models.CharField(_("Ticker"), max_length=6)
    ISIN = models.CharField(max_length=12, null=True, unique=True)
    currency = models.CharField(
        _("Currency"),
        choices=CURRRENCY_CHOICES,
        max_length=4,
        default="USD",
        blank="USD",
    )
    sector = models.CharField(
        _("Sector"),
        choices=SECTOR_CHOICES,
        max_length=20,
        default="Not set",
        blank="Not set",
    )

    class Meta:
        verbose_name = _("stock item")
        verbose_name_plural = _("stock items")

    def __str__(self):
        return self.ticker.upper()

    def number_of_instruments(self):
        return StockItem.objects.count()

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("stock_detail", kwargs={"ticker": str(self.slug)})
