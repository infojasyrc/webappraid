'''
Created on Aug 19, 2013

@author: Jose Antonio Sal y Rosas Celi
@contact: jose.salyrosas@jro.igp.gob.pe
'''

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

import os
from util.files.jsonFile import JsonFile

def index(request):
    #finalpath = "/puma/storage"
    finalpath = "/gossip/storage"
    
    if "unit" in request.GET:
        units = str(request.GET["unit"]).lower()
    else:
        units = "gb"
        
    information = disk_usage(finalpath, units)
    
    if "out" in request.GET:
        if request.GET["out"] == "json":
            template = os.path.join("information","diskInfo.json")
            pathFile = os.path.join(settings.PROJECT_DIR, 'information', 'templates', template)
            
            objJson = JsonFile()
            objJson.save(pathFile, information)
        else:
            template = "information/index.html"
    else:
        template = "information/index.html"
    
    return render_to_response(template, {"total" : information["total"],
                                         "used" : information["used"],
                                         "free" : information["free"],
                                         }, 
                              context_instance=RequestContext(request))


def disk_usage(path, units="gb"):
    """Return disk usage statistics about the given path.

    Returned values is a named tuple with attributes 'total', 'used' and
    'free', which are the amount of total, used and free space, in bytes.
    """
    st = os.statvfs(path)
     
    #free = (st.f_bavail * st.f_frsize) (bytes)
    free_bytes = (st.f_bavail * st.f_frsize)
    
    #total = st.f_blocks * st.f_frsize (bytes)
    total_bytes = st.f_blocks * st.f_frsize
    
    #used = (st.f_blocks - st.f_bfree) * st.f_frsize (bytes)
    used_bytes = (st.f_blocks - st.f_bfree) * st.f_frsize
    
    free = getRealUnit(free_bytes)
    total = getRealUnit(total_bytes)
    used = getRealUnit(used_bytes)
    
    return {"total" : total, "used" : used, "free" : free}


def getRealUnit(amount):
    units = 1000
    maxUnit = 1000000000000
    
    i = 1
    while True:
        result = calculateUnit(amount, maxUnit)
        strUnit = getStrUnit(maxUnit)
        if result == 0:
            units = units ** i
            maxUnit = maxUnit / units
        else:
            strfinal = "%d %s" % (result, strUnit)
            break
    
    return strfinal


def calculateUnit(amount, unit):
    result = amount / unit
    return result


def getStrUnit(unit):
    if unit == 1000000000000:
        strUnit = "TB"
    elif unit == 1000000000:
        strUnit = "GB"
    elif unit == 1000000:
        strUnit = "MB"
    elif unit == 1000:
        strUnit = "KB"
    else:
        strUnit = "B"
    
    return strUnit
    