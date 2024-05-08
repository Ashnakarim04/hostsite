"""
URL configuration for zillionhire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from website.views import loginn,reg, index, loggout,sample2, jobs, studentloginn, cindex, sindex, aboutuser, contactuser, cprofile, cjob, postjob, addjob,edit_job, admin_login, admin_index2,admin_profile,admin_editprofile,admin_company,addstudents,jobslist, admin_poststudent,companyprofilelist, search_company, search_student,edit_student, ad_cprofile, download_criteria, search_course, ad_deletecompany, search_job,adsearch_company, videoform, videolibraryadd, videolist, content2form, content2list, content2,searchcontent, searchvideo, scontent2list, payconfirm, likedcontent2
from website.views import toggle_like, adcontent2, editcontent2, dlt_content2, alumnilist, toggle_alumni_status
from website.views import *
from website import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from website.views import StudentDataAPIView

 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    # path('', sample, name=''),
    path('',views.index, name="index"),
    path('jobs',views.jobs, name="jobs"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('shome',views.shome, name="shome"),
    # path('blog',views.blog, name="blog"),
    path('sample2', sample2, name='sample2'),
    path('studentloginn', studentloginn, name='studentloginn'),
    path('loginn', loginn, name='loginn'),
    path('reg', reg, name='reg'), 
    path('loggout', loggout, name='loggout'),
    path('cindex', cindex, name='cindex'),
    path('aboutuser', aboutuser, name='aboutuser'),
    path('contactuser', contactuser, name='contactuser'),
    path('cprofile/<int:companyprofile_id>/', cprofile, name='cprofile'),
    path('cprofile/<int:user_id>/', views.approve_comp, name='approve_comp'),
    path('approve_comp/<int:company_id>/', views.approve_comp, name='approve_comp'),
    # path('postjob/<int:companyprofile_id>/', postjob, name='postjob'),
    path('cjob', cjob, name='cjob'),
    path('postjob/', views.postjob, name='postjob'),
    path('addjob', addjob, name='addjob'),
    # path('addjob/<int:obj_id>/', views.addjob, name='addjob'),
    path('sindex', sindex, name='sindex'),
    path('sabout',views.sabout, name="sabout"),
    path('scontact',views.scontact, name="scontact"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("",include("allauth.urls")),
    path('edit/job/<int:job_id>/', views.edit_job, name='edit_job'), 
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),  
    path('admin_login', admin_login, name='admin_login'),
    # path('admin_index', admin_index, name='admin_index'),
    path('admin_index2', admin_index2, name='admin_index2'),
    path('admin_profile', admin_profile, name='admin_profile'),
    path('ad_cprofile', ad_cprofile, name='ad_cprofile'),
    
    # path('admin_students', admin_students, name='admin_students'),
    path('admin_company', admin_company, name='admin_company'),
    path('admin_edit-profile', admin_editprofile, name='admin_editprofile'),
    path('addstudents', addstudents, name='addstudents'),
    path('jobslist',jobslist, name='jobslist'),
    # path('addelete_job',views.addelete_job, name='addelete_job'),
    # path('admin_studentadd',admin_studentadd,name='admin_studentadd'),
    path('admin_poststudent/', views.admin_poststudent, name='admin_poststudent'),
    path('companyprofilelist',companyprofilelist,name='companyprofilelist'),
    path('search_company', search_company, name='search_company'),
    path('search_job', search_job, name='search_job'),
    # path('search_jobs/', views.search_jobs, name='search_jobs'),
    path('adsearch_company', adsearch_company, name='adsearch_company'),
    path('delete_company', views.delete_company, name='delete_company'),
    path('ad_deletecompany/<int:comp_id>/', views.ad_deletecompany, name='ad_deletecompany'),

    path('search_student', search_student, name='search_student'),
    path('search_student2', views.search_student2, name='search_student2'),
    # path('edit_student',edit_student,name='edit_student'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('ad_studentlist', views.ad_studentlist, name='ad_studentlist'),
    # path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('download_criteria/<int:job_id>/', download_criteria.as_view(), name='download_criteria'),
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
     
    path('companyapprove',views.companyapprove, name='companyapprove'),
    path('search_course',search_course, name='search_course'),
    path('profc',views.profc, name='profc'),
    path('search_course',search_course, name='search_course'),
    path('stureg',views.stureg, name='stureg'),
    path('students/', views.student_list, name='student_list'),
    # path('api/get_student_data/', StudentDataAPIView.as_view(), name='get_student_data'),
    # path('asha_approved_appo', views.asha_approved_appointments, name='asha_approved_appo'),
    # path('approve-appointment/<int:appointment_id>/', views.approve_appointment, name='approve_appointment'),
    path('add_student/', views.add_student, name='add_student'),
    path('admin_addstudents/', views.admin_addstudents, name='admin_addstudents'),
    # path('sdashboard/', views.sdashboard, name='sdashboard'),
    path('sprofile/<int:studentprofile_id>/', views.sprofile, name='sprofile'),
    path('jobapply/<int:jobapply_id>/', views.jobapply, name='jobapply'),

    # path('sprofile/', views.sprofile, name='sprofile'),
    # path('sprofile/<int:studentprofile_id>/', views.sprofile, name='sprofile'),
    path('cindex/', views.cindex, name='cindex'),
    path('srequest/', views.srequest, name='srequest'),
    path('adpostjob/', views.adpostjob, name='adpostjob'),
    path('job_approve/<int:studentprofile_id>/', views.job_approve, name='job_approve'),


    path('approved_jobs/<int:job_id>/', views.approved_jobs, name='approved_jobs'),
    path('eligibility', views.eligibility, name='eligibility'),

    path('appliedstudents', views.appliedstudents, name='appliedstudents'),
    path('adminappstudents', views.adminappstudents, name='adminappstudents'),
    path('sappliedjobs/<int:studentprofile_id>/', views.sappliedjobs, name='sappliedjobs'),
    path('s_shortlist/<int:studentprofile_id>/', views.s_shortlist, name='s_shortlist'),
    path('cfirstround', views.cfirstround, name='cfirstround'),
    path('admin_shortlist', views.admin_shortlist, name='admin_shortlist'),
    path('studentprofileapp/<int:studentprofile_id>/', views.studentprofileapp, name='studentprofileapp'), 



    


    path('reject_shortlist/<int:application_id>/', views.reject_shortlist, name='reject_shortlist'),
    path('approve_shortlist/<int:application_id>/', views.approve_shortlist, name='approve_shortlist'),
    path('admincontent',views.admincontent, name="admincontent"),
    path('contentform',views.contentform, name="contentform"),
    # path('contentview/<int:id>', views.contentview, name='contentview/<int:id>'),
    path('interinfo', views.interinfo, name='interinfo'),
    path('classdetail', views.classdetail, name='classdetail'),
    path('intern1/', views.intern1, name='intern1'),
    path('toggle_alumni/<int:student_profile_id>/', views.toggle_alumni_status, name='toggle_alumni_status'),
    path('contentlist', views.contentlist, name='contentlist'),
    path('videoform',views.videoform, name="videoform"),
    path('videolibraryadd',views.videolibraryadd, name="videolibraryadd"),
    path('videolist', views.videolist, name='videolist'),
    path('content2/', views.content2, name='content2'),
    path('content2form',views.content2form, name="content2form"),
    path('content2list', views.content2list, name='content2list'),
    path('searchcontent', views.searchcontent, name='searchcontent'),
    path('searchvideo', views.searchvideo, name='searchvideo'),
    
    path('scontent2list/<int:studentprofile_id>/<int:content_id>/', views.scontent2list, name='scontent2list'),
    path('scontent2list/<int:studentprofile_id>/', views.scontent2list, name='scontent2list'),
    path('scontent2list/<int:content_id>/', views.scontent2list, name='scontent2list'),

    path('payconfirm/<int:content_id>/', views.payconfirm, name='payconfirm'),
    path('payconfirm/<int:studentprofile_id>/<int:content_id>/', views.payconfirm, name='payconfirm'),

    path('scontent2list/<int:studentprofile_id>/<int:content_id>/', views.scontent2list, name='scontent2list'),
    path('scontent2list/<int:studentprofile_id>/', views.scontent2list, name='scontent2list_student'),
    path('scontent2list/<int:content_id>/', views.scontent2list, name='scontent2list_content'),

    path('search_content2/<int:studentprofile_id>/', search_content2, name='search_content2'),
    path('search_content1/<int:studentprofile_id>/', search_content1, name='search_content1'),
    path('s_searchvideo/<int:studentprofile_id>/', views.s_searchvideo, name='s_searchvideo'),
    path('s_searchvideo_ajax/<int:studentprofile_id>/', views.s_searchvideo_ajax, name='s_searchvideo_ajax'),

    path('payconfirm/<int:content_id>/', views.payconfirm, name='payconfirm'),
    path('payconfirm/<int:studentprofile_id>/<int:content_id>/', views.payconfirm, name='payconfirm'),
    path('likedcontent2/<int:studentprofile_id>/', views.likedcontent2, name='likedcontent2'),

    path('content/details/', views.content_details, name='content_details'),

    path('save_liked_content/', views.save_liked_content, name='save_liked_content'),
    path('toggle_like/', views.toggle_like, name='toggle_like'),
    path('save_liked_content1/', views.save_liked_content1, name='save_liked_content1'),
    path('toggle_like1/', views.toggle_like1, name='toggle_like1'),
    path('adcontent2/', views.adcontent2, name='adcontent2'),
    path('editcontent2/<int:content_id>/', views.editcontent2, name='editcontent2'),
    path('dlt_content2/', views.dlt_content2, name='dlt_content2'),
    path('alumnilist/', views.alumnilist, name='alumnilist'),
    path('toggle_alumni_status/<int:student_profile_id>/', toggle_alumni_status, name='toggle_alumni_status'),

    path('resume1/', views.resume1, name='resume1'),
    path('gen_resume/', gen_resume, name='gen_resume'),
    path('home', home, name = 'home'), 

    path('resumeform',views.resumeform, name="resumeform"),
    path('resumelist', views.resumelist, name='resumelist'),
    path('editcontent1/<int:adcont_id>/', editcontent1, name='editcontent1'),
    path('dlt_content1/<int:id>/', dlt_content1, name='dlt_content1'),


    path('scontent1list/<int:studentprofile_id>/<int:content_id>/', views.scontent1list, name='scontent1list'),
    path('scontent1list/<int:studentprofile_id>/', views.scontent1list, name='scontent1list'),
    path('scontent1list/<int:content_id>/', views.scontent1list, name='scontent1list'),

    path('svideolist/<int:studentprofile_id>/<int:content_id>/', views.svideolist, name='svideolist'),
    path('svideolist/<int:studentprofile_id>/', views.svideolist, name='svideolist'),
    path('svideolist/<int:content_id>/', views.svideolist, name='svideolist'),

    path('alumni_index', views.alumni_index, name='alumni_index'),
    path('alumni/profile/<int:alumni_id>/', alumni_profile, name='alumni_profile'),
    # path('scontent2list', views.scontent2list, name='scontent2list'),


    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    # path('submit_review/', views.submit_review, name='submit_review'),
    path('create_blog_content/<int:alumni_id>/', create_blog_content, name='create_blog_content'),
    path('display_blog_content/<int:alumni_id>/', display_blog_content, name='display_blog_content'),
    path('alumni_blog/<int:studentprofile_id>/', views.alumni_blog, name='alumni_blog'),
    path('ad_alumniblog/', views.ad_alumniblog, name='ad_alumniblog'),
    path('bloglist2/<int:alumni_id>/', views.bloglist2, name='bloglist2'),
    path('dlt_blog/<int:id>/', dlt_blog, name='dlt_blog'),
    path('eventform/<int:alumni_id>/', eventform, name='eventform'),
    path('eventlist/<int:alumni_id>/', eventlist, name='eventlist'),
    path('editevent/<int:alumni_id>/<int:event_id>/', editevent, name='editevent'),
    path('delete_event/', views.delete_event, name='delete_event'),
    path('delete_blog_content/<int:content_id>/', views.delete_blog_content, name='delete_blog_content'),
    path('import-excel/', views.import_excel_data_view, name='import_excel_data'),
    path('aptform/', aptform, name='aptform'),
    path('aptform2',views.aptform2, name="aptform2"),
    path('apt_notification/<int:studentprofile_id>/', views.apt_notification, name='apt_notification'),

    path('conduct-aptitude-test/', conduct_aptitude_test, name='conduct_aptitude_test'),
    path('sevent/<int:studentprofile_id>/', views.sevent, name='sevent'),  
    path('company-event/<int:studentprofile_id>/', views.scevent, name='scevent'),  
    path('quiz_form/', views.quiz_form, name='quiz_form'),    
    path('error/',error,name='error'),
    path('company_event_form/', company_event_form, name='company_event_form'),
    path('ceventlist/', ceventlist, name='ceventlist'),
    path('edit_company_event/<int:event_id>/', views.edit_company_event, name='edit_company_event'),
    path('exam_view/', exam_view, name='exam_view'),
    path('save-and-next/', save_and_next, name='save_and_next'),
    path('create-question/', create_question, name='create_question'),
    path('apt_list_company/',apt_list_company, name='apt_list_company'),
    path('q_preview/',q_preview, name='q_preview'),
    path('edit/<int:question_id>/', views.edit_question, name='edit_question'),
    path('delete/<int:question_id>/', views.delete_question, name='delete_question'),    
    path('attend_exam/<int:studentprofile_id>/<int:company_profile_id>/', attend_exam, name='attend_exam'),
    path('submit_exam', views.submit_exam, name='submit_exam'),
    path('approved_aptitude/<int:aptitude_id>/', views.approved_aptitude, name='approved_aptitude'),
    path('apt_approve', views.apt_approve, name='apt_approve'),
    path('alumni_job_approve', views.alumni_job_approve, name='alumni_job_approve'),
    path('approved_alumnijob/<int:blog_id>/', views.approved_alumnijob, name='approved_alumnijob'),
    path('test-response/', views.test_response, name='test_response'),    # path('deleteevent/<int:alumni_id>/<int:event_id>/', views.deleteevent, name='deleteevent'),
    path('test_result', views.test_result, name='test_result'),
    path('shortlist_selected_students/', shortlist_selected_students, name='shortlist_selected_students'),
    path('webscrap/<int:studentprofile_id>/', webscrap, name='webscrap'),
    path('shortlist2/', shortlist2, name='shortlist2'),
    path('delete_aptd_result/<int:result_id>/', delete_aptd_result, name='delete_aptd_result'),
     path('schedule-interview/', schedule_interview, name='schedule_interview'),
     path('get_interview_details/', get_interview_details, name='get_interview_details'),
    path('sinter/<int:studentprofile_id>/', views.sinter, name='sinter'),
<<<<<<< HEAD:zillionhire/zillionhire/urls.py
    path('department-wise-placements/', department_wise_placements, name='department-wise-placements'),   
    path('admin_cevent', views.admin_cevent, name='admin_cevent'), 
=======
>>>>>>> 20df51b452a1e4e86df8a3cfd7cb2fa6da05e795:zillionhire/urls.py
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

