from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
           return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func   


# We are trying to restrict access of users to certain pages like home page.
# User is meant to access only customer page.
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):     
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to access this page')
            
        return wrapper_func
    return decorator

#For Admins

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'customer':
            return redirect('user-page')
        
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func       
            
        
        
    
    