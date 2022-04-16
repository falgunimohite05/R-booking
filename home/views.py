from django.shortcuts import render
from django.template import loader
from features.models import Members
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .forms import UserLogin,UserReg
from django.contrib import auth
from django.contrib.auth import authenticate,login
#from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, "features/index.html")

    def post(self, request):
        return render(request, "feautures/index.html")

def home(request):
    return render(request,'features/home.html')

class Register(View):
    def get(self, request):
        return render(request, "features/register.html")

    def post(self,request):
        postData = request.POST
        username = postData.get('uname')
        email = postData.get('email')
        password = postData.get('psw')
        print(password)

        # validation
        value = {'username': username, 'email': email}
        member = Members(username=username, email=email, password=password)
        err_msg = self.validateMember(member)

        # saving
        if not err_msg:
            member.password = make_password(member.password)
            member.register()
            request.session['username'] = member.username
            request.session['member'] = member.id

            return redirect('/login')
            #return render(request,"features/login.html")
            #return redirect('features/home.html')

            #return render(request, 'features/home.html')
        else:
            data = {'error': err_msg, 'values': value}
            return render(request, "features/register.html",data)

    def validateMember(self,member):
        err_msg = None
        if (not member.username):
            err_msg = "Name Required!"
        elif not member.validateEmail():
            err_msg = 'Enter valid email'
        elif not member.password:
            err_msg = "please create a password"
        elif len(member.password) < 6:
            err_msg = "Password must be 6 char long"
        elif member.doExists():
            err_msg = 'Email Address Already registered..'
        return err_msg


class Login(View):
    def get(self, request):
        #Login.return_url = request.GET.get('return_url')
        return render(request, "features/login.html")

    def post(self, request):

        username = request.POST.get('uname')
        password = request.POST.get('psw')
        member = Members.get_member_by_uname(username)
        print(username,password)
        print(member)
        err_msg = None
        if member:
            print(member.password)
            flag = check_password(password, member.password)
            print(flag)
            if flag:
                request.session['username'] = member.username
                request.session['member'] = member.id
                return render(request, 'features/home.html')
            else:
                err_msg = 'Username or Password invalid1'
        else:
            err_msg = 'Username or Password invalid2'
        return render(request, 'features/login.html', {'error': err_msg})


def logout(request):
    request.session.clear()
    return render(request, 'features/index.html')


class Contact(View):
    def post(self, request):
        return render(request, "features/contact.html")

    def get(self, request):
        return render(request, "features/contact.html")