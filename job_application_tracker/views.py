from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView
from .models import JobApplication
from .forms import JobApplicationForm


class ApplicataionCreateAndListView(View):
    model = JobApplication
    template_name = "jobs_application_tracker/applications_list.html"
    fields = ["company_name", "job_title", "job_description", "expected_salary"]
    created_at = timezone.now()

    def get(self, request):
        context = {
            "object_list": self.model.objects.filter(user=self.request.user).all()
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.instance.created_at = timezone.now()
            form.instance.user = self.request.user
            form.save()
        return redirect("jobs:list")


class ApplicationDetailView(DetailView):
    model = JobApplication
    template_name = "jobs_application_tracker/application_detail.html"


class ApplicationUpdateView(UpdateView):
    model = JobApplication
    template_name = "jobs_application_tracker/application_edit.html"
    fields = ["company_name", "job_title", "job_description", "expected_salary"]


class ApplicationDeleteView(DeleteView):
    model = JobApplication
    success_url = reverse_lazy("jobs:list")
