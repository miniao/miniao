# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render, render_to_response
from .models import Interviewarticle, Doctorarticle, Expertarticle, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext, loader, Context
import pymysql
import json


def interviewarticle_detail(request, pk):
    column = 'zhuanfang'
    url = 'http://127.0.0.1:8000' + request.path
    tmpurl = '/'.join(str(request.path).split('/')[:-1]) + '/'
    article = Interviewarticle.objects.filter(pk=pk, column=column, published=True)
    # classes = [{'column': '动态', 'slug': 'dongtai'}]
    relate = Interviewarticle.objects.filter(column=column, published=True)[0:6]
    belong = 'expert'
    column1 = '专访'
    if article:
        num = article[0].browser + 1
        article.update(browser=num)
        if "userid" in request.session and "identity" in request.session:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
            cursor = conn.cursor()
            userid = request.session.get("userid")
            cursor.execute("select * from userdata_favourite where userid=%s and url='%s'" % (userid, url))
            row = cursor.fetchone()
            if row:
                collect = True
            else:
                collect = False
            cursor.execute("select avg(scorenum) from userdata_score where url='%s'" % url)
            row1 = cursor.fetchone()
            if row1[0]:
                avgnum = row1[0]
            else:
                avgnum = 0
            cursor.execute("select scorenum from userdata_score where userid=%s and url='%s'" % (userid, url))
            row2 = cursor.fetchone()
            if row2:
                scorenum = '%.1f' % float(row2[0])
            else:
                scorenum = False
            return render(request, 'article_detail.html', {'tmpurl': tmpurl, 'relate': relate, 'belong': belong, 'column1': column1, 'article': article[0], 'collect': collect, 'avgnum': avgnum,
                                                    'scorenum': scorenum})
        else:
            return render(request, 'article_detail.html', {'tmpurl': tmpurl, 'relate': relate, 'belong': belong, 'column1': column1, 'article': article[0]})
    else:
        return HttpResponseRedirect('/')


