from django import forms
from .models import WasteRequest

class WasteRequestForm(forms.ModelForm):
    class Meta:
        model = WasteRequest
        fields = ['category', 'description', 'address', 'quantity']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 2 bags, 10kg'}),
        }