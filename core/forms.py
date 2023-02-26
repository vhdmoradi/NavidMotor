from django.forms import widgets, ModelForm
from django import forms


from .models import ContactUsFormModel, City, Province


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUsFormModel
        fields = "__all__"
        exclude = ["created"]

    first_name = forms.CharField(
        label="نام",
        widget=forms.TextInput(
            attrs={
                "class": "form-inline d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="نام خانوادگی",
        widget=forms.TextInput(
            attrs={
                "class": "form-inline d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
    province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        label="استان",
        widget=forms.Select(
            attrs={
                "class": "form-select d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="آدرس ایمیل",
        widget=forms.TextInput(
            attrs={
                "class": "form-inline d-inline-flex form-control",
                "required": "True",
                "placeholder": "email@test.com",
                "dir": "ltr",
            }
        ),
    )
    subject = forms.CharField(
        label="موضوع",
        widget=forms.TextInput(
            attrs={
                "class": "form-inline d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
    message_body = forms.CharField(
        label="متن پیام",
        widget=forms.Textarea(
            attrs={
                "class": "form-inline d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
