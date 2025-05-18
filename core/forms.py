from django import forms

from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'})
    )
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'})
    )
    website = forms.URLField(
        required=False,
        max_length=255,
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your Website'})
    )
    phone_number = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'})
    )
    comment = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment'})
    )
  





