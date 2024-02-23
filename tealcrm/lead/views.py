from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import AddLeadForm

@login_required
def add_lead(request):
    
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            
            return redirect('dashboard')
    else: 
        form = Add
    form = AddLeadForm()
    
    return render(request, 'lead/add_lead.html',{
        'form': form
    })