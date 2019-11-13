# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

from django_mongodb_engine.contrib import MongoDBManager

# Create your models here.


class Student(Document):

	name = models.CharField(max_length = 100)
	class_name = models.CharField(max_length = 100)
	Address = models.CharField(max_length =100)

	objects = MongoDBManager()
	