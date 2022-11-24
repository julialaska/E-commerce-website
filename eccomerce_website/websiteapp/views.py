from django.shortcuts import render


def frontpage(request):
    return render(request, 'website_app/frontpage.html')
