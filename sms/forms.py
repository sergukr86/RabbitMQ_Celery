from django import forms


class SendingForm(forms.Form):
    receiver = forms.CharField(label="receiver", max_length=20)
    message = forms.CharField(label="message", max_length=150)

