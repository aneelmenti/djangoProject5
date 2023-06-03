from django.shortcuts import render
from django.views import View
from django.http import  HttpResponse


# Create your views here.

class home(View):
    def get(self,request):
        return render(request,'home.html')
class GetInput(View):
    def get(self,requuest):
        return render(requuest,'GetInput.html')
class PostInput(View):
    def Post(self,request):
       return render(request,'PostInput')


class Add(View):
    def get(self,request):
        p=int(request.GET['t1'])
        j=int(request.GET['t2'])
        r=p+j
        return HttpResponse("the sum is :"+str)




    def post(self,request):
        x=int(request.POST['t1'])
        y=int(request.POST['t2'])
        z=x+y
        return HttpResponse("the sum is :"+str)