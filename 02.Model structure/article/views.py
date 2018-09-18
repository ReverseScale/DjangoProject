from django.shortcuts import render_to_response, get_object_or_404
from .models import Article

# Create your views here.
def article_detail(request, article_id):

	# get_object_or_404 简化写法
	article = get_object_or_404(Article, pk=article_id)
	context = {}
	context['article_obj'] = article
	return render_to_response("article_detail.html", context)


	# render + Http404 写法
	# 注意：
	# （
	# 需要引入
	# from django.shortcuts import render，render_to_response
	# 和 
	# from django.http import HttpResponse, Http404
	# ）
	# 
	# try:
	# 	article = Article.objects.get(id=article_id)
	# 	context = {}
	# 	context['article_obj'] = article
	# 	# return render(request, "article_detail.html", context)
	# 	return render_to_response("article_detail.html", context)
	# except Article.DoesNotExist:
	# 	raise Http404("not found")
	# # return HttpResponse("<h2>文章标题: %s</h2> <br> 文章内容: %s" % (article.title, article.content))


