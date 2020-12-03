from django.shortcuts import render, render_to_response


def page_not_found(request,**kwargs):
    return render_to_response('404.html')

def server_error(request,**kwargs):
    return render_to_response('500.html')