# app specific urls
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from matcher import views


urlpatterns = patterns('',
    url(r'^home', 'matcher.views.home', name='home'),
     url(r'^profile', 'matcher.views.myProfile', name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success', views.registersuccess),
    #authentication
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^newUserPassword/$', 'django.contrib.auth.views.password_change'),
    
    
    #industries CRUD
    url(r'^industries$', views.IndustriesView.as_view(), name='industries_index'), #listView
    url(r'^industries/create$', views.IndustryCreate.as_view(), name='industry_create'),
    url(r'^industries/edit/(?P<pk>\d+)$', views.UpdateIndustry.as_view(), name='industry_edit'),
    url(r'^industries/delete/(?P<pk>\d+)$', views.DeleteIndustry.as_view(), name='industry_delete'),
    
    #Job Types CRUD
    url(r'^jobTypes$', views.JobTypesView.as_view(), name='jobtypes_index'), #listView
    url(r'^jobTypes/create$', views.JobTypesCreate.as_view(), name='jobtypes_create'),
    url(r'^jobTypes/edit/(?P<pk>\d+)$', views.UpdateJobTypes.as_view(), name='jobtypes_edit'),
    url(r'^jobTypes/delete/(?P<pk>\d+)$', views.DeleteJobTypes.as_view(), name='jobtypes_delete'),
    
    #Channels CRUD
    url(r'^channels$', views.ChannelsView.as_view(), name='channels_index'), #listView
    url(r'^channels/create$', views.ChannelsCreate.as_view(), name='channels_create'),
    url(r'^channels/edit/(?P<pk>\d+)$', views.UpdateChannels.as_view(), name='channels_edit'),
    url(r'^channels/delete/(?P<pk>\d+)$', views.DeleteChannels.as_view(), name='channels_delete'),
    
    
    #Users CRUD
    url(r'^users$', views.UsersView.as_view(), name='users_index'), #listView
    url(r'^users/create$', views.UsersCreate.as_view(), name='users_create'),
    url(r'^users/edit/(?P<pk>\d+)$', views.UpdateUsers.as_view(), name='users_edit'),
    url(r'^users/delete/(?P<pk>\d+)$', views.DeleteUsers.as_view(), name='users_delete'),
    
     #qualificationparams CRUD
    url(r'^qualificationparams$', views.QualificationParamsView.as_view(), name='qualificationparams_index'), #listView
    url(r'^qualificationparams/create$', views.QualificationParamsCreate.as_view(), name='qualificationparams_create'),
    url(r'^qualificationparams/edit/(?P<pk>\d+)$', views.UpdateQualificationParams.as_view(), name='qualificationparams_edit'),
    url(r'^qualificationparams/delete/(?P<pk>\d+)$', views.DeleteQualificationParams.as_view(), name='qualificationparams_delete'),
    
    #Education CRUD
    url(r'^education$', views.EducationView.as_view(), name='education_index'), #listView
    url(r'^education/create$', views.EducationCreate.as_view(), name='education_create'),
    url(r'^education/edit/(?P<pk>\d+)$', views.UpdateEducation.as_view(), name='education_edit'),
    url(r'^education/delete/(?P<pk>\d+)$', views.DeleteEducation.as_view(), name='education_delete'),
    
    #Skills CRUD
    url(r'^skills$', views.SkillsView.as_view(), name='skills_index'), #listView
    url(r'^skills/create$', views.SkillsCreate.as_view(), name='skills_create'),
    url(r'^skills/edit/(?P<pk>\d+)$', views.UpdateSkills.as_view(), name='skills_edit'),
    url(r'^skills/delete/(?P<pk>\d+)$', views.DeleteSkills.as_view(), name='skills_delete'),
    
    #Experience CRUD
    url(r'^experience$', views.ExperienceView.as_view(), name='experience_index'), #listView
    url(r'^experience/create$', views.ExperienceCreate.as_view(), name='experience_create'),
    url(r'^experience/edit/(?P<pk>\d+)$', views.UpdateExperience.as_view(), name='experience_edit'),
    url(r'^experience/delete/(?P<pk>\d+)$', views.DeleteExperience.as_view(), name='experience_delete'),
    

    #jobseekers CRUD
    url(r'^jobseekers$', views.JobSeekersView.as_view(), name='jobseekers_index'), #listView
    url(r'^jobseekers/create$', views.JobSeekersCreate.as_view(), name='jobseekers_create'),
    url(r'^jobseekers/edit/(?P<pk>\d+)$', views.UpdateJobSeekers.as_view(), name='jobseekers_edit'),
    url(r'^jobseekers/delete/(?P<pk>\d+)$', views.DeleteJobSeekers.as_view(), name='jobseekers_delete'),
    
    #jobseeker Admin manage
    url(r'^jobseekers/view/(?P<pk>\d+)$', views.jobSeekersAdminView, name='seeker_view'),
    url(r'^jobseekers/deactivate/(?P<pk>\d+)$', views.DeactivateJobSeekers.as_view(), name='seeker_deactivate'),
    url(r'^jobseekers/activate/(?P<pk>\d+)$', views.ActivateJobSeekers.as_view(), name='seeker_activate'),
    
     #jobs manage
    url(r'^joblist$', views.JobsView.as_view(), name='jobslist_view'),
)
