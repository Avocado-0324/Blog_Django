from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown


def index(request):
    post_list = Post.objects.all().order_by('created_time')
    # 相当于是定义了一个 业务逻辑（logic）
    # index这个视图函数（类比java的Servlet）需要根据创建时间倒序来显示所有文章标题
    return render(request, 'blog/index.html', context={'post_list': post_list})
    # 类似于Servlet的forward


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 定义文章详情，从URL中捕捉文章的id之后在数据库当中获取与之对应的Post数据（也就是文章）
    # 这里用到了 get_object_or_404。其作用是：当传入的pk对应的Post在数据库存在时，return对应的post数据
    # 如果不存在，就给用户返回一个404错误，已表明该文章不存在
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 将Markdown格式的文本解析成HTML文本 ➡️ 调用markdown的库

    return render(request, 'blog/detail.html', context={'post': post})
