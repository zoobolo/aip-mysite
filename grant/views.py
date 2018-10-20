from django.http import HttpResponse 
from django.template import loader
from django.shortcuts import render, redirect
#from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import Airport
from django.views import generic    


def index(request):
    if not request.user.is_authenticated():
        return redirect('login')
    
    airport_list = Airport.objects.order_by('airport_name')
    
    context = {'airport_list': airport_list}
   
    return render(request, 'home.html', context)

# def home(request):
#     if not request.user.is_authenticated():
#         return redirect('login')
        
#     return render(request, 'grant/home.html')

class getAirportListView(generic.ListView):
     model = Airport


#class getPeterAirport(request):
#    peter_airport = Airport.object.filter(ado_pm="Peter Hughes").order_by('airport_name')
#    return render(request, 'grant/userhome.html')

#def index(request):
#    return render(request, 'grant/home.html')
#   return render(request, 'grant/login.html')




#def register(request):
#    return render(request, 'grant/home.html')
#    if request.method == "POST": 
#      form = UserCreationForm(request.POST)
    #   if form.is_valid():
    #       form.save()
    #       return redirect('/grant')
    # else:
    #     form = UserCreationForm()
    #     args = {'form': form}
    # return render(request, 'grant/reg_form.html', args)
        