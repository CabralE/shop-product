from django.forms import ModelForm
from .models import SubCart

class QuantityForm(ModelForm):
  class Meta:
    model = SubCart
    fields = ['quantity']