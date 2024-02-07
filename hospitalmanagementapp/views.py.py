from django.shortcuts import render, redirect
from hospitalmanagementapp.forms import PatientForm
from hospitalmanagementapp.models import Patient

def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")
def submit(request):
    return render(request,"submit.html")

def pat(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/submit")
            except:
                pass
    else:
        form = PatientForm()
    return render(request,"index.html", {'form':form})
def show(request):
    patients = Patient.objects.all()
    return render(request,"show.html", {'patients': patients})
def edit(request, id):
    patient = Patient.objects.get(id=id)
    return render(request,"edit.html",{'patient' : patient})
def update(request,id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(request.POST, instance= patient)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"edit.html",{'patient': patient})
def delete(request,id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect("/show")
