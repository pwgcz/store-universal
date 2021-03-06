from django.urls import path
from store_web import views

urlpatterns = [
    path("orders/", views.OrdersList.as_view(), name="orders-list"),
    path("orders/<int:pk>/", views.OrdersDetails.as_view()),
    path("staff/orders/", views.OrdersListStaff.as_view(), name="orders-list-staff"),
    path("staff/orders/<int:pk>/", views.OrdersDetailsStaff.as_view()),
    path("order-items/", views.OrderItemList.as_view(), name="order-items-list"),
    path("order-items/<int:pk>/", views.OrderItemDetails.as_view()),
    path("address/", views.AddressList.as_view(), name="address-list"),
    path("address/<int:pk>/", views.AddressDetails.as_view()),
    path("cart-items/", views.CartItemList.as_view(), name="cart-items-list"),
    path("cart-items/<int:pk>/", views.CartItemDetails.as_view()),
    path("categories/", views.CategoryList.as_view(), name="categories-list"),
    path(
        "staff/categories/", views.CategoryListStaff.as_view(), name="categories-list"
    ),
    path("staff/categories/<int:pk>/", views.CategoryDetailsStaff.as_view()),
    path("products/", views.ProductList.as_view(), name="products-list"),
    path("products/<int:pk>/", views.ProductDetails.as_view()),
    path(
        "staff/products/", views.ProductListStaff.as_view(), name="products-list-staff"
    ),
    path("staff/products/<int:pk>/", views.ProductDetailsStaff.as_view()),
]
