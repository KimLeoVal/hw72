from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, \
    IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.models import Quote


from api_v1.serializers import QuoteSerializers



class QuoteView(APIView):
    serializer_class = QuoteSerializers
    permission_classes = [ DjangoModelPermissionsOrAnonReadOnly ]
    queryset=Quote.objects.none()
    def get(self, request, *args, **kwargs):
        quotes=self.get_queryset()
        serializer = QuoteSerializers(quotes, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = QuoteSerializers(data=request.data)
        if serializer.is_valid():
            quote = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if request.user.has_perm('api_v1.change_quote'):
            quote = get_object_or_404(Quote, pk=pk)
            serializer = QuoteSerializers(data=request.data, instance=quote)
            if serializer.is_valid():
                quote = serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=400)
    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if request.user.has_perm('api_v1.delete_quote'):
            quote=get_object_or_404(Quote,pk=pk)
            Quote.delete(quote)
            return Response(status=status.HTTP_204_NO_CONTENT)


    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs.get('pk')
        if user.has_perm('api_v1.add_quote'):
            quotes= Quote.objects.all()
        else:
            quotes= Quote.objects.filter(status=1)
        if pk:
            if user.has_perm('api_v1.add_quote'):
                quotes = Quote.objects.filter(pk=pk)
            else:
                quotes = Quote.objects.filter(pk=pk,status=1)
        return quotes


class ChangeRatingPlus(APIView):
    def post(self, request, *args, **kwargs):
        print(request.session.session_key)
        pk = self.kwargs.get('pk')
        quote = get_object_or_404(Quote, pk=pk)
        # if request.session.get('session') != request.session.session_key:
        print(request.session.session_key)
        quote.rate=quote.rate+1
        quote.save()
        # request.session['session']=request.session.session_key
        print(quote.rate)
        return Response({'rate': quote.rate})
        # else:
        #     print(request.session.session_key)
        #     return Response({'rate': quote.rate})


class ChangeRatingMinus(APIView):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        quote = get_object_or_404(Quote, pk=pk)
        print(request.session.get('session_key'))
        if request.session.get('session') != request.session:
            print(request.session.get('session_key'))
            quote.rate = quote.rate - 1
            quote.save()
            request.session['session'] = request.session.get('session_key')
            print(quote.rate)
            return Response({'rate': quote.rate})
        else:
            return Response({'rate': quote.rate})


@ensure_csrf_cookie

def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')