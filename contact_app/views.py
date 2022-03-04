from django.shortcuts import redirect, render
from .models import Name
from .forms import EmailForm,NameForm,PhoneNumbersForm, ScodeForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index(request):
    return render(request, 'contact_app/index.html')

@login_required
def names(request):
    names = Name.objects.filter(owner=request.user).order_by()
    context={'names':names}
    return render(request, 'contact_app/names.html',  context)

@login_required
def name(request,name_id):
    name = Name.objects.get(id=name_id)
    if name.owner != request.user:
        raise Http404
    mail = name.email_set.all()
    phone = name.phonenumbers_set.all()
    context = {
        'name':name,
        'email':mail,
        'mobiles':phone
    }
    return render(request, 'contact_app/name.html',context)

@login_required
def new_name(request):
    if request.method != 'POST':
        form = NameForm()
    else:
        form=NameForm(data=request.POST)
        if form.is_valid():
                new_name=form.save(commit=False)
                new_name.owner = request.user
                new_name.save()
                return redirect('contact_app:info')
    context = {'form':form,}
    return render(request, 'contact_app/new_name.html',context)

@login_required
def new_email(request,name_id):
    name = Name.objects.get(id=name_id)
    if request.method != 'POST':
        form = EmailForm()
    else:
        form = EmailForm(data=request.POST)
        if form.is_valid():
            new_email = form.save(commit=False)
            new_email.person = name
            new_email.save()
            return redirect('contact_app:name', name_id=name_id)
    context = {'name':name, 'form':form}
    return render(request, 'contact_app/new_email.html',context)

@login_required
def new_pnum(request,name_id):
    name = Name.objects.get(id=name_id)
    if request.method != 'POST':
        form = PhoneNumbersForm
    else:
        form = PhoneNumbersForm(data=request.POST)
        if form.is_valid():
            new_pnum = form.save(commit=False)
            new_pnum.person = name
            new_pnum.save()
            return redirect('contact_app:name', name_id=name_id)
    context = {'name':name, 'form':form}
    return render(request, 'contact_app/new_pnum.html',context)

@login_required
def scode(request):
    if request.method != 'POST':
        form = ScodeForm()
    else:
        form=ScodeForm(data=request.POST)
        if form.is_valid():
                scode=form.save(commit=False)
                scode.owner = request.user
                scode.save()
                return redirect('contact_app:index')
    context = {'form':form,}
    return render(request, 'contact_app/scode.html',context)

@login_required
def info(request):
    return render(request,'contact_app/info.html')