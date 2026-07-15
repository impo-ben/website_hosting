from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = (
            "full_name",
            "phone",
            "email",
            "subject",
            "message",
        )

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Full Name"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject"
            }),

            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Tell us about your project..."
            }),

        }