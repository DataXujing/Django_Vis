from django.shortcuts import render

from .models import Aiscore

# Create your views here.


def index(request):

    # project_table

    project_table_query = Aiscore.objects.all() # 查询所有
 
    project_table_list = []
    for item_ in project_table_query:
        temp = {"title":item_.title,"partner":item_.partner,"des":item_.describe,"date":item_.createdate}
        project_table_list.append(temp)
        


    # return render(request, 'index.html',{'form':form_index,'state':'get','qr_pic':None})
    return render(request, 'index.html',{"project_table":project_table_list})

