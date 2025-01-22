import os
from django.http import FileResponse, Http404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GeneratedFile
from .serializers import GeneratedFileSerializer
from .app.hyper3d import hyper3d_process_image_to_3d, load_config
from .app.tripo3d import tripo3d_process_image_to_3d
from .app.meshy import meshy_process_image_to_3d


class GeneratedFileGenerateHyper3DView(APIView):
    def post(self, request, format=None):
        serializer = GeneratedFileSerializer(data=request.data)
        if serializer.is_valid():
            image_url = serializer.validated_data['original_image']

            # 加载配置文件
            config = load_config()
            api_key_hyper3d = config['app']['hyper3d']['key']

            # 调用API生成GLB文件
            glb_file1_path = hyper3d_process_image_to_3d(image_url, api_key_hyper3d)

            return Response({'glb': glb_file1_path}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeneratedFileGenerateTripo3DView(APIView):
    def post(self, request, format=None):
        serializer = GeneratedFileSerializer(data=request.data)
        if serializer.is_valid():
            image_url = serializer.validated_data['original_image']

            # 加载配置文件
            config = load_config()
            api_key_tripod3d = config['app']['tripo3d']['key']

            # 调用API生成GLB文件
            glb_file2_path = tripo3d_process_image_to_3d(image_url, api_key_tripod3d)

            return Response({'glb': glb_file2_path}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeneratedFileGenerateMeshyView(APIView):
    def post(self, request, format=None):
        serializer = GeneratedFileSerializer(data=request.data)
        if serializer.is_valid():
            image_url = serializer.validated_data['original_image']

            # 加载配置文件
            config = load_config()
            api_key_meshy = config['app']['meshy']['key']

            # 调用API生成GLB文件
            glb_file3_path = meshy_process_image_to_3d(image_url, api_key_meshy)

            return Response({'glb': glb_file3_path}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeneratedFileUpdateView(APIView):
    def post(self, request, format=None):
        serializer = GeneratedFileSerializer(data=request.data)
        if serializer.is_valid():
            # created_at = serializer.validated_data['created_at']
            original_image = serializer.validated_data['original_image']
            glb_file1 = serializer.validated_data.get('glb_file1')
            glb_file2 = serializer.validated_data.get('glb_file2')
            glb_file3 = serializer.validated_data.get('glb_file3')

            # 创建新的记录
            generated_file = GeneratedFile(
                original_image=original_image,
                glb_file1=glb_file1,
                glb_file2=glb_file2,
                glb_file3=glb_file3
            )
            generated_file.save()
            return Response({'msg': 'ok'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeneratedFileListView(APIView):
    def get(self, request, format=None):
        # 获取所有 GeneratedFile 对象
        generated_files = GeneratedFile.objects.all()
        # 使用序列化器序列化数据
        serializer = GeneratedFileSerializer(generated_files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GeneratedFileDownloadView(APIView):
    def get(self, request, file_path, format=None):
        try:
            file_path = os.path.join('downloads', file_path)
            return FileResponse(open(file_path, 'rb'), as_attachment=True)
        except FileNotFoundError:
            raise Http404("File not found")
