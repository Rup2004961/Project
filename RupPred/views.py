from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import pickle 
import os


model_path = os.path.join(settings.BASE_DIR, "rfc.pkl")


with open(model_path,"rb") as file :
   model = pickle.load(file)




def home(request):
    pred = None
    if request.method == "POST":
        longitude = request.POST['longitude']
        soil_moisture = request.POST['soil_moisture']
        temperature = request.POST['temperature']
        yeild_value = request.POST['yeild']
        env = [[longitude,soil_moisture,temperature,yeild_value]]
        pred = model.predict(env)
    context = {
        "prediction":pred
    }
    return render(request, "home.html", context)


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

