from django.shortcuts import render
from apps.message_form.models import Message
#配置一个html页面显示的逻辑
#1. 配置url
#2. 配置对应的views逻辑
#3. 拆分静态文件（css, js, images)放入到static，html放入到templates之下
    #1. 可以放到对应的app下面
    #2. 也可以放入到全局的templates和static目录之下
#4. 配置全局的static文件访问路径的配置

# get 拉，post 推
# Create your views here.
def message_form(request):
    # queryset 1.进行for循环 2.进行切片
    # queryset本身没有执行sql操作

    # all_messages = Message.objects.all()[:1]
    # print(all_messages)

    # 2.filter
    # all_messages = Message.objects.filter(name='jack')
    # all_messages.delete()  删除全部数据
    # print(all_messages.query)
    # for message in all_messages:
    #     print(message.name)

    # 3.get 返回的是一个对象，数据不存在或者有多条数据存在会抛出异常
    # try:
    #     message = Message.objects.get(name='jack')
    # except Message.DoesNotExist as e:
    #     pass
    # except Message.MultipleObjectsReturned as e:
    #     pass
    # message.delete() 删除该条数据
    # print(message.name)

    # 进行数据插入操作
    message = Message()
    # message.name = 'kiven'
    # message.email = 'kiven@gmail.com'
    # message.address = 'CA'
    # message.message = 'hi'
    # # 如果存在则更新，如果不存在则插入
    # message.save()

    # 从html中提取数据保存到数据库中
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message_text = request.POST.get('message', '')

        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = message_text
        message.save()

    return render(request, 'message_form.html')