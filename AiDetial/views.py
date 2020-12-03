from django.shortcuts import render

from django.forms import forms
from DjangoUeditor.forms import UEditorField
from  DjangoUeditor.widgets import UEditorWidget

from .models import Aidetial, Aidata, Aisort, Aidemo

# Create your views here.

from django.template.defaulttags import register

from .test_echarts import *
from pyecharts import options as opts
from pyecharts.charts import Grid,Page

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def detial(request,project):

    print(project)
    
    # 项目介绍
    detial_title = Aidetial.objects.filter(title=project)

    try:
        latest_detial = detial_title.latest('createdate')
        title_detial = latest_detial.title
        detial_detail = latest_detial.detail
    except Aidetial.DoesNotExist:
        title_detial = None
        detial_detail = None

    # 评价指标介绍

    data_title = Aidata.objects.filter(title=project)

    try:
        latest_data = data_title.latest('createdate')
        title_data = latest_data.title
        data_text = latest_data.content_text
    except Aidata.DoesNotExist:
        title_data = None
        data_text = None

    # 排名 本来考虑下拉列表，现在直接平铺

    Aisort_ = Aisort.objects.filter(title=project)
    testList = Aisort_.values_list("test_type")
    totalList = [list(set(testList))[i][0] for i in range(len(list(set(testList))))]
    totalList= sorted(totalList, key=lambda L: (L.lower(), L))

    if len(totalList) == 0:
        totalList = None
        data_list = None
        grid = None

    else:
        data_list = {}
        grid = Page()

        for test_A in totalList:
            my_data = Aisort.objects.filter(test_type=test_A)
            my_data_ = my_data.order_by("-score")
            my_data_1 = my_data.order_by("createdate")

  

            temp_list = []
            score_list = []
            date_list = []
            plot_data = {}

            for i, score_,model_,time_, plot_score_ in zip(range(len(list(my_data_.values("score")))),list(my_data_.values("score")),list(my_data_.values("model_name")),list(my_data_.values("createdate")),list(my_data_1.values("score"))):
                
                temp_list.append({"sort":i+1,"score":score_['score'],"model":model_['model_name'],"time":time_['createdate']})

                score_list.append(plot_score_['score'])
               

            temp_len = len(score_list)

    
            data_list[test_A] = temp_list
            plot_data[test_A] = score_list

            line_plot_ = get_line(range(temp_len),plot_data,project)
            # line_plot = line_plot_.render_embed()
            grid.add(line_plot_)

    if grid is not None:
        grid = grid.render_embed()



    # 效果展示
    demo_title = Aidemo.objects.filter(title=project)

    try:
        latest_demo = demo_title.latest('createdate')
        title_demo = latest_demo.title
        detial_demo = latest_demo.detail
    except Aidemo.DoesNotExist:
        title_demo = None
        detial_demo = None


    return render(request,'detial.html',
        {"project":project, "title_detial":title_detial, "detial_detail":detial_detail,
        "title_data":title_data,"data_text":data_text,
        "title_demo":title_demo,"detial_demo":detial_demo,
        "testList":totalList,"sortdata":data_list,
        'line_plot':grid,})