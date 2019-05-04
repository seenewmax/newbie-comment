from django.shortcuts import render


def main(request):
    return render(request, 'html/index.html')

def signup(request):
    return render(request, 'signup.html')
    
def help(request):
    return render(request, 'help.html')

def host_mogakco(request):
    return render(request, 'event/templates/new.html')

def show_by_region(request):
    return render(request, 'region.html')

def show_by_subject(request):
    return render(request, 'subject.html')

def subscribe(request):
    return render(request, 'html/subscribe.html')

def somewhere(request):
    return render(request, 'html/somewhere.html')