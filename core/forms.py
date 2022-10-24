from django import forms


class ContactUsForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email_address = forms.EmailField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
