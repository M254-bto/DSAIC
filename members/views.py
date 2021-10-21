from django.shortcuts import render
from .forms import MemberCreateForm
from django.shortcuts import redirect
from django.urls import reverse
from .models import MemberModel
from django.views import generic


def landing_view(request):
    return render(request, 'members/landing.html')


def new_member(request):
    form = MemberCreateForm()
    if request.method == 'POST':
        form = MemberCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members:mem-list')

    return render(request, 'members/member_create.html', context={
        "form": form
    })


def member_list(request):
    member = MemberModel.objects.all()
    return render(request, 'members/list.html', context={
        "member": member
    })


#detail views
        #function-based view

def member_detail(request, pk):
    member = MemberModel.objects.get(id=pk)
    return render(request, 'members/member_detail.html', context={
        "member": member
    })

        # generic detail view

class MembersDetailView(generic.DetailView):
    template_name = 'members/member_detail.html'
    context_object_name = 'member'

    def get_queryset(self):
        return MemberModel.objects.all()


#update views

        #function-based view

def member_update(request, pk):
    member = MemberModel.objects.get(id=pk)
    form = MemberCreateForm(instance=member)
    if request.method == 'POST':
        form = MemberCreateForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            redirect('members:mem-detail')
            
    return render(request, 'members/member_update.html', context={
        "form": form,
        "member": member

    })
        #generic update view

class MemberUpdateView(generic.UpdateView):
    form_class = MemberCreateForm
    template_name = 'members/member_update.html'
    

    def get_queryset(self):
        return MemberModel.objects.all()

    def get_success_url(self):
        return redirect('members:mem-list')