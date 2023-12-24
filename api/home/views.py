from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSeriazlizer
from .models import Todo

# Create your views here.

@api_view(['GET','POST','PACTH'])
def home(request):
    if request.method=='GET':

        return Response({
            'status' : 200,
            'message' : "Yes ! Django is freameworks is working!!!",
            'method_called' : "You called GET method"
        })
    
    elif request.method =='POST':
        return Response({
            'status' : 200,
            'message' : "Yes ! Django is freameworks is working!!!",
            'method_called' : "You called POST method"
            
        })
    elif request.method =='PATCH':
        return Response({
            'status' : 200,
            'message' : "Yes ! Django is freameworks is working!!!",
            'method_called' : "You called PATCH method"
            
        })


    else:
        return Response({
            'status' : 400,
            'message' : "Yes ! Django is freameworks is working!!!",
            'method_called' : "You called invalid method"
        })
    
  
@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    seriazlizer = TodoSeriazlizer(todo_objs,many=True)
    return Response({
        'status' : True,
        'message' : 'Todo fetched',
        'data' : seriazlizer.data
    })


    
@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSeriazlizer(data = data)
        if serializer.is_valid():
            serializer.save()
    
            return Response({
                'status' : True,
                'message' : 'success data', 
                'data' : serializer.data

            })
        


        return Response({
            'status' : False,
            'message' : 'invalid data',
            'data' : serializer.errors

        })
        
    except Exception as e:
        print(e)
        return Response({
            'status' : False,
            'message' : 'something went wrong'

        })