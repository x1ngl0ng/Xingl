from django.db import models


class GeneratedFile(models.Model):
    original_image = models.URLField(max_length=500)  # 存储图像 URL
    glb_file1 = models.CharField(max_length=500, null=True)  # 存储 GLB 文件 URL
    glb_file2 = models.CharField(max_length=500, null=True)
    glb_file3 = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'GeneratedFile {self.id}'
