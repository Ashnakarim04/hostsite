from django.contrib import admin
from . models import Jobs, CompanyProfile, LikedContent, Students,AdminStudent,StudentProfile,CompanyApprove,JobApplication,internship,videolibrary,ccontent
from . models import Alumni, resume1, LikedContent1, ResumeBuilder, BlogContent, Review, Event, ExcelData, AddAptitude, AptitudeTest,Question


# Register your models here.
# from . import models
# # Register your models here.

admin.site.register(Jobs)
admin.site.register(CompanyProfile)
admin.site.register(Students)
admin.site.register(AdminStudent)
admin.site.register(StudentProfile)
admin.site.register(CompanyApprove)
admin.site.register(JobApplication)
admin.site.register(internship)
admin.site.register(videolibrary)
admin.site.register(ccontent)
admin.site.register(LikedContent)
admin.site.register(Alumni)
admin.site.register(resume1)
admin.site.register(LikedContent1)
admin.site.register(ResumeBuilder)
admin.site.register(BlogContent)
admin.site.register(Review)
admin.site.register(Event)
admin.site.register(ExcelData)
admin.site.register(AddAptitude)
admin.site.register(AptitudeTest)
admin.site.register(Question)
# admin.site.register(CustomUser)