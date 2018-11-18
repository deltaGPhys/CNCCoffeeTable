# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pattern(models.Model):
    Name = models.CharField(max_length=40)
    Blueprint = models.FileField(blank=True,null=True)
    Photo = models.FileField(blank=True,null=True)
    Gcode = models.FileField(blank=True,null=True)
    Duration = models.TimeField(blank=True,null=True)
    Description = models.TextField(blank=True,null=True)
    TypeChoices = (
    ('Background', 'Background'),
    ('Shape', 'Shape')
    )
    Type = models.CharField(max_length=30,default='Textual',choices=TypeChoices)

    def __unicode__(self):
        return u'%s (%d)' % (self.Name,self.pk)
    
    
