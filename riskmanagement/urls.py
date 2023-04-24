from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)
from .apps.processes.urls import router as processesRouter
from .apps.risks.urls import router as risksRouter
from .apps.accounts.urls import router as accountsRouter
from .apps.permissions.urls import router as permissionsRouter
from .viewsLdap import LDAPLogin,LDAPLogout 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(processesRouter.urls)),
    path('api/', include(risksRouter.urls)),
    path('api/', include(accountsRouter.urls)),
    path('docs/', include_docs_urls(title='Risk Management API')),
    path('processes', processesRouter.get_api_root_view()),
    #path('risks', risksRouter.get_api_root_view()),
    path('accounts', accountsRouter.get_api_root_view()),
    path('permissions',permissionsRouter.get_api_root_view()),
    # Reset password
        # reset for admin in django
    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),  name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
        # reset for api 
    path('accounts/password-reset/',include('django_rest_resetpassword.urls', namespace='password_reset')),

    #JWT

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # LDAP
    path('login', LDAPLogin.as_view()),
    path('logout', LDAPLogout.as_view()),
]
