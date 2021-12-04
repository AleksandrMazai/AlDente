from django import forms
from .models import Contact
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(attrs={
                'type': 'text',
                'id': 'name',
                'class': 'form-control',
                'placeholder': 'Имя',
                'required': 'required'

            }),
            'phone': PhoneNumberInternationalFallbackWidget(attrs={
                'type': 'tel',
                'id': 'tel',
                'class': 'form-control',
                'placeholder': 'Номер телефона',
                'required': 'required'
            }),
            'message': forms.Textarea(attrs={
                'name': 'message',
                'id': 'message',
                'class': 'form-control',
                'rows': '4',
                'placeholder': 'Сообщение'
            })
        }
