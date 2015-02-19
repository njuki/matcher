# -*- coding: utf-8 -*-
from django import forms
from models import *
from django.contrib.admin.widgets import FilteredSelectMultiple


class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Companies
        exclude = ('status',)


class IndustriesForm(forms.ModelForm):
    class Meta:
        model = Industries
        fields = ['industryname','description']


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['firstname','lastname', 'emailaddress', 'mobilenumber','usertype']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['emailaddress','password']


class JobTypesForm(forms.ModelForm):
    class Meta:
        model = JobTypes
        fields = ['typename','description']


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        exclude = ['companyid', 'createdBy']


    def __init__(self, *args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs.update({'class': 'datepicker'})
        self.fields['skills'].widget.attrs.update({'class': 'chosen-select'})
        self.fields['skills'] = forms.ModelMultipleChoiceField(queryset=Skillset.objects.all(), widget=FilteredSelectMultiple("", is_stacked=False))

class QualificationParametersForm(forms.ModelForm):
    class Meta:
        model = QualificationParameters
        fields = ['name', 'inputtype', 'units', 'description']


class JobQualificationParametersForm(forms.ModelForm):
    class Meta:
        model = JobQualificationParameters


class JobSeekersForm(forms.ModelForm):
    class Meta:
        model = JobSeekers
        
        fields = ['firstname', 'lastname', 'mobilenumber', 'gender', 'dateofbirth','skills',
                   'cv','maritalstatus', 'expectedsalary', 'yearsofexperience', 'educationid',
                   'experienceid', 'profiledescription']
        
        #skills = forms.ModelMultipleChoiceField(queryset=Skillset.objects.all(), widget=FilteredSelectMultiple("Skillset", is_stacked=False))
        #fields.insert(-1, skills)
        def __init__(self, *args, **kwargs):
            super(JobSeekersForm, self).__init__(*args, **kwargs)
            self.fields['skills'] =  ModelChoiceField(queryset=Skillset.objects.all(), empty_label="Choose a skill")


class SeekersQualificationParametersForm(forms.ModelForm):
    class Meta:
        model = SeekersQualificationParameters


class ChannelsForm(forms.ModelForm):
    class Meta:
        model = Channels


class OutMessagesForm(forms.ModelForm):
    class Meta:
        model = OutMessages


class JobApplicantMatchesForm(forms.ModelForm):
    class Meta:
        model = JobApplicantMatches


class InboxForm(forms.ModelForm):
    class Meta:
        model = Inbox

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education


class ExperienceLevelForm(forms.ModelForm):
    class Meta:
        model = ExperienceLevel


class SkillsetForm(forms.ModelForm):
    class Meta:
        model = Skillset

