from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
from forms import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import Http404
from django.shortcuts import redirect
from matcher.models import *
from django.conf import settings  # import the settings file
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.decorators import login_required

# import generic views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.core.urlresolvers import reverse_lazy
import random, string
from utils import *

# import emailing library
from django.core.mail import EmailMessage

class IndustriesView(ListView):
    template_name = 'industries.html'
    model = Industries

class IndustryCreate(CreateView):
    template_name = 'create.html'
    model = Industries
    form_class = IndustriesForm
    success_url = '/matcher/industries'
    
class UpdateIndustry(UpdateView):
    template_name = 'update.html'
    model = Industries
    success_url = '/matcher/industries'

class DeleteIndustry(DeleteView):
    model = Industries
    template_name = 'industry_confirm.html'  
    
    def get_success_url(self):
        return reverse_lazy('industries_index')


# Job Types
class JobTypesView(ListView):
    template_name = 'jobtypes.html'
    model = JobTypes

class JobTypesCreate(CreateView):
    template_name = 'create.html'
    model = JobTypes
    form_class = JobTypesForm
    success_url = '/matcher/jobTypes'


class UpdateJobTypes(UpdateView):
    template_name = 'update.html'
    model = JobTypes
    success_url = '/matcher/jobTypes'
    
class DeleteJobTypes(DeleteView):
    model = JobTypes
    template_name = 'jobtype_delete.html'  
    
    def get_success_url(self):
        return reverse_lazy('jobtypes_index')


# Channels
class ChannelsView(ListView):
    template_name = 'channels.html'
    model = Channels

class ChannelsCreate(CreateView):
    template_name = 'create.html'
    model = Channels
    form_class = ChannelsForm
    success_url = '/matcher/channels'


class UpdateChannels(UpdateView):
    template_name = 'update.html'
    model = Channels
    success_url = '/matcher/channels'
    
class DeleteChannels(DeleteView):
    model = Channels
    template_name = 'channel_delete.html'  
    
    def get_success_url(self):
        return reverse_lazy('channels_index')



# Users
class UsersView(ListView):
    template_name = 'users.html'
    model = Users

class UsersCreate(CreateView):
    template_name = 'create.html'
    model = Users
    form_class = UsersForm
    
    success_url = '/matcher/users'
  
    def form_valid(self, form_class):
        try: 
            s = string.lowercase + string.digits
            password = ''.join(random.sample(s, 10))
            user = User.objects.create_user(form_class.cleaned_data['emailaddress'], form_class.cleaned_data['emailaddress'], password)
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.save()
            
            form_class.instance.authid = user
            form_class.instance.profilecompleted = 2
            name = form_class.cleaned_data['firstname'] + ' ' + form_class.cleaned_data['lastname']
            username = form_class.cleaned_data['emailaddress']
            message = ''' <span style="font-family:Trebuchet MS, Verdana, Arial; font-size:17px; font-weight:bold;">Hello ''' + name + '''!</span>
                            <br /> <p>Your account has been created with the below details:
                            <div style="padding-left:20px; padding-bottom:10px;">-&nbsp;&nbsp;&nbsp;Username - ''' + username + '''</div>
                            <div style="padding-left:20px; padding-bottom:10px;">-&nbsp;&nbsp;&nbsp;Password - ''' + password + '''</div>
                            <p>Kindly follow this link (''' + settings.SYSTEM_URL + ''' ) by clicking or pasting on your browser to access the system.</p>
                            <p>You are advised to change your password after logging in for the first time for security purpose. </p>'''
                        
            email = EmailMessage('Dumaworks - User Account Information', message, to=[form_class.cleaned_data['emailaddress']]) 
                        
            email.content_subtype = 'html'
            email.send()
            return super(UsersCreate, self).form_valid(form_class) 
        except Exception, e:
            #raise Http404("Error Creating Account. Please try again or contact the administrator" + str(e))
            return render_to_response('create.html', {'form':form_class, 'user': self.request.user, 'err': str(e)})
   

class UpdateUsers(UpdateView):
    template_name = 'update.html'
    model = Users
    form_class = UsersForm
    success_url = '/matcher/users'
    
class DeleteUsers(DeleteView):
    model = Users
    template_name = 'user_delete.html'  
    
    def get_success_url(self):
        return reverse_lazy('users_index')


# QualificationParams
class QualificationParamsView(ListView):
    template_name = 'qualificationparams.html'
    model = QualificationParameters

