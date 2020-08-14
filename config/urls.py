from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from rest_framework import routers
# from api.activity_picture.views import APIView
#
# router = routers.DefaultRouter(trailing_slash= False)
# router.register('aps',APIView)

##카카오 로그인
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ##카카오 로그인
    path('', include('api.urls')),
    path('account/', include('api.urls', namespace='accounts')),
    path('api-jwt-auth/', obtain_jwt_token),
    path('api-jwt-auth/refresh/', refresh_jwt_token),
    path('api-jwt-auth/verify/', verify_jwt_token),
    path('rest-auth', include('rest_auth.urls')),
]

# swagger 정보 설정, 관련 엔드포인트 추가
# swagger 엔드포인트는 DEBUG Mode에서만 노출
schema_view = get_schema_view(
    openapi.Info(
        title="WiseStudy API",
        default_version='v1',
        description=
        """
        WiseStudy Open API 문서 페이지

        "슬기로운 공부생활" 스터디 앱 만들기 위한 API 문서입니다.
        
        팀원:Team_Algo
        """,
        terms_of_service="https://github.com/wisestudy",
        contact=openapi.Contact(email="wisestudy@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^docs$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        # UI 상태 불량으로 인해 redoc은 이제 제공하지 않습니다.
        # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

APPEND_SLASH = False
