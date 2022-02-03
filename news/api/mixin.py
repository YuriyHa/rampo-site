
# likes/api/mixins.py
from rest_framework.decorators import action
from rest_framework.response import Response
from .. import servises
from .serializers import FanSerializer, CommentSerializer
class PostMixin:
    @action(detail=False,methods=['POST'])
    def post(self, request): 
        # print('title: ' + str(request.data['title']))
        # print('text: ' + str(request.data['text']))
        try:
            data=request.data
            servises.post(user=request.user, data=data)
            return Response()
        except Exception as error:
            return Response(status=500)
        
    @action(detail=True,methods=['POST']) 
    def deletepost(self,request,pk=None): 
        try:
            obj=self.get_object() 
            if servises.deleteModel(user=request.user, obj=obj): 
                return Response() 
            else: 
                return Response(status=500)
        except Exception as error:
            return Response(status=500)

    @action(detail=True,methods=['POST']) 
    def editpost(self,request,pk=None): 
        try:
            obj=self.get_object() 
            if servises.editpost(user=request.user,obj=obj, data=request.data): 
                return Response()
            else: 
                return Response(status=500)
        except Exception as e:
            return Response(status=500)

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        """Лайкает `obj`.
        """
        obj = self.get_object()
        servises.add_like(obj, request.user)
        return Response()

    @action(detail=True,methods=['POST'])
    def unlike(self, request, pk=None):
        """Удаляет лайк с `obj`.
        """
        obj = self.get_object()
        servises.remove_like(obj, request.user)
        return Response()
    @action(detail=True,methods=['GET'])
    def fans(self, request, pk=None):
        """Получает всех пользователей, которые лайкнули `obj`.
        """
        obj = self.get_object()
        fans = servises.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST']) 
    def comment(self,request,pk=None): 
        try:
            servises.comment(user=request.user,obj=self.get_object(),data=request.data)
            return Response()
        except Exception as e:
            return Response(status=500)

    @action(detail=True,methods=['GET'])
    def commentlist(self, request, pk=None):
        """Возвращает все комментарии  ктвиту"""
        obj=self.get_object()
        comment=servises.get_comments(obj, request.user)
        serializer=CommentSerializer(comment, many=True)
        return Response(serializer.data)


class CommentMixin: 
    @action(detail=True,methods=['POST'])
    def editcomment(self, request, pk=None): 
        try:
            obj=self.get_object() 
            if servises.editcomment(user=request.user,obj=obj, data=request.data): 
                return Response()
            else: 
                return Response(status=500)
        except Exception as e:
            return Response(status=500)

    @action(detail=False,methods=['POST'])
    def deletecomment(self,request,pk=None): 
        try:
            obj=self.get_object()
            if servises.deleteModel(user=request.user, obj=obj): 
                return Response()
            else: 
                return Response(status=500)
        except Exception as e:
            return Response(status=500)