from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(f'', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name="home"),
    path('menu-items/', views.MenuItemsView.as_view(), name="menuitem-list"),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name="menuitem-details"),
    path('booking/', include(router.urls)),
]