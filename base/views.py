from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import TaskModel
from django.db.models import Q 

# Create your views here.
@login_required(login_url='login_')
def home(request):
    # record which are active - is_delete should be False
    data=TaskModel.objects.filter(Q(host=request.user) & Q(is_delete=False) & Q(is_complete=False))
    return render(request,'home.html',{'data':data})

@login_required(login_url='login_')
def add(request):
    if request.method=='POST':
        TaskModel.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            host=request.user #we need assign complete currently logedin user object instance
        )
        return redirect('home')
    return render(request,'add.html')

@login_required(login_url='login_')
def complete(request):
    data=TaskModel.objects.filter(Q(host=request.user) & Q(is_complete=True) & Q(is_delete=False))
    return render(request,'complete.html',{'data':data})

@login_required(login_url='login_')
def trash(request):
    #display the instance record where is_delete=True
    data=TaskModel.objects.filter(Q(host=request.user) & Q(is_delete=True))
    return render(request,'trash.html',{'data':data})

@login_required(login_url='login_')
def about(request):
    return render(request,'about.html')

#home page delete button
def delete_h(request,id):
    data=TaskModel.objects.get(id=id)
    data.is_delete=True
    data.save()
    return redirect('trash')

#home page complete button
def complete_h(request,id):
    data=TaskModel.objects.get(id=id)
    data.is_complete=True
    data.save()
    return redirect('complete')

#complete page delete button
def delete_c(request,id):
    data=TaskModel.objects.get(id=id)
    data.is_delete=True
    data.save()
    return redirect('trash')

# complete page restore button
def restore_c(request,id):
    data=TaskModel.objects.get(id=id)
    data.is_complete=False
    data.save()
    return redirect('home')

#trash page delete button
def delete_t(request,id):
    data=TaskModel.objects.get(id=id)
    data.delete()
    return redirect('trash')

#trash page restore button
def restore_t(request,id):
    data=TaskModel.objects.get(id=id)
    data.is_delete=False
    data.save()
    #if the record is getting restored to the complete page then we need to redirect to complete
    #if is_complete =True , it will get restore to complete page
    #if is_complete =False , it will get restore to home page
    if data.is_complete:
        return redirect('complete')
    return redirect('home')

#home page complete all button
def complete_allh(request):
    # fetch the records whose is_delete field is False , is_complete= Fasle and user specific
    # then upadate is_complete field to True
    data=TaskModel.objects.filter(Q(host=request.user) & Q(is_delete=False) & Q(is_complete=False))
    return redirect('complete')

# home page delete all  utton
def delete_allh(request):
    data=TaskModel.objects.filter(Q(host=request.user) & Q(is_delete=False) & Q(is_complete=False)).update(is_delete=True)
    return redirect('trash')


'''
#! 22.7.26
complete page - restore all ,delete all
trash page - restore all , delete all

--In the trash page we 2 types of deleted records
delete directly from the home page
delete from the complete page

-- if the record has been delete from home page i need to restore it to home
--if the record has been delete from the compelete page i need to restore it to complete 

home page - is_complete =False , is_delete =False
complete page - is_complete =True , is_delete=False
trash page - is_complete =False , is_delete =True


#! 
-->Authentication is the process of verifying the indentity 
of auser it checks whether the prrson trying to acess the applicaton is 
really the same person they claim to be

-->AUthorization is the process of deciding what an authenticated 
user is allowed to do inside the application

--> Cookies are samll pieces of data stored in the user's
 browser b y the website

 --> chache is a temporary storage that helps to improve the performance 
 of a website

--> session storage is used to store user data on the server side
 for a limited period of time
 
'''