class QualificationParamsCreate(CreateView):
    template_name = 'create.html'
    model = QualificationParameters
    form_class = QualificationParametersForm
    
    success_url = '/matcher/qualificationparams'

class UpdateQualificationParams(UpdateView):
    template_name = 'update.html'
    model = QualificationParameters
    form_class = QualificationParametersForm
    success_url = '/matcher/qualificationparams'
    
class DeleteQualificationParams(DeleteView):
    model = QualificationParameters
    template_name = 'qualificationparams_delete.html'  
    
    def get_success_url(self):
        return reverse_lazy('qualificationparams_index')



# JobSeekers
class JobSeekersView(ListView):
    template_name = 'jobseekers.html'
    model = JobSeekers

class JobSeekersCreate(CreateView):
    template_name = 'create.html'
    model = JobSeekers
    form_class = JobSeekersForm
    success_url = '/matcher/profile'
    
    def get_initial(self):
        super(JobSeekersCreate, self).get_initial()
        user = getCurrentUser(self.request.user.pk)
        self.initial = {"firstname": user.firstname, "lastname": user.lastname, "mobilenumber": user.mobilenumber}

        return self.initial
    
    def get_form(self, form_class):
        form = super(JobSeekersCreate, self).get_form(form_class)
        form.fields['dateofbirth'].widget.attrs.update({'class': 'datepicker'})
        form.fields['skills'].widget.attrs.update({'class': 'chosen-select'})
        
        form.fields['skills'] = forms.ModelMultipleChoiceField(queryset=Skillset.objects.all(), widget=FilteredSelectMultiple("", is_stacked=False))
        return form
    def form_valid(self, form_class):
        user = utils.getCurrentUser(self.request.user.pk)
        user.profilecompleted = 1
        user.save()
        form_class.instance.userid = user
        return super(JobSeekersCreate, self).form_valid(form_class) 


class UpdateJobSeekers(UpdateView):
    template_name = 'update.html'
    model = JobSeekers
    form_class = JobSeekersForm
    success_url = '/matcher/profile'
    
    def get_form(self, form_class):
        form = super(UpdateJobSeekers, self).get_form(form_class)
        form.fields['dateofbirth'].widget.attrs.update({'class': 'datepicker'})
        form.fields['skills'].widget.attrs.update({'class': 'chosen-select'})
        
        form.fields['skills'] = forms.ModelMultipleChoiceField(queryset=Skillset.objects.all(), widget=FilteredSelectMultiple("", is_stacked=False))
        return form

    
class DeleteJobSeekers(DeleteView):
    model = JobSeekers
    template_name = 'jobseekers_delete.html'  
    
    def get_success_url(self):
        return reverse_lazy('jobseekers_index')

class DeactivateJobSeekers(View):
    model = JobSeekers
    template_name = 'jobseekers_deactivate.html'  
    success_url = '/matcher/home'
    
    def get(self, request, pk, *args, **kwargs):
        seekerprofile = JobSeekers.objects.all().get(jobseekerid=pk)
        return TemplateResponse(request, self.template_name,{'jobseekers': seekerprofile})
    
    def post(self, request, pk, *args, **kwargs):
        seekerprofile = JobSeekers.objects.all().get(jobseekerid=pk)
        seekerprofile.status = 2
        seekerprofile.save()
        
        #deactivate the user attached to the jobseeker profile
        matcher_user = Users.objects.all().get(userid=seekerprofile.userid.userid)
        #matcher_user.authid.is_active = 0
        User.objects.filter(pk=matcher_user.authid.id).update(is_active=0)
        #return HttpResponse(pk)
        return HttpResponseRedirect('/matcher/jobseekers')
        #return TemplateResponse(request, self.template_nam,{}
   

class ActivateJobSeekers(View):
    model = JobSeekers
    template_name = 'jobseekers_activate.html'  
    success_url = '/matcher/home'
    
    def get(self, request, pk, *args, **kwargs):
        seekerprofile = JobSeekers.objects.all().get(jobseekerid=pk)
        return TemplateResponse(request, self.template_name,{'jobseekers': seekerprofile})
    
    def post(self, request, pk, *args, **kwargs):
        seekerprofile = JobSeekers.objects.all().get(jobseekerid=pk)
        seekerprofile.status = 1
        seekerprofile.save()
        
        #deactivate the user attached to the jobseeker profile
        matcher_user = Users.objects.all().get(userid=seekerprofile.userid.userid)
        #matcher_user.authid.is_active = 0
        User.objects.filter(pk=matcher_user.authid.id).update(is_active=1)
        #return HttpResponse(pk)
        return HttpResponseRedirect('/matcher/jobseekers')
        #return TemplateResponse(request, self.template_nam,{}
  

