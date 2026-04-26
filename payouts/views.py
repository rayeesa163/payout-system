from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import time

from .models import Payout


# 👉 Home page
def home(request):
    return render(request, 'index.html')


# 👉 Create payout
@method_decorator(csrf_exempt, name='dispatch')
class CreatePayoutView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        merchant = request.data.get("merchant")
        amount = request.data.get("amount_paise")
        bank = request.data.get("bank_account_id")

        payout = Payout.objects.create(
            merchant_id=merchant,
            amount_paise=int(amount),
            bank_account_id=bank,
            status="pending"
        )

        return Response({
            "id": payout.id,
            "status": payout.status
        })


# 👉 View payout
class PayoutDetailView(APIView):
    def get(self, request, pk):
        try:
            payout = Payout.objects.get(id=pk)
            return Response({
                "id": payout.id,
                "status": payout.status,
                "amount": payout.amount_paise
            })
        except Payout.DoesNotExist:
            return Response({"error": "Not found"}, status=404)


# 👉 Process payout (pending → processing → success)
@method_decorator(csrf_exempt, name='dispatch')
class ProcessPayoutView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, pk):
        try:
            payout = Payout.objects.get(id=pk)

            payout.status = "processing"
            payout.save()

            time.sleep(2)  # simulate delay

            payout.status = "success"
            payout.save()

            return Response({
                "id": payout.id,
                "status": payout.status
            })

        except Payout.DoesNotExist:
            return Response({"error": "Not found"}, status=404)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payout

class PayoutListView(APIView):
    def get(self, request):
        payouts = Payout.objects.all().order_by('-id')
        data = [
            {
                "id": p.id,
                "status": p.status,
                "amount": p.amount_paise,
                "merchant": p.merchant_id
            }
            for p in payouts
        ]
        return Response(data)