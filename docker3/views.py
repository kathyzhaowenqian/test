from django.shortcuts import render
from docker3.models import *
from django_redis import get_redis_connection
from django.core.cache import cache

# Create your views here.
def Docker3(request):

    
    

    
    data1= ADAIADAI.objects.all()

    redis_conn = get_redis_connection('default')
    keys = redis_conn.keys('*')
    # print('keys',keys)
    data2=[]
    for i in keys:
        i=i.decode('utf-8')
        # print('i',i)
        age = redis_conn.hget(i, 'age')
        weight = redis_conn.hget(i, 'weight')
        # values = redis_conn.hgetall(i)  # 获取哈希表数据
        # print('values',values)
        data2.append({
            'name': i,
            'age': age.decode('utf-8'),
            'weight': weight.decode('utf-8')
        })
        # print('data2',data2)

    context = {'data1': data1,'data2':data2}  # 将数据传递给HTML模板

    # cache.set('adai2',{'name':'adai','age':4})

    # cache_result = cache.get('adai2')
    # print(cache_result,type(cache_result))

    return render(request, 'adaidocker3.html', context)

