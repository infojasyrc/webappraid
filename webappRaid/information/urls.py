'''
Created on Aug 20, 2013

@author: Jose Antonio Sal y Rosas Celi
@contact: jose.salyrosas@jro.igp.gob.pe
'''

from django.conf.urls import patterns, url

urlpatterns = patterns('information.views',
    url(r'^$', 'index', name="index"),
)