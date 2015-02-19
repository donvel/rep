# -*- coding: UTF-8 -*-

from django.utils import timezone
from django.db import models

def _current_date():
    return timezone.now().date()

class CommunionDay(models.Model):
    name = models.CharField(max_length=200, verbose_name="nazwa",
            help_text="krótsza niż temat :-}")
    topic = models.CharField(max_length=500, verbose_name="temat")
    date = models.DateField(default=_current_date, verbose_name="data")
    handout = models.FileField(verbose_name="konspekt", upload_to="konspekty",
            null=True, blank=True) # można wymyślić coś lepszego :P

    class Meta:
        verbose_name = "Dzień Wspólnoty"
        verbose_name_plural = "Dni Wspólnoty"

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.date)

class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name="nazwa")

    class Meta:
        verbose_name = "Filia"
        verbose_name_plural = "Filie"
    
    def __unicode__(self):
        return self.name

class Diocese(models.Model):
    name = models.CharField(max_length=100, verbose_name="nazwa")
    branch = models.ForeignKey('Branch')

    class Meta:
        verbose_name = "Diecezja"
        verbose_name_plural = "Diecezje"
    
    def __unicode__(self):
        return self.name


class Report(models.Model):
    branch = models.ForeignKey('Branch')
    communion_day = models.ForeignKey('CommunionDay')
    
    class Meta:
        verbose_name = "Sprawozdanie filialne"
        verbose_name_plural = "Sprawozdania filialne"
    
    def __unicode__(self):
        return '%s - %s' % (self.communion_day, self.branch)
