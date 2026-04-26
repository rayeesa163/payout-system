from rest_framework import serializers
from .models import Payout


class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = ['id', 'merchant', 'amount_paise', 'status', 'bank_account_id', 'idempotency_key']
        read_only_fields = ['status']