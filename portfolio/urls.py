from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customer/create/', views.customer_new, name='customer_new'),

    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),

    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),

    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name='password_reset'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="registration/reset_email_sent.html"),
         name='reset_email_sent'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset_confirm.html"),
         name='reset_confirm'),
    path('accounts/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/reset_complete.html"),
         name='reset_complete'),

    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"),
         name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_changed.html"),
         name='password_changed'),
]
