from django.http import HttpResponse
from django.shortcuts import render
from upload_download.functions import handle_uploaded_file
from upload_download.forms import StudentForm

def index(request):
      return render(request,"upload_download/indexi.html")

def indexi(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"upload_download/upload_file.html",{'form':student}) 