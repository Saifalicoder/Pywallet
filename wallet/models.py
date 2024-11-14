from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email}'s Wallet"


TRANSACTION_TYPES = (
    ('add', 'Add'),
    ('remove', 'Remove'),
)

class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10, 
        choices=TRANSACTION_TYPES, 
        default='add'
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction of {self.amount} for {self.user.email}"