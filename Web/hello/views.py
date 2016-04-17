from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from hello.models import Task,WaterParticle,UserDevice
from hello.serializers import TaskSerializer,WaterParticleSerializer
from django.template import RequestContext
from django.contrib.auth.models import User



def login(request):
    if request.user.is_authenticated():
        queryset = WaterParticle.objects.filter(user  = request.user).order_by('dateTime')
        return render_to_response('loggedin.html', {'water_data':queryset,'current_user':request.user})
    else:
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html',c)
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password=password)
    if user is not None: 
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loading_main_page/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')


def loading_main_page(request):
    return render_to_response('loading_main_page.html')
def loading_login_page(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)


@login_required(login_url='/accounts/login/')
def loggedin(request):
    if request.user.is_authenticated():
        queryset = WaterParticle.objects.filter(user  = request.user).order_by('dateTime')
        return render_to_response('loggedin.html', {'water_data':queryset,'current_user':request.user})
    else:
        return HttpResponseRedirect('/accounts/login/')


def invalid_login(request):
    return HttpResponseRedirect('/accounts/logout/')
def logout(request):
    auth.logout(request)
    return render_to_response('loading_login_page.html')
def register_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        deviceID = request.POST.get('device_id')
        user, created = User.objects.get_or_create(username=user_name,email=email)
        user.set_password(password)
        user.save() 
        user_device = UserDevice(user = user_name,deviceID = deviceID)
        user_device.save()       
        return HttpResponseRedirect('/accounts/register_success/')
    
    queryset = UserDevice.objects.all()
    args = {'all_user':queryset}
    args.update(csrf(request))
    return render_to_response('register.html', args)


def register_success(request):
    queryset = WaterParticle.objects.filter(user  = request.user).order_by('dateTime')
    return render_to_response('loggedin.html', {'water_data':queryset,'current_user':request.user})

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def task_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def water_list(request):
    """
    List all waterParticleData, or create a new task.
    """
    if request.method == 'GET':
        waters = WaterParticle.objects.filter(user = request.user)
        serializer = WaterParticleSerializer(waters, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WaterParticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def task_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def water_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        water = WaterParticle.objects.get(pk=pk)
    except WaterParticle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WaterParticleSerializer(water)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WaterParticleSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        water.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



