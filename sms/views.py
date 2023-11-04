from django.shortcuts import render
from .tasks import send_sms
from .forms import SendingForm


# Create your views here.
def main(request):
    if request.method == "GET":
        form = SendingForm()
        return render(request, "main.html", {"form": form})
    form = SendingForm(request.POST)
    if form.is_valid():
        receiver = form.cleaned_data["receiver"]  # Access the cleaned data using the form's cleaned_data attribute
        message = form.cleaned_data["message"]
        send_sms.delay(receiver, message)
    return render(request, "thank_you.html")


def thanks(request):
    return render(request, "thank_you.html")
