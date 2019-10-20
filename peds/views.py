from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'peds/mailbox.html')

@login_required
def read_mail(request):
    return render(request, 'peds/read-mail.html')

@login_required
def compose(request):
    return render(request, 'peds/compose.html')

@login_required
def profile(request):
    return render(request, 'peds/profile.html')
