from django.shortcuts import render, redirect
from .models import Journal
from .forms import JournalForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def journal_data_all(request):
    journals = Journal.objects.all()
    return render(request, 'data.html', {'journal_entries': journals})

@login_required
def journal_data(request):
    journals = Journal.objects.filter(username=request.user)
    return render(request, 'data.html', {'journal_entries': journals})

@login_required
def add_entry(request):   
    if request.method == 'POST':         
        form = JournalForm(request.POST)               
        if form.is_valid():
            # Extract data from cleaned form
            title = form.cleaned_data['title']
            day_type = form.cleaned_data['day_type']
            day_date = form.cleaned_data['day_date']
            description = form.cleaned_data['description']
            day_rate =form.cleaned_data['day_rate']
    
            # Create a new JournalEntry object and save it
            journal_entry = Journal(title=title, day_type=day_type,day_date=day_date, description=description,day_rate=day_rate, username=request.user)             
            journal_entry.save()             
            return redirect('/crudapp/data')
    else:         
        form = JournalForm()     
        return render(request, 'add_entry.html', {'form': form})

@login_required    
def edit_entry(request, id):
    entry = Journal.objects.get(id=id)
    journal_entry = {'title': entry.title, 'day_type': entry.day_type,'day_date': entry.day_date, 'description': entry.description,'day_rate': entry.day_rate}     
    if request.method == 'POST':
        form = JournalForm(request.POST)   
        if form.is_valid():
            entry.title = form.cleaned_data['title']
            entry.day_type = form.cleaned_data['day_type']
            entry.day_date = form.cleaned_data['day_date']
            entry.description = form.cleaned_data['description']
            entry.day_rate = form.cleaned_data['day_rate']
            entry.username=request.user
            entry.save()
            return redirect('/crudapp/data')      
        #form = JournalForm(request.POST, initial=journal_entry)         
    else:   
        form = JournalForm(initial=journal_entry)              
        return render(request, 'edit_entry.html', {'form': form})

@login_required
def delete_entry(request, id):
    entry = Journal.objects.get(id=id)
    entry.delete()
    return redirect('/crudapp/data')
   