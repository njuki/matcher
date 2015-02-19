from django.db import models
from django.contrib.auth.models import User

class Industries(models.Model):
    industryid = models.AutoField(primary_key=True, verbose_name="Industry", db_index=True)
    industryname = models.CharField(unique=True, max_length=255, verbose_name="Industry Name")
    description = models.TextField()
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)
    
class Companies(models.Model):  
    companyid = models.AutoField(primary_key=True, unique=True, db_index=True)
    companyname = models.TextField(verbose_name="Company Name")
    emailaddress = models.EmailField(max_length=150, verbose_name="Company Email")
    telephone = models.CharField(max_length=15, verbose_name="Telephone")
    physicaladdress = models.TextField(verbose_name="Physical Address")
    industryid = models.ForeignKey('Industries', verbose_name="Industry")
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)
    

class Users(models.Model):
    USER_TYPES_CHOICES = (
                          (1, 'Job Seeker'),
                          (2, 'Employer')
                          )
#     if(user.is_staff):
#         USER_TYPES_CHOICES.append((3, 'Staff'))
        
    userid = models.AutoField(primary_key=True, verbose_name="user", db_index=True)
    authid = models.ForeignKey(User, blank=True, null=True)
    companyid = models.ForeignKey(Companies, blank=True, null=True)
    firstname = models.CharField(max_length=255, verbose_name="First Name")
    lastname = models.CharField(max_length=255, verbose_name="Last Name")
    username = models.CharField(max_length=255, verbose_name="User Name", null=True)
    password = models.CharField(max_length=255, verbose_name="Password")
    emailaddress = models.EmailField(max_length=150, verbose_name="Email Address")
    status = models.IntegerField(default=1)
    profilecompleted = models.IntegerField(default=2)
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now=True, auto_now_add=True)
    lastloginip = models.IPAddressField(null=True)
    lastlogindate = models.DateTimeField(null=True)
    mobilenumber = models.CharField(max_length=15, verbose_name="Mobile Number")
    usertype = models.PositiveIntegerField(choices=USER_TYPES_CHOICES, verbose_name="Please select type of account")
    



class JobTypes(models.Model):
    STATUS_CHOICES = (
                          (1, 'Active'),
                          (2, 'Inactive')
                          )
    
    typename = models.CharField(unique=True, max_length=255, verbose_name='Job Type')
    description = models.TextField()
    jobtypeid = models.AutoField(primary_key=True)
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now=True, auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    



class Jobs(models.Model):
    """
    The various vacancies as posted by companies
    """
    
    title = models.CharField(max_length=255)
    shortdescription = models.CharField(max_length=255)
    detaileddescription = models.TextField()
    jobid = models.AutoField(primary_key=True)
    companyid = models.ForeignKey('Companies')
    createdBy = models.ForeignKey('Users')
    deadline = models.DateField()
    openingsavailable = models.IntegerField()
    yearsofexperience = models.FloatField()
    skills =  skills =  models.TextField(verbose_name="Skill set")
    educationid = models.ForeignKey('Education')    
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now=True, auto_now_add=True)
    



class QualificationParameters(models.Model):
    INPUT_TYPES_CHOICES = (
                          (1, 'Number'),
                          (2, 'Text'),
                          (3, 'Date') 
                          )

    name = models.CharField(unique=True, max_length=255)
    units = models.CharField(max_length=255)
    description = models.TextField(verbose_name="Description")
    parameterid = models.AutoField(primary_key=True)
    inputtype = models.IntegerField(choices = INPUT_TYPES_CHOICES, verbose_name="Input Type")
    



class JobQualificationParameters(models.Model): 
    jobid = models.ForeignKey('Jobs')
    qualificationparamid = models.ForeignKey('QualificationParameters')
    jobqualificationparameterid = models.AutoField(primary_key=True)
    

class Education(models.Model):
    educationid = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Education Level Name", max_length=255, unique=True)
    description = models.TextField(verbose_name="Brief Description")
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __str__(self):
        return self.name
   
    
    
class ExperienceLevel(models.Model):
    experienceid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __str__(self):
        return self.name
   
class Skillset(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    skillid = models.AutoField(primary_key=True)
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __str__(self):
        return self.name


  
class JobSeekers(models.Model):
    GENDER_CHOICES = (
                          ("M", 'Male'),
                          ("F", 'Female'),
                          )
    
    MARITAL_STATUS = (
                          (1, 'Single'),
                          (2, 'Engaged'),
                          (3, 'Married'),
                          )
    
    SKILLS_CHOICES = tuple((y.pk,y.name) for y in Skillset.objects.all())
    
    STATUS_CHOICES = (
                          (1, 'Active'),
                          (2, 'Inactive')
                          )
    
    
    firstname = models.CharField(max_length=255, verbose_name="First Name")
    lastname = models.CharField(max_length=255, verbose_name="Last Name")
    gender = models.CharField(choices = GENDER_CHOICES, max_length=1)
    cv = models.FileField(verbose_name = "Upload CV", upload_to='uploads/cvs')
    jobseekerid = models.AutoField(primary_key=True)
    experienceid = models.ForeignKey(ExperienceLevel, verbose_name="Experience")
    educationid = models.ForeignKey(Education, verbose_name="Education Level")
    skills =  models.TextField(verbose_name="Skill set")
    userid = models.ForeignKey(Users, unique=True)
    dateofbirth = models.DateField(verbose_name="Date of Birth")
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now=True, auto_now_add=True)
    yearsofexperience = models.FloatField(verbose_name="Years of Industrial Experience")
    mobilenumber = models.CharField(max_length=15, verbose_name="Mobile Number")
    maritalstatus = models.SmallIntegerField(choices = MARITAL_STATUS, verbose_name="Marital Status")
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)
    expectedsalary = models.FloatField(verbose_name="Expected Salary")
    profiledescription = models.TextField(verbose_name="Summary About Self")
    
    



class SeekersQualificationParameters(models.Model):
    jobqualificationparamid = models.ForeignKey('JobQualificationParameters')
    jobseekerid = models.ForeignKey('JobSeekers')
    parametervalue = models.CharField(max_length=255)
    qualificationparamid = models.AutoField(primary_key=True)
    



class Channels(models.Model):
    STATUS_CHOICES = (
                          (1, 'Active'),
                          (2, 'Inactive')
                          )
    name = models.CharField(unique=True, max_length=255, verbose_name='Channel Name')
    description = models.TextField()
    channelid = models.AutoField(primary_key=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)
    



class OutMessages(models.Model): 
    jobid = models.ForeignKey('Jobs')
    channelid = models.ForeignKey('Channels')
    jobseekerid = models.ForeignKey('JobSeekers')
    jobapplicantmatchid = models.ForeignKey('JobApplicantMatches')
    uniqueid = models.CharField(max_length=255)
    message = models.TextField()
    outmessageid = models.AutoField(primary_key=True)
    datecreated = models.DateTimeField()
    datemodified = models.DateTimeField()
    



class JobApplicantMatches(models.Model):
    jobid = models.ForeignKey('Jobs')
    generatedbyuserid = models.ForeignKey('Users')
    jobseekerid = models.ForeignKey('JobSeekers')
    jobapplicantmatchid = models.AutoField(primary_key=True)
    datecreated = models.DateTimeField(auto_now=True)
    datemodified = models.DateTimeField(auto_now=True, auto_now_add=True)
    



class Inbox(models.Model):
    source = models.CharField(max_length=255)
    uniqueid = models.CharField(max_length=255)
    message = models.TextField()
    inboxid = models.AutoField(primary_key=True)
    datecreated = models.DateTimeField()
 



