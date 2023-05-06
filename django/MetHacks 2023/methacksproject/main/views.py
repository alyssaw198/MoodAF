from django.shortcuts import render
from django.http import HttpResponse
from .models import PatientData
from .forms import PatientForm
from django.contrib import messages
from django.db.models import Q
from methacksproject.globals import GLOBAL_FNAME, GLOBAL_LNAME


#Where ALL the python functions are written

def home(request):
    return render(request, 'index.html', {})


def form(request):
    if request.method == "POST":
        submission = PatientForm(request.POST or None)
        if submission.is_valid():
            submission.save()
            patientfName = request.POST['fname']
            patientlName = request.POST['lname']
            date = request.POST['date']
            return analyzeEntry(request, patientfName, patientlName, date)
        else:
            return render(request, 'form.html', {})
    else:
        return render(request, 'form.html', {})
    

def analyzeEntry(request, fname, lname, date):
    all_entries = PatientData.objects.filter(Q(fname__icontains = fname) | Q(lname__icontains = lname) | Q(date__icontains = date))
    #COHERE CODE, OR LINK FUNCTION THAT CLASSIFIES IT
    #return cohere's analysis
    return render(request, "postForm.html", {'entries': all_entries})
    #return all_entries
        

def postForm(request, originalEntries, analyzedEntries):
    return render(request, "postForm.html", {'entries': originalEntries, 'analyzed': analyzedEntries})


#Function for all entries from login page
def summary(request):
    patientfName = request.POST['fname']
    patientlName = request.POST['lname']
    global GLOBAL_FNAME
    GLOBAL_FNAME = patientfName
    global GLOBAL_LNAME
    GLOBAL_LNAME = patientlName
    #viewEntries(request, patientfName, patientlName)
    #extract all entries under firstname and lastname
    #call a function that extracts and formats all entries under fname and lname
    return render(request, 'summary.html', {})

def viewEntries(request):
    all_entries = PatientData.objects.filter(Q(fname__icontains = GLOBAL_FNAME) | Q(lname__icontains = GLOBAL_LNAME))
    return render(request, 'index.html', {})

#TODO: function that allows patient to access their journal entries (should be saved under their name) 'LOGIN' page
#this should be associated with the home page

#TODO: submit form function, if all the entires are valid in the journal entry, allows the form to be submitted and saved into database

#TODO: function COHERE API - summarize journal entry inputs 

#TODO: function COHERE API - classify journal entry inputs

#TODO: function to organize all the outputs of the cohere API model

#TODO: function display summarized and mood of journal entry on webpage - could be any sort of display

#TODO: create other functions to change the html view of the webpage if we wanna do different page links or tabs etc

#TODO: function to summarize ALL the journal entry data from each patient (this is more for healthcare research use I guess)


#EXTRAS
#TODO: Personalizable journal entries page? (this would be cool but IDK how to do this at all)
#TODO: Google map API to gather location information for healthcare research purposes
#TODO: voice entry for children (attached to the form, not sure how to do this though)
#TODO: 'Make an Account' page, where the patient makes their account, or we can just do, when a new name is submitted in the form, a new 'Patient' is entered
