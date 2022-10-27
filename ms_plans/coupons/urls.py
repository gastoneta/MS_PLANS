from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import CouponViewSet

router = DefaultRouter()

router.register(r'coupons', CouponViewSet, basename='coupon_router')

urlpatterns = []
urlpatterns += router.urls 