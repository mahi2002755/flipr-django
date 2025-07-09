from django.shortcuts import render, redirect
from PIL import Image
import os
from django.conf import settings
from .models import Project, Client, Contact, Newsletter
from .forms import ContactForm, NewsletterForm, ProjectForm, ClientForm

# Helper function to crop and save images
def crop_image(image_field, target_path):
    img = Image.open(image_field)
    cropped_img = img.resize((450, 350))  # Resize or crop logic
    cropped_img.save(target_path)

# Landing Page

def index(request):
    projects = Project.objects.all()
    clients = Client.objects.all()
    contact_form = ContactForm()
    newsletter_form = NewsletterForm()
    return render(request, 'index.html', {
        'projects': projects,
        'clients': clients,
        'contact_form': contact_form,
        'newsletter_form': newsletter_form,
    })

def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')

# Admin Views

def admin_panel(request):
    contacts = Contact.objects.all()
    newsletters = Newsletter.objects.all()
    return render(request, 'admin_panel.html', {
        'contacts': contacts,
        'newsletters': newsletters
    })

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            image = request.FILES.get('image')
            filename = image.name
            save_path = os.path.join(settings.MEDIA_ROOT, 'projects', filename)
            crop_image(image, save_path)
            project.image = f'projects/{filename}'
            project.save()
            return redirect('admin_panel')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save(commit=False)
            image = request.FILES.get('image')
            filename = image.name
            save_path = os.path.join(settings.MEDIA_ROOT, 'clients', filename)
            crop_image(image, save_path)
            client.image = f'clients/{filename}'
            client.save()
            return redirect('admin_panel')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})