from .import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('loan-distribution',views.loan_distribution,name='loan_distribution'),
    path('loan-management',views.loan_management,name='loan_management'),
    path('member-registration',views.member_registration,name="member_registration"),
    path('login/',views.login,name='login'),
    path('loan-deposit',views.loan_deposit,name='loan_deposit'),
    path('rules', views.rules, name='rules'),
    path('bachatgat-registration/', views.bachatgat_registration, name='bachatgat_registration'),
    path('success', views.success_page, name='success_page'),
    path('register-member/', views.register_member, name='register_member'),

]
