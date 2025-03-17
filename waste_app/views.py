from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
from .models import FarmerQuery
from django.contrib import messages



def home(request):
    return render(request, "waste_app/home.html")



def query_form(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        contact = request.POST.get("contact", "").strip()
        query_text = request.POST.get("query_text", "").strip()
        voice_message = request.FILES.get("voice_message")

        if not name or not contact:
            messages.error(request, "Name and contact details are required.")
            return render(request, "query.html")

        query = FarmerQuery.objects.create(
            name=name, contact=contact, query_text=query_text, voice_message=voice_message
        )
        messages.success(request, "Your query has been submitted successfully!")
        return redirect("home")

    return render(request, "waste_app/query.html")
    

# View all blogs
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at').distinct()
    return render(request, "waste_app/blogs_list.html", {"blogs": blogs})

# Add a new blog
def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    else:
        form = BlogForm()
    return render(request, "waste_app/add_blog.html", {"form": form})

# View a single blog post
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "waste_app/blog_detail.html", {"blog": blog})


def Contact(request):
    return render(request, "waste_app/conversion_guides.html")


def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blog_list')