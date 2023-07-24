from django.forms import widgets, ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _


from .models import ContactUsFormModel, City, Province


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUsFormModel
        fields = "__all__"
        exclude = ["created"]

    first_name = forms.CharField(
        label=_("نام"),
        widget=forms.TextInput(
            attrs={
                "class": "form-inline d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label=_("نام خانوادگی"),
        widget=forms.TextInput(
            attrs={
                "class": "form-inline d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
    province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        label=_("استان"),
        widget=forms.Select(
            attrs={
                "class": "form-select d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label=_("آدرس ایمیل"),
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
        label=_("موضوع"),
        widget=forms.TextInput(
            attrs={
                "class": "form-inline d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
    message_body = forms.CharField(
        label=_("متن پیام"),
        widget=forms.Textarea(
            attrs={
                "class": "form-inline d-inline-flex form-control",
                "required": "True",
            }
        ),
    )
