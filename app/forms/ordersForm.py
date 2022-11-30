from django.forms import ModelForm
from app.models import Order

class OrdersForm(ModelForm):
    
    class Meta: 
        model = Order
        fields = "__all__"