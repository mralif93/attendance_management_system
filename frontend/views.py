from django.shortcuts import render

# Create your views here.
def LandingView(request):
  context = {}
  return render(request, 'frontend/landing.html', context)