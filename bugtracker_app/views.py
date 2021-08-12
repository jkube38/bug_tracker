from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


from bugtracker_app.forms import LoginForm, CreateTicketForm
from bugtracker_app.models import Tickets, CustomUserModel


# Create your views here.
def login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return redirect(reverse('home'))
    form = LoginForm()
    context.update({'form': form})
    return render(request, 'index.html', context)


@login_required
def home_view(request):
    all_tickets = Tickets.objects.all()
    return render(request, 'home.html', {'all_tickets': all_tickets})


@login_required
def create_ticket_view(request):
    context = {}
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tickets.objects.create(
                title=data['title'],
                description=data['description'],
                filed_by=request.user,
                status='New'
            )
            return redirect(reverse('home'))

    form = CreateTicketForm()
    context.update({'form': form})
    return render(request, 'createticket.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


# Help from stackoverflow with action drop down menu in the
# ticket.html (answer provided by Uday Kiran)
@login_required
def ticket_view(request, title):
    context = {}
    title = Tickets.objects.get(title=title)
    context = {'title': title}
    return render(request, 'ticket.html', context)


def edit_view(request, title):
    context = {}
    title = Tickets.objects.get(title=title)
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title.title = data['title']
            title.description = data['description']
            title.save()
            return redirect('ticket', title.title)

    form = CreateTicketForm()
    context = {'form': form}
    return render(request, 'edit.html', context)


def assigned_view(request, title):
    title = Tickets.objects.get(title=title)
    title.assigned_to = request.user
    title.status = 'In Progress'
    title.save()
    return redirect('ticket', title.title)


def invalid_view(request, title):
    title = Tickets.objects.get(title=title)
    title.status = 'Invalid'
    title.assigned_to = None
    title.completed_by = None
    title.save()
    return redirect('ticket', title.title)


def done_view(request, title):
    title = Tickets.objects.get(title=title)
    title.status = 'Done'
    title.completed_by = title.assigned_to
    title.assigned_to = None
    title.save()
    return redirect('ticket', title.title)


def return_view(request, title):
    title = Tickets.objects.get(title=title)
    title.status = 'New'
    title.completed_by = None
    title.assigned_to = None
    title.save()
    return redirect('ticket', title.title)


def user_view(request, username):
    context = {}
    username = CustomUserModel.objects.get(username=username)
    user_filed = Tickets.objects.filter(filed_by=username)
    user_completed = Tickets.objects.filter(completed_by=username)
    user_progress = Tickets.objects.filter(assigned_to=username)
    context = {
        'username': username,
        'user_filed': user_filed,
        'user_completed': user_completed,
        'user_progress': user_progress
        }
    return render(request, 'userprofile.html', context)
