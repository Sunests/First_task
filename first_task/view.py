from django.shortcuts import render


app_name = 'hotels'


def base_hotels(request):
    return render(request, 'base.html')
