from django.db import models
from django.db.models import Sum, Case, When, IntegerField, F


class Merchant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_balance(self):
        result = self.ledgerentry_set.aggregate(
            balance=Sum(
                Case(
                    When(type__in=['CREDIT', 'RELEASE'], then=F('amount_paise')),
                    When(type__in=['DEBIT', 'HOLD'], then=-1 * F('amount_paise')),
                    output_field=IntegerField()
                )
            )
        )
        return result['balance'] or 0


class LedgerEntry(models.Model):
    TYPE_CHOICES = [
        ('CREDIT', 'Credit'),
        ('DEBIT', 'Debit'),
        ('HOLD', 'Hold'),
        ('RELEASE', 'Release'),
    ]

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount_paise = models.BigIntegerField()
    reference_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.merchant.name} - {self.type} - {self.amount_paise}"
class Payout(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    amount_paise = models.BigIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    bank_account_id = models.CharField(max_length=100)
    idempotency_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.merchant.name} - {self.amount_paise} - {self.status}"