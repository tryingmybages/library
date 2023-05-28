from django.shortcuts import render,redirect
from .models import *
from .forms import Form,Categoryform
# Create your views here.
def index(request):

    if request.method == 'POST':
        add_book= Form(request.POST or None,request.FILES)
        if add_book.is_valid():
            add_book.save()
     

        add_cat= Categoryform(request.POST)    
        if add_cat.is_valid():
            add_cat.save()
          
    context = {
        'booknumber':str(Book.objects.filter(active= True).count()),
        'bookav':str(Book.objects.filter(status= 'availble').count()),
        'bookso':str(Book.objects.filter(status= 'seald').count()),
        'bookr':str(Book.objects.filter(status= 'retaled').count()),
        'book':Book.objects.all(),'cat':Categrymodel.objects.all(),'form':Form(),
        'fromcat':Categoryform()
    }
        
    return render(request,'pages/index.html',context)


def books(request):
    return render(request,'pages/books.html',{'book':Book.objects.all(),'cat':Categrymodel.objects.all()})




def delete(request,id):
    book_delete = Book.objects.get(id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('index')


    return render(request,'pages/delete.html')



def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save= Form(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid:
            book_save.save()
            return redirect('index')
    else:
        book_save = Form(instance=book_id)
    context = {
        'form':book_save,
    }


    return render(request,'pages/update.html',context)