def interviewarticle(request):
    column = 'zhuanfang'
    tmpurl = str(request.path).strip('/')
    classes = [{'column': '专家', 'slug': 'zhuanjia'}, {'column': '大家风范', 'slug': 'fengfan'},
               {'column': '专访', 'slug': 'zhuanfang'}]
    column1 = '专访'
    belong = 'expert'
    article = Interviewarticle.objects.filter(column=column, published=True)
    if article:
        objects, page_range = my_pagination(request, article, 2)
        return render_to_response('article_column.html', {'classes': classes, 'column': column1, 'belong': belong, 'objects':objects,'page_range':page_range, 'tmpurl':tmpurl},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


"""def doctorarticle_detail(request, column, pk):
    url = 'http://127.0.0.1:8000' + request.path
    article = Doctorarticle.objects.filter(pk=pk, column=column, published=True)
    if article:
        num = article[0].browser + 1
        article.update(browser=num)
        if "userid" in request.session and "identity" in request.session:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
            cursor = conn.cursor()
            userid = request.session.get("userid")
            cursor.execute("select * from userdata_favourite where userid=%s and url='%s'" % (userid, url))
            row = cursor.fetchone()
            if row:
                collect = True
            else:
                collect = False
            cursor.execute("select avg(scorenum) from userdata_score where url='%s'" % url)
            row1 = cursor.fetchone()
            if row1[0]:
                avgnum = row1[0]
            else:
                avgnum = 0
            cursor.execute("select scorenum from userdata_score where userid=%s and url='%s'" % (userid, url))
            row2 = cursor.fetchone()
            if row2:
                scorenum = '%.1f' % float(row2[0])
            else:
                scorenum = False
            return render(request, 'article.html', {'article': article[0], 'collect': collect, 'avgnum': avgnum,
                                                    'scorenum': scorenum})
        else:
            return render(request, 'article.html', {'article': article[0]})
    else:
        return HttpResponseRedirect('/')"""
def doctorarticle_detail(request, pk):
    column = 'fengfan'
    # url = 'http://127.0.0.1:8000' + request.path
    tmpurl = '/'.join(str(request.path).split('/')[:-1]) + '/'
    article = Doctorarticle.objects.filter(pk=pk, column=column, published=True)
    belong = 'expert'
    column1 = '大家风范'
    if article:
        num = article[0].browser + 1
        article.update(browser=num)
        """if "userid" in request.session and "identity" in request.session:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
            cursor = conn.cursor()
            userid = request.session.get("userid")
            cursor.execute("select * from userdata_favourite where userid=%s and url='%s'" % (userid, url))
            row = cursor.fetchone()
            if row:
                collect = True
            else:
                collect = False
            cursor.execute("select avg(scorenum) from userdata_score where url='%s'" % url)
            row1 = cursor.fetchone()
            if row1[0]:
                avgnum = row1[0]
            else:
                avgnum = 0
            cursor.execute("select scorenum from userdata_score where userid=%s and url='%s'" % (userid, url))
            row2 = cursor.fetchone()
            if row2:
                scorenum = '%.1f' % float(row2[0])
            else:
                scorenum = False
            return render(request, 'article_fengfan_detail.html', {'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'collect': collect, 'avgnum': avgnum,
                                                    'scorenum': scorenum})
        else:"""
        return render(request, 'article_fengfan_detail.html', {'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl})
    else:
        return HttpResponseRedirect('/')

def doctorarticle(request):
    column = 'fengfan'
    tmpurl = str(request.path).strip('/')
    classes = [{'column': '专家', 'slug': 'zhuanjia'}, {'column': '大家风范', 'slug': 'fengfan'},
               {'column': '专访', 'slug': 'zhuanfang'}]
    column1 = '大家风范'
    belong = 'expert'
    article = Doctorarticle.objects.filter(column=column, published=True)
    if article:
        objects, page_range = my_pagination(request, article, 2)
        return render_to_response('article_column.html', {'classes': classes, 'column': column1, 'belong': belong, 'objects':objects,'page_range':page_range, 'tmpurl':tmpurl},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


def expertarticle_detail(request, pk):
    column = 'zhuanjia'
    article = Expertarticle.objects.filter(pk=pk, column=column, published=True)
    comment = Comment.objects.filter(name=article[0].name, published=True)
    if article:
            return render(request, 'article_expert_detail.html', {'article': article[0], 'comment': comment})
    else:
        return HttpResponseRedirect('/')


def expertarticle(request):
    sel_province = ""
    sel_department = ""
    column = 'zhuanjia'
    classes = [{'column': '专家', 'slug': 'zhuanjia'}, {'column': '大家风范', 'slug': 'fengfan'}, {'column': '专访', 'slug': 'zhuanfang'}]
    column1 = '专家'
    if "province" in request.GET and "department" in request.GET:
        sel_province = request.POST["province"]
        sel_department = request.POST["department"]
        article = Expertarticle.objects.filter(column=column, province=sel_province, department=sel_department, published=True)
    elif "province" in request.GET:
        sel_province = request.POST["province"]
        article = Expertarticle.objects.filter(column=column, province=sel_province, published=True)
    elif "department" in request.GET:
        sel_department = request.POST["department"]
        article = Expertarticle.objects.filter(column=column, department=sel_department, published=True)
    else:
        article = Expertarticle.objects.filter(column=column, published=True)
    tmpurl = str(request.path).strip('/')
    # article = Expertarticle.objects.filter(column=column, published=True)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    res = cursor.execute("select distinct department from expert_expertarticle")
    row = cursor.fetchmany(res)
    department = []
    for i in row:
        department.append(str(i[0]))
    res1 = cursor.execute("select distinct province from expert_expertarticle")
    row1 = cursor.fetchmany(res1)
    province = []
    for i in row1:
        province.append(str(i[0]))
    if article:
        objects, page_range = my_pagination(request, article, 2)
        return render_to_response('article_expert.html', {'classes': classes, 'column': column1, 'sel_province': sel_province, 'sel_department': sel_department, 'objects':objects,'page_range':page_range, 'tmpurl':tmpurl, 'department': department, 'province': province},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

# 评论
def givecomment(request):
    if request.method == 'POST':
        try:
            url = request.POST['url']
            content = request.POST['content']
        except:
            return HttpResponseRedirect('/')
        expertid  = str(url).strip('/').split('/')[-1]
        tmp = Expertarticle.objects.filter(id=expertid)
        name = tmp[0].name
        Comment.objects.create(name=name, content=content)
        return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
    else:
        return HttpResponseRedirect('/')
# 赞
def zan(request):
    if request.method == 'GET':
        try:
            url = request.GET['url']
        except:
            return HttpResponseRedirect('/')
        expertid = str(url).strip('/').split('/')[-1]
        tmp = Expertarticle.objects.filter(id=expertid)
        ori = tmp[0].zan
        tmp.update(zan=ori+1)
    else:
        return HttpResponseRedirect('/')

def my_pagination(request, queryset, display_amount, after_range_num=3, bevor_range_num=2):
    paginator = Paginator(queryset,display_amount)
    try:
        page = int(request.GET["page"])
    except:
        page = 1
    try:
        object = paginator.page(page)
    except (EmptyPage, InvalidPage):
        object = paginator.page(paginator.num_pages)
    except:
        object = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]
    else:
        page_range = paginator.page_range[0:page+bevor_range_num]
    return object,page_range