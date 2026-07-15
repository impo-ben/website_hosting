from django import forms
from .models import ServiceInquiry


class ServiceInquiryForm(forms.ModelForm):

    class Meta:

        model = ServiceInquiry

        fields = (
            "full_name",
            "phone",
            "email",
            "company",
            "message",
        )

        widgets = {

            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Full Name",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+91 XXXXX XXXXX",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),

            "company": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Company Name (Optional)",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Tell us about your project...",
                }
            ),

        }