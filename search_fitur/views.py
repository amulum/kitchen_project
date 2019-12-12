from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'search_fitur/index.html', {'users': users})

# def personal_info(request):
#     current_user = request.User
#     prof_pict = request.POST['prof_pict']
#     jabatan = request.POST['jabatan']
#     socmed_link = request.POST['socmedlink']
#     new_info = PersonalInfo(user_id=current_user.id, jabatan=jabatan, socmed_link=socmed_link, prof_pict=prof_pict)
#     return render(request, 'search_fitur/index.html', {})

def register(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            return redirect('login')
    else:
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, 'register.html', {'u_form': u_form, 'p_form': p_form})