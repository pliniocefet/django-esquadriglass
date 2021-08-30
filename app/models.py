# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class Teste(models.Model):
    
    STATUS =( 
        ('orcamento', 'Orçamento'),
        ('pedido', 'Pedido'),
    )

    obra = models.CharField(max_length=255)
    situacao = models.CharField(max_length=9, choices=STATUS,) 
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    valores = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.obra