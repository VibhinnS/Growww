from django.urls import path
from .views import ProductViewSet
urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('products/<str:primary_key>', ProductViewSet.as_view({
        'get':'retrive',
        'put':'update',
        'delete':'destroy'
    }))
]