# Education
class EducationView(ListView):
    template_name = 'education.html'
    model = Education

class EducationCreate(CreateView):
    template_name = 'create.html'
    model = Education
    form_class = EducationForm
    success_url = '/matcher/education'
    
class UpdateEducation(UpdateView):
    template_name = 'update.html'
    model = Education
    form_class = EducationForm
    success_url = '/matcher/education'
    
class DeleteEducation(DeleteView):
    model = Education
    template_name = 'education_delete.html'  
    
    def get_success_url(self):
        return reverse_lazy('education_index')
    

# Skills
class SkillsView(ListView):
    template_name = 'skills.html'
    model = Skillset

class SkillsCreate(CreateView):
    template_name = 'create.html'
    model = Skillset
    form_class = SkillsetForm
    success_url = '/matcher/skills'
    
class UpdateSkills(UpdateView):
    template_name = 'update.html'
    model = Skillset
    form_class = SkillsetForm
    success_url = '/matcher/skills'
    
class DeleteSkills(DeleteView):
    model = Skillset
    template_name = 'skills_delete.html'  
    
    def get_success_url(self):
        return reverse_lazy('skills_index')
    

# Experience
class ExperienceView(ListView):
    template_name = 'experience.html'
    model = ExperienceLevel

class ExperienceCreate(CreateView):
    template_name = 'create.html'
    model = ExperienceLevel
    form_class = ExperienceLevelForm
    success_url = '/matcher/experience'
    
class UpdateExperience(UpdateView):
    template_name = 'update.html'
    model = ExperienceLevel
    form_class = ExperienceLevelForm
    success_url = '/matcher/experience'
    
class DeleteExperience(DeleteView):
    model = ExperienceLevel
    template_name = 'experience_delete.html'  
    
    def get_success_url(self):
        return reverse_lazy('experience_index')



# Jobs
class JobsView(ListView):
    template_name = 'jobslist.html'
       
    def get(self, request, *args, **kwargs):
        model = Jobs.objects.all()
        try:
            matcherUser = Users.objects.all().get(authid=request.user.pk)
        except:
            matcherUser = None
        if (matcherUser):
            if(matcherUser.usertype==2):#if employer only list the companies job
                try:
                    model = Jobs.objects.all().filter(companyid=matcherUser.companyid)
                except:
                    model = None
        
        return TemplateResponse(request, self.template_name,{'matchUser': matcherUser, 'object_list': model})
  
    
    
    
    
def home(request):
        if(request.user.is_authenticated()):
            try:
                matcherUser = Users.objects.all().get(authid=request.user.pk)
            except:
                matcherUser = None
            if(matcherUser):
            # if the user is a jobseeker and hasnt completed profile, display page to complete profile
                if(matcherUser.usertype == 1):
                # check if the jobseeker profile already exists
                    try:
                        seekerprofile = JobSeekers.objects.all().get(userid=matcherUser.userid)
                    except:
                        seekerprofile = None
                
                        return render_to_response('jobseeker/profile.html', {'user': request.user, 'matchUser': matcherUser, 'seekerprofile': seekerprofile})
                if (matcherUser.usertype == 2):
                    return render_to_response('employer/profile.html', {'user': request.user, 'matchUser': matcherUser})

            # if the user is an employer and hasnt completed profile, display page to create company profile
        else:
            matcherUser = None
            
        return render_to_response('home.html', {'user': request.user, 'matchUser': matcherUser})

@login_required
def myProfile(request):
    matcherUser = Users.objects.all().get(authid=request.user.pk)
    #if the user is a jobseeker and hasnt completed profile, display page to complete profile
    if(matcherUser.usertype == 1):
        # check if the jobseeker profile already exists
        try:
            seekerprofile = JobSeekers.objects.all().get(userid=matcherUser.userid)
        except:
            seekerprofile = None
        return render_to_response('jobseeker/profile.html', {'user': request.user, 'matchUser': matcherUser, 'seekerprofile': seekerprofile})
    if (matcherUser.usertype == 2):
        return render_to_response('employer/profile.html', {'user': request.user, 'matchUser': matcherUser})
    #if the user is an employer and hasnt completed profile, display page to create company profile
    return render_to_response('home.html', {'user': request.user, 'matchUser': matcherUser})

