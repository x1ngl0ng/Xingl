from django.urls import path
from .views import (
    GeneratedFileGenerateHyper3DView,
    GeneratedFileGenerateTripo3DView,
    GeneratedFileGenerateMeshyView,
    GeneratedFileUpdateView,
    GeneratedFileDownloadView,
    GeneratedFileListView
)

urlpatterns = [
    path('generated-files/generate/hyper3d/', GeneratedFileGenerateHyper3DView.as_view(),
         name='generated-file-generate-hyper3d'),
    path('generated-files/generate/tripo3d/', GeneratedFileGenerateTripo3DView.as_view(),
         name='generated-file-generate-tripo3d'),
    path('generated-files/generate/meshy/', GeneratedFileGenerateMeshyView.as_view(),
         name='generated-file-generate-meshy'),
    path('generated-files/update/', GeneratedFileUpdateView.as_view(), name='generated-file-update'),
    path('generated-files/downloads/<path:file_path>/', GeneratedFileDownloadView.as_view(),
         name='generated-file-download'),
    path('list/', GeneratedFileListView.as_view(), name='list-generated-files'),  # 新添加的路由

]
