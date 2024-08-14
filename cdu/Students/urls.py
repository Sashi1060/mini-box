from . import views  # Import your views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('students/', views.get_all_students, name='get_all_students'),
    path('update/<str:college_id>/', views.update_student, name='update_student'),
    path('delete_account/<str:college_id>/', views.delete_account, name='delete_account'),
    path('login/', views.login_student, name='login_student'),  # Add login URL
    path('logout/', views.logout_student, name='logout_student'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 
    path('profile/', views.get_user_profile, name='get_user_profile'),


]