from django.conf.urls import url,include
from . import views
urlpatterns = [url(r'add_book$',views.add_book,),url(r'show_books$',views.show_books,),

               url(r'register_account$',views.register_account,),
               url(r'add_purchase_order$',views.add_purchase_order,),
               url(r'add_food_variety$',views.add_food_variety,),
               url(r'add_food_category_variety$',views.add_food_category_variety,),
               url(r'add_shopping_cart_content$',views.add_shopping_cart_content,),
               url(r'add_admin$',views.add_admin,),
               url(r'add_complaints$',views.add_complaints,),

               url(r'get_food_info$',views.get_food_info,),
               url(r'get_all_food_category$',views.get_all_food_category,),
               url(r'get_food_category_info$',views.get_food_category_info,),
               url(r'get_page_food$',views.get_page_food,),
               url(r'get_page_food_by_category$',views.get_page_food_by_category,),
               url(r'get_shopping_cart_content$',views.get_shopping_cart_content,),
               url(r'get_all_page$',views.get_all_page,),
               url(r'get_page_by_category$',views.get_page_by_category,),
               url(r'get_customer_order$',views.get_customer_order,),
               url(r'get_customer_order_page$',views.get_customer_order_page,),
               
               url(r'get_all_order$',views.get_all_order,),
               url(r'get_all_order_page$',views.get_all_order_page,),

               url(r'get_all_complaints$',views.get_all_complaints,),

               url(r'get_all_users$',views.get_all_user,),



               
               url(r'delete_customer$',views.delete_customer,),
               url(r'delete_food$',views.delete_food,),
               url(r'delete_purchase_order$',views.delete_purchase_order,),
               url(r'delete_food_category$',views.delete_food_category,),
               url(r'delete_shopping_cart_content$',views.delete_shopping_cart_content,),
               url(r'delete_admin$',views.delete_admin,),
               url(r'delete_complaints$',views.delete_complaints,),


               url(r'customer_login$',views.customer_login,),
               url(r'admin_login$',views.admin_login,),


               url(r'upload_pic$',views.upload_pic,),
               ]
