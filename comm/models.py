# -*- coding: UTF-8 -*-

from tinymce.models import HTMLField
from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def _current_date():
    return timezone.now().date()


class CommunionDay(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"nazwa",
            help_text="krótsza niż temat :-}")
    topic = models.TextField(verbose_name=u"temat")
    date = models.DateField(default=_current_date, verbose_name=u"data")
    handout = models.FileField(verbose_name=u"konspekt", upload_to="konspekty",
            null=True, blank=True) # można wymyślić coś lepszego :P

    class Meta:
        verbose_name = "Dzień Wspólnoty"
        verbose_name_plural = "Dni Wspólnoty"

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.date)


class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"nazwa")

    class Meta:
        verbose_name = "filia"
        verbose_name_plural = "filie"
    
    def __unicode__(self):
        return self.name


class Diocese(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"nazwa",
            help_text='np. "radomska"')
    branch = models.ForeignKey('Branch', verbose_name=u"filia")
    arch = models.BooleanField(default=False, verbose_name=u"archi")

    class Meta:
        verbose_name = u"diecezja"
        verbose_name_plural = u"diecezje"
    
    def __unicode__(self):
        prefix = 'Archidiecezja' if self.arch else 'Diecezja'
        return '%s %s' % (prefix, self.name)


class Report(models.Model):
    branch = models.ForeignKey('Branch', verbose_name=u"filia")
    communion_day = models.ForeignKey('CommunionDay',
            verbose_name=u"Dzień Wspólnoty")
    file_report = models.FileField(verbose_name="dokument sprawozdania",
            help_text=u"tradycyjne sprawozdanie (np. .doc lub .pdf)",
            upload_to="sprawozdania", null=True, blank=True)
    
    class Meta:
        verbose_name = u"sprawozdanie filialne"
        verbose_name_plural = u"sprawozdania filialne"
        unique_together = (("branch", "communion_day"),)
    
    def __unicode__(self):
        return u'%s - %s' % (self.communion_day, self.branch)
    

class CustomTextConfig(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"nazwa")
    obligatory = models.BooleanField(default=False,
            verbose_name=u"obowiązkowy",
            help_text=u"Punkty obowiązkowe pojawią się w każdym sprawozdaniu.")
    use_in_report = models.BooleanField(default=False,
            verbose_name=u"w raporcie zbiorczym",
            help_text=u"Czy uwzględnić w zbiorczym raporcie z DWDD.")

    class Meta:
        verbose_name = u"typ pola"
        verbose_name_plural = u"typy pól"
    
    def __unicode__(self):
        return self.name


class CustomText(models.Model):
    report = models.ForeignKey('Report', verbose_name=u"sprawozdanie")
    config = models.ForeignKey('CustomTextConfig', verbose_name=u"typ")
    content = HTMLField(null=True, blank=True, verbose_name=u"treść")
    
    class Meta:
        verbose_name = u"pole tekstowe"
        verbose_name_plural = u"pola tekstowe"
    
    def __unicode__(self):
        return str(self.config)


SERVICE_SHORT_NAME_MLEN = 10

class Service(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=u"pełna nazwa")
    short_name = models.CharField(max_length=SERVICE_SHORT_NAME_MLEN,
            verbose_name=u"krótka nazwa", #unique=True,
            help_text="max %s znaków, np. MDDK" % SERVICE_SHORT_NAME_MLEN)
    display_prioirity = models.IntegerField(default=0,
            verbose_name=u"priorytet w tabelce",
            help_text=u"posługi w tabelce obecności są uporządkowane według " +
                u"malejącego priorytetu")
    
    class Meta:
        verbose_name = u"posługa"
        verbose_name_plural = u"posługi"
        ordering = ['-display_prioirity']
    
    def __unicode__(self):
        return '%s (%s)' % (self.full_name, self.short_name)


class Attendance(models.Model):

    report = models.ForeignKey('Report', verbose_name=u"sprawozdanie")
    diocese = models.ForeignKey('Diocese', verbose_name=u"diecezja")
    service = models.ForeignKey('Service', verbose_name=u"posługa")
    number = models.IntegerField(default=0,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(10000),
            ],
            verbose_name=u"liczba")

    class Meta:
        verbose_name = u"obecność"
        verbose_name_plural = u"obecności"
        unique_together = (("report", "diocese", "service"),)
