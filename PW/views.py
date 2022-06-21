from django.shortcuts import render

# Create your views here.
# def PW(request):
#     return render(request, 'PW.html', {})

def photo(request):
    return render(request, 'photo.html')

def Student(request):
    return render(request, 'Student.html')

def Main(request):
    return render(request, 'Main.html')

def Homepage(request):
    return render(request, 'Homepage.html')

def Web(request):
    return render(request, 'Web.html')

def Marketing(request):
    return render(request, 'Marketing.html')