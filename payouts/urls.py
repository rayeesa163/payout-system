from django.urls import path
from .views import CreatePayoutView, PayoutDetailView, ProcessPayoutView, PayoutListView

urlpatterns = [
    path('payouts/', CreatePayoutView.as_view()),
    path('payouts/all/', PayoutListView.as_view()),
    path('payouts/<int:pk>/', PayoutDetailView.as_view()),
    path('payouts/<int:pk>/process/', ProcessPayoutView.as_view()),
]