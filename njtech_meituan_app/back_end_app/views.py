from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
import os
import math
from .models import Book
from .models import Purchase_Order
from .models import Food
from .models import Customer
from .models import Food_Category
from .models import Shopping_Cart
from .models import Administrator
from .models import Complaints
from django.shortcuts import render
from django.shortcuts import HttpResponse
import time
# Create your views here.

@require_http_methods(["GET"])
def add_book(request):
    response={}
    try:
        book = Book(book_name = request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response={}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json",books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



@require_http_methods(["GET"])
def add_purchase_order(request):
    tmpID = request.GET.get('cartid')
    response={}
    try:
        purchase_order = Purchase_Order(
            food_id = request.GET.get('food_id'),
            customer_id = request.GET.get('customer_id'),
            remarks = request.GET.get('remarks'),
            amount_money = request.GET.get('amount_money'),
            quantity = request.GET.get('quantity'),
            )
        purchase_order.save()
        print(tmpID)
        shopping_cart = Shopping_Cart.objects.get(id = tmpID)
        shopping_cart.isdeleted = True
        shopping_cart.save()
        
        
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



@require_http_methods(["GET"])
def register_account(request):
    response={}
    try:
        customer = Customer(mobile_phone = request.GET.get('mobile_phone'),
                            sex = request.GET.get('sex'),
                            nickname = request.GET.get('nickname'),
                            passport = request.GET.get('passport'),
                            password = request.GET.get('password'),
                            avatar = request.GET.get('avatar'),
                            )
        customer.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

#################################################################

def get_all_user(request):
    response={}
    try:
        customer = Customer.objects.filter()
        response['list'] = json.loads(serializers.serialize("json",customer))

        for elee in response['list']:
            del elee['fields']['password']
            #del elee['fields']['avatar']
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
###################################################################



@require_http_methods(["GET"])
def add_food_variety(request):
    response={}
    try:
        food = Food(
            category_id = request.GET.get('category_id'),
            name = request.GET.get('name'),
            amount_money = request.GET.get('amount_money'),
            introduction = request.GET.get('introduction'),
            #add_time = request.GET.get('add_time'),
            #stop_time = request.GET.get('stop_time'),
            picUrl1 = request.GET.get('url1'),
            picUrl2 = request.GET.get('url2'),
            picUrl3 = request.GET.get('url3'),
            picUrl4 = request.GET.get('url4'),
            )
        food.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)




@require_http_methods(["GET"])
def get_food_info(request):
    tmpID = request.GET.get('id')
    response={}
    try:
        food = Food.objects.filter(id = tmpID)
        response['list'] = json.loads(serializers.serialize("json",food))

        for elee in response['list']:
            elee['fields']['urluse'] = [None]*4
            elee['fields']['urluse'][0] = elee['fields']['picUrl1']
            elee['fields']['urluse'][1] = elee['fields']['picUrl2']
            elee['fields']['urluse'][2] = elee['fields']['picUrl3']
            elee['fields']['urluse'][3] = elee['fields']['picUrl4']
            del elee['fields']['picUrl1']
            del elee['fields']['picUrl2']
            del elee['fields']['picUrl3']
            del elee['fields']['picUrl4']
            
            food_categoryyyy = Food_Category.objects.filter(id = elee['fields']["category_id"])
            tmpnamelist = json.loads(serializers.serialize("json",food_categoryyyy))
            elee['fields']['category_id'] = (tmpnamelist[0]['fields']['name'])    
            
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



######################################################
@require_http_methods(["GET"])
def get_all_page(request):
    response ={}
    tmpp={}
    try:
        food = Food.objects.filter()
        tmplist = json.loads(serializers.serialize("json",food))
        tmpp['list'] = json.loads(serializers.serialize("json",food))
        for ele in tmpp['list']:
            del ele['fields']['picUrl2']
            del ele['fields']['picUrl3']
            del ele['fields']['picUrl4']
            del ele['fields']['introduction']
            del ele['fields']['add_time']
            del ele['fields']['stop_time']
            if(ele['fields']['isexpired']==True):
                tmpp['list'].remove(ele)
                continue
            del ele['fields']['isexpired']
        response["allPage"] = math.ceil(len(tmpp['list'])/20)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)




@require_http_methods(["GET"])
def get_page_by_category(request):
    response ={}
    tmpp={}
    try:
        category = request.GET.get('category_id')
        food = Food.objects.filter(category_id = category)
        tmplist = json.loads(serializers.serialize("json",food))
        tmpp['list'] = json.loads(serializers.serialize("json",food))
        for ele in tmpp['list']:
            del ele['fields']['picUrl2']
            del ele['fields']['picUrl3']
            del ele['fields']['picUrl4']
            del ele['fields']['introduction']
            del ele['fields']['add_time']
            del ele['fields']['stop_time']
            if(ele['fields']['isexpired']==True):
                tmpp['list'].remove(ele)
                continue
            del ele['fields']['isexpired']
        print(tmpp['list'])
        response["allPage"] = math.ceil(len(tmpp['list'])/20)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
######################################################

def get_page_food(request):
    page = request.GET.get('page')
    pagestart = (int(page)-1)*20
    pageend = int(page)*20
    response={}
    try:
        food = Food.objects.filter()
        tmplist = json.loads(serializers.serialize("json",food))
        response['list'] = json.loads(serializers.serialize("json",food))
        for ele in response['list']:
            del ele['fields']['picUrl2']
            del ele['fields']['picUrl3']
            del ele['fields']['picUrl4']
            del ele['fields']['introduction']
            del ele['fields']['add_time']
            del ele['fields']['stop_time']
            if(ele['fields']['isexpired']==True):
                response['list'].remove(ele)
                continue
            del ele['fields']['isexpired']
        response['list'] = response['list'][pagestart:pageend]
        for elee in response['list']:
            food_categoryyyy = Food_Category.objects.filter(id = elee['fields']["category_id"])
            tmpnamelist = json.loads(serializers.serialize("json",food_categoryyyy))
            elee['fields']['category_id'] = (tmpnamelist[0]['fields']['name'])            
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



def get_page_food_by_category(request):
    page = request.GET.get('page')
    category = request.GET.get('category_id')
    pagestart = (int(page)-1)*20
    pageend = int(page)*20
    response={}
    try:
        food = Food.objects.filter(category_id = category)
        tmplist = json.loads(serializers.serialize("json",food))
        response['list'] = json.loads(serializers.serialize("json",food))
        for ele in response['list']:
            del ele['fields']['picUrl2']
            del ele['fields']['picUrl3']
            del ele['fields']['picUrl4']
            del ele['fields']['introduction']
            del ele['fields']['add_time']
            del ele['fields']['stop_time']
            if(ele['fields']['isexpired']==True):
                response['list'].remove(ele)
                continue
            del ele['fields']['isexpired']
        response['list'] = response['list'][pagestart:pageend]
        for elee in response['list']:
            food_categoryyyy = Food_Category.objects.filter(id = elee['fields']["category_id"])
            tmpnamelist = json.loads(serializers.serialize("json",food_categoryyyy))
            elee['fields']['category_id'] = (tmpnamelist[0]['fields']['name'])            
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['GET'])
def add_food_category_variety(request):
    response={}
    try:
        food_category = Food_Category(
            name = request.GET.get('name'),
            remarks = request.GET.get('remarks')
            )
        food_category.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_all_food_category(request):
    response={}
    try:
        food_category = Food_Category.objects.filter()
        response['list'] = json.loads(serializers.serialize("json",food_category))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def get_food_category_info(request):
    tmpID = request.GET.get('id')
    response={}
    try:
        food_category = Food_Category.objects.filter(id = tmpID)
        response['list'] = json.loads(serializers.serialize("json",food_category))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['GET'])
def add_shopping_cart_content(request):
    response={}
    try:
        customerTempID = request.GET.get('customer_id')
        foodTempID = request.GET.get('food_id')
        isselectTemp = request.GET.get('isselected')
        numTemp = request.GET.get('quantity')

        remarkTemp = request.GET.get('remarks')
        
        flag =False
        try:
            food_search = Shopping_Cart.objects.get( food_id = foodTempID , customer_id = customerTempID,
                                                 isdeleted = False)
            print(food_search)
            if(food_search):
                food_search.isselected = isselectTemp
                food_search.quantity = numTemp
                food_search.remarks = remarkTemp
                print(food_search.isselected)
                food_search.save()
                flag =True
        except Exception as e:
            print(str(e))
            None

        if(flag == False):
            shopping_cart = Shopping_Cart(
                customer_id = request.GET.get('customer_id'),
                food_id = request.GET.get('food_id'),
                quantity = request.GET.get('quantity'),
                amount_money = request.GET.get('amount_money'),
                remarks = request.GET.get('remarks'),
                isselected = isselectTemp
                )
            shopping_cart.save()

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



def get_shopping_cart_content(request):
    userID = request.GET.get('id')
    response={}
    try:
        shopping_cart = Shopping_Cart.objects.filter(customer_id = userID,
                                                     isdeleted = False)
        response['list'] = json.loads(serializers.serialize("json",shopping_cart))
        
        
        for ele in response['list']: 
            foodid = ele["fields"]["food_id"]
            food = Food.objects.get(id = foodid)
            ele["fields"]["unit_price"] = food.amount_money
            ele["fields"]["foodname"] = food.name

        for ele in response['list']:
            if(ele["fields"]["isdeleted"] == True):
                response['list'].remove(ele)

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        print(e)
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def get_customer_order(request):
    page = request.GET.get('page')
    userID = request.GET.get('id')
    response={}
    try:
        purchase_order = Purchase_Order.objects.filter(customer_id = userID)
        response['list'] =  json.loads(serializers.serialize("json",purchase_order))
        response['list'].reverse()
        for ele in response['list']: 
            foodid = ele["fields"]["food_id"]
            food = Food.objects.get(id = foodid)
            ele["fields"]["unit-price"] = food.amount_money
            ele["fields"]["foodname"] = food.name
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def get_customer_order_page(request):
    response={}
    count={}
    try:
        userID = request.GET.get('id')
        purchase_order = Purchase_Order.objects.filter(customer_id = userID)
        count['list'] =  json.loads(serializers.serialize("json",purchase_order))
        response["allPage"] = math.ceil(len(count['list'])/20)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def get_all_order(request):
    page = request.GET.get('page')
    response={}
    try:
        purchase_order = Purchase_Order.objects.filter()
        response['list'] =  json.loads(serializers.serialize("json",purchase_order))
        response['list'].reverse()
        for ele in response['list']: 
            foodid = ele["fields"]["food_id"]
            food = Food.objects.get(id = foodid)
            ele["fields"]["unit-price"] = food.amount_money
            ele["fields"]["foodname"] = food.name
        for ele in response['list']: 
            userid = ele["fields"]["customer_id"]
            user = Customer.objects.get(id = userid)
            ele["fields"]["customername"] = user.nickname
            
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def get_all_order_page(request):
    response={}
    count={}
    try:
        purchase_order = Purchase_Order.objects.filter()
        count['list'] =  json.loads(serializers.serialize("json",purchase_order))
        response["allPage"] = math.ceil(len(count['list'])/20)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def get_all_complaints(request):
    response={}
    try:
        compliants = Complaints.objects.filter()
        response['list'] =  json.loads(serializers.serialize("json",compliants))
        for ele in response['list']: 
            purchaseorderid = ele["fields"]["purchase_order_id"]
            purchase_order = Purchase_Order.objects.get(id = purchaseorderid)
            foodid = purchase_order.food_id
            food =Food.objects.get(id = foodid)            
            ele["fields"]["food_id"] = food.id
            ele["fields"]["food_name"] = food.name
        for ele in response['list']: 
            userid = ele["fields"]["customer_id"]
            user = Customer.objects.get(id = userid)
            ele["fields"]["customer_id"] = user.id
            ele["fields"]["customer_nickname"] = user.nickname
        response['list'].reverse()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



########################################
def delete_shopping_cart_content(request):
    userID = request.GET.get('userid')
    foodID = request.GET.get('foodid')
    response={}
    try:
        shopping_cart = Shopping_Cart.objects.get(customer_id = userID
                         ,food_id =foodID)
        shopping_cart.isdeleted = True
        shopping_cart.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def delete_customer(request):
    phone = request.GET.get('mobile_phone')
    response={}
    try:
        customer = Customer.objects.get(mobile_phone = phone)
        customer.isdeleted = True
        customer.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
    

def delete_food(request):
    tmpID = request.GET.get('foodid')
    response={}
    try:
        food = Food.objects.get(id = tmpID)
        food.isexpired = True
        food.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def delete_purchase_order(request):
    tmp = request.GET.get('orderid')
    response={}
    try:
        purchase_order = Purchase_Order.objects.get( id = tmp )
        purchase_order.status = 1
        purchase_order.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def delete_food_category(request):
    tmp = request.GET.get('category_id')
    response={}
    try:
        food_category = Food_Category.objects.get(id = tmp)
        food_category.isDelete = True
        purchase_order.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
        
def delete_admin(request):
    tmp_id = request.GET.get('id')
    response = {}
    try:
        admin = Administrator.objects.get(id = tmp_id)
        admin.isdeleted = True
        admin.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def delete_complaints(request):
    tmp_id = request.GET.get('id')
    response = {}
    try:
        complaints = Complaints.objects.get(id = tmp_id)
        complaints.isdeleted = True
        complaints.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
        
########################################

def add_admin(request):
    response={}
    try:
        administrator = Administrator(
            name = request.GET.get('name'),
            password = request.GET.get('password'),
            )
        administrator.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def add_complaints(request):
    response={}
    try:
        complaints = Complaints(
            purchase_order_id = request.GET.get('purchase_order_id'),
            customer_id = request.GET.get('customer_id'),
            content = request.GET.get('content'),
            )
        complaints.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



##########################################################################
def upload_pic(request):
    response={}
    try:
        if request.method == "POST":    # 请求方法为POST时，进行处理
            print(request)
            myFile =request.FILES.get("file", None)    # 获取上传的文件，如果没有文件，则默认为None 
            print(request.FILES)
            nowtime = str(time.time())
            destination = open(os.path.join("E:\\web_django\\njtech_meituan_app\\back_end_app\\pic",nowtime+myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作 
            for chunk in myFile.chunks():      # 分块写入文件 
                destination.write(chunk) 
            destination.close()
            response['path'] = "http://10.22.252.59:8080/pic/"+ nowtime+myFile.name
            #response['path'] = "http://192.168.43.230:8080/pic/"+ nowtime+myFile.name
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

##########################################################################





def customer_login(request):
    if(request.method == "POST"):
        print(request.POST.get("userphone"))
        response={}
        userphone = request.POST.get("userphone")
        pswd = request.POST.get("pswd")
        try:
            ret = Customer.objects.get(mobile_phone = userphone,
                                          password = pswd)      
            if ret:
                response['id'] = ret.id
                response['name'] = ret.nickname
                response['phone'] = ret.mobile_phone
                response['sex'] = ret.sex
                response['passport'] = ret.passport
                response['create_time'] = ret.create_time
                response['isdelete'] = ret.isdeleted

                if(response['isdelete'] == False):
                    response['msg'] = 'success'
                    response['error_num'] = 0
                else:
                    response['msg'] = 'account has been deleted'
                    response['error_num'] = 1
                return JsonResponse(response)
            else:
                response['msg'] = 'ERROR Incorrect username or password'
                response['error_num'] = 2
                return  JsonResponse(response)
        except Exception as e:
            print(str(e))
            response['msg'] = 'ERROR Incorrect username or password'
            response['error_num'] = 3
            return  JsonResponse(response)


def admin_login(request):
    if(request.method == "POST"):
        response={}
        username = request.POST.get("name")
        pswd = request.POST.get("pswd")
        try:
            ret = Administrator.objects.get(name = username,
                                          password = pswd)      
            if ret:
                response['id'] = ret.id
                response['name'] = ret.name
                response['isdelete'] = ret.isdeleted

                if(response['isdelete'] == False):
                    response['msg'] = 'success'
                    response['error_num'] = 0
                else:
                    response['msg'] = 'account has been deleted'
                    response['error_num'] = 1
                return JsonResponse(response)
            else:
                response['msg'] = 'ERROR Incorrect username or password'
                response['error_num'] = 2
                return  JsonResponse(response)
        except Exception as e:
            print(str(e))
            response['msg'] = 'ERROR Incorrect username or password'
            response['error_num'] = 3
            return  JsonResponse(response)



def customer_pswd_modify(request):
    response={}
    try:
        if(request.method == "POST"):
            newpswd = request.POST.get("pswd")
            is_login = request.COOKIES.get("is_login",None)
            if (is_login):
                userid = request.COOKIES.get("id",123)
                nowuser = Customer.objects.get(id = userid)
                nowuser.password = newpswd
                nowuser.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def admin_pswd_modify(request):
    response={}
    try:
        if(request.method == "POST"):
            newpswd = request.POST.get("pswd")
            is_login = request.COOKIES.get("is_login",None)
            if (is_login):
                userid = request.COOKIES.get("id",123)
                nowuser = Administrator.objects.get(id = userid)
                nowuser.password = newpswd
                nowuser.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
