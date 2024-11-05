from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Material, Seller

from .serializers import MaterialSerializer, SellerSerializer


class MaterialAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            mats = Material.objects.all()
            return Response({"post": MaterialSerializer(mats, many=True).data})

        try:
            mat = Material.objects.get(pk=pk)
            return Response({"post": MaterialSerializer(mat).data})
        except:
            return Response({"error": "Object don't exist"})

    def post(self, request):
        serializer = MaterialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'posts': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        print(pk)
        if not pk:
            return Response({"error": "Method PUT is not allowed"})

        try:
            instance = Material.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = MaterialSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"posts": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE is not allowed"})

        try:
            Material.objects.get(pk=pk).delete()
        except:
            return Response({"error": "Object does not exist"})

        return Response({"post": f"deleted post {pk}"})


class SellerAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            objects = Seller.objects.all()
            return Response({'posts': SellerSerializer(objects, many=True).data})

        try:
            ob = Seller.objects.get(pk=pk)
            return Response({"post": SellerSerializer(ob).data})
        except:
            return Response({"error": "Object does not exist"})

    def post(self, request):
        serializer = SellerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'posts': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT is not allowed"})

        try:
            instance = Seller.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = SellerSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"posts": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE is not allowed"})
        try:
            Seller.objects.get(pk=pk).delete()
        except:
            return Response({"error": "Object does not exist"})

        return Response({"post": f"deleted post {pk}"})
