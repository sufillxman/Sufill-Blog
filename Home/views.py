from django.shortcuts import render, redirect, get_object_or_404
from .forms import blogform
from .models import BlogModel
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    context = {'blogs': BlogModel.objects.all().order_by('-created_at')} # Latest blog upar aayega
    return render(request, 'Home/home.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'Home/login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'Home/register.html')

# --- SECURE VIEWS START HERE ---

@login_required(login_url='/login/')
def add_blog(request):
    context = {'form': blogform()}
    try:
        if request.method == 'POST':
            # Ab hume alag se title/image nikalne ki zaroorat nahi
            form = blogform(request.POST, request.FILES)
            
            if form.is_valid():
                # Commit=False ka matlab: Abhi ruk jao, User add karna baki hai
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                
                messages.success(request, "Blog added successfully!")
                return redirect('/see-blog/')
            else:
                messages.error(request, "Form is invalid. Please check inputs.")
                
    except Exception as e:
        print(e)
        messages.error(request, "Something went wrong.")

    return render(request, 'Home/add_blog.html', context)

@login_required(login_url='/login/')
def blog_update(request, slug):
    context = {}
    try:
        blog_obj = get_object_or_404(BlogModel, slug=slug)

        # Security Check: Kya ye blog isika hai?
        if blog_obj.user != request.user:
            messages.warning(request, "You cannot edit someone else's blog.")
            return redirect('/')

        if request.method == 'POST':
            form = blogform(request.POST, request.FILES, instance=blog_obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Blog updated successfully!")
                return redirect('/see-blog/')
        
        # GET request
        context['blog_obj'] = blog_obj
        context['form'] = blogform(instance=blog_obj)

    except Exception as e:
        print(e)

    return render(request, 'Home/update_blog.html', context)

@login_required(login_url='/login/')
def blog_delete(request, id):
    try:
        blog_obj = get_object_or_404(BlogModel, id=id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
            messages.success(request, "Blog deleted successfully!")
        else:
            messages.warning(request, "You cannot delete this blog.")
            
    except Exception as e:
        print(e)
    return redirect('/see-blog/')

@login_required(login_url='/login/')
def see_blog(request):
    context = {}
    try:
        blog_objs = BlogModel.objects.filter(user=request.user).order_by('-created_at')
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)
    return render(request, 'Home/see_blog.html', context)

# --- PUBLIC VIEWS ---

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = get_object_or_404(BlogModel, slug=slug)
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'Home/blog_detail.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('/')