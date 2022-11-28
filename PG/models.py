from django.contrib.auth.models import User
from django.db import models


class ParametricGraph(models.Model):
    title = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Layer(models.Model):
    name = models.CharField(max_length=255)
    pg = models.ForeignKey('ParametricGraph', null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Node(models.Model):
    name_node = models.CharField(max_length=255)
    parametr = models.CharField(max_length=255, default='1')
    normParametr = models.CharField(max_length=255, default='1')
    kolSolution = models.CharField(max_length=255, default='0')
    kolSolutionNorm = models.CharField(max_length=255, default='1')
    layer = models.ForeignKey('Layer', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_node