def register(request):
    err = ''
    try:
        if(request.method == "POST"):
            form = UsersForm(request.POST)
            if(form.is_valid()):
                s = string.lowercase + string.digits
                password = ''.join(random.sample(s, 10))
                user = User.objects.create_user(form.cleaned_data['emailaddress'], form.cleaned_data['emailaddress'], password)
                user.first_name = form.cleaned_data['firstname']
                user.last_name = form.cleaned_data['lastname']
                user.save()
                user_instance = form.save(commit=False)
                user_instance.status = 1
                user_instance.authid = user
                user_instance.lastloginip = request.META['REMOTE_ADDR']
                user_instance.lastlogindate = timezone.now()
                user_instance.profilecompleted = 2
                user_instance.save()
                
                user_instance.lastlogindate = timezone.now()
                name = form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
                username = form.cleaned_data['emailaddress']
                message = ''' <span style="font-family:Trebuchet MS, Verdana, Arial; font-size:17px; font-weight:bold;">Hello ''' + name + '''!</span>
                        <br /> <p>Your account has been created with the below details:
                        <div style="padding-left:20px; padding-bottom:10px;">-&nbsp;&nbsp;&nbsp;Username - ''' + username + '''</div>
                        <div style="padding-left:20px; padding-bottom:10px;">-&nbsp;&nbsp;&nbsp;Password - ''' + password + '''</div>
                        <p>Kindly follow this link (''' + settings.SYSTEM_URL + ''' ) by clicking or pasting on your browser to access the system.</p>
                        <p>You are advised to change your password after logging in for the first time for security purpose. </p>'''
                        
                email = EmailMessage('Dumaworks - User Account Information', message, to=[form.cleaned_data['emailaddress']]) 
                    
                email.content_subtype = 'html'
                email.send()
                    
                return redirect('/matcher/register/success')    
        else:
            form = UsersForm 
    except Exception, e:
        #raise Http404("Error Creating Account. Please try again or contact the administrator" + str(e))
        return render_to_response('register.html', {'form':form, 'err': str(e)}, context_instance=RequestContext(request))
    
    return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

def registersuccess(request):
   
    d = {}

    return render_to_response('registersuccess.html', d)

@login_required
@is_employee_nocompany
def createcompany(request):
    context = RequestContext(request)

    if request.method == "POST":
        form = CompaniesForm(request.POST)
        if(form.is_valid()):
            c = Companies()
            c.companyname = form.cleaned_data['companyname']
            c.emailaddress = form.cleaned_data['emailaddress']
            c.telephone = form.cleaned_data['telephone']
            c.physicaladdress = form.cleaned_data['physicaladdress']
            c.industryid = form.cleaned_data['industryid']
            c.save()

            #Add Company to user
            muser = Users.objects.all().get(authid=request.user.pk)
            muser.companyid = c
            muser.profilecompleted = 1
            muser.save()

            return redirect('/matcher/home')
    else:
        form = CompaniesForm

    return render_to_response('company_create.html', {'form':form},
            context_instance=context)


class UpdateCompany(LoginRequiredMixin,UpdateView):
    template_name = 'company_create.html'
    model = Companies
    form_class = CompaniesForm
    success_url = '/matcher/home'


def jobSeekersAdminView(request, pk):
                try:
                    seekerprofile = JobSeekers.objects.all().get(jobseekerid=pk)
                except:
                    seekerprofile = None
                
                return render_to_response('jobseeker/adminview.html', {'user': request.user, 'seekerprofile': seekerprofile})


def jobDetails(request, pk):
                try:
                    job = Jobs.objects.all().get(jobid=pk)
                except:
                    job = None
                
                return render_to_response('jobs/adminview.html', {'user': request.user, 'job': job})


@login_required
def createjob(request):
    context = RequestContext(request)
    user = getCurrentUser(request.user.pk)
    if request.method == "POST":
        form = JobsForm(request.POST)
        if(form.is_valid()):
            j = Jobs()
            j.title = form.cleaned_data['title']
            j.shortdescription = form.cleaned_data['shortdescription']
            j.detaileddescription = form.cleaned_data['detaileddescription']
            j.companyid = user.companyid
            j.yearsofexperience = form.cleaned_data['yearsofexperience']
            j.educationid = form.cleaned_data['educationid']
            j.skills = form.cleaned_data['skills']
            j.openingsavailable = form.cleaned_data['openingsavailable']
            j.deadline = form.cleaned_data['deadline']
            j.createdBy = user
            j.save()

            return redirect('/matcher/jobs')
    else:
        form = JobsForm

    return render_to_response('create_job.html', {'form':form},
            context_instance=context)
