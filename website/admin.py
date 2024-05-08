from django.contrib import admin
from . models import Jobs, CompanyProfile, LikedContent, Students,AdminStudent,StudentProfile,CompanyApprove,JobApplication,internship,videolibrary,ccontent
from . models import Alumni, resumeadmin, LikedContent1, ResumeBuilder, BlogContent, Review, AlumniEvent, ExcelData, AddAptitude, AptitudeTest,Question, Option, ExamSchedule
from . models import Question2, Option2, Quiz3, Question3, Option3, CompanyEvent, Questionn

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
admin.site.register(resumeadmin)
admin.site.register(LikedContent1)
admin.site.register(ResumeBuilder)
admin.site.register(BlogContent)
admin.site.register(Review)
admin.site.register(AlumniEvent)
admin.site.register(ExcelData)
admin.site.register(AddAptitude)
admin.site.register(AptitudeTest)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(ExamSchedule)
admin.site.register(Question2)
admin.site.register(Option2)
admin.site.register(Quiz3)
admin.site.register(Question3)
admin.site.register(Option3)
admin.site.register(CompanyEvent)
admin.site.register(Questionn)
# admin.site.register(CustomUser)