from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/accounts/', include('accounts.urls')),
    path('api/bootcamps/',include('bootcamps.urls')),
    path('api/advcourses/',include('advcourses.urls')),
    path('api/tickets/', include('tickets.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/blogs/', include('blogs.urls'))
]
