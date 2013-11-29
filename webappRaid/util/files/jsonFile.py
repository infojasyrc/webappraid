'''
Created on Aug 8, 2013

@author: Jose Antonio Sal y Rosas Celi
@contact: jose.salyrosas@jro.igp.gob.pe
'''

import json

class JsonFile(object):
    
    def __init__(self):
        pass
    
    def save(self, pathFile, ListPython):
        contentFile = json.dumps(ListPython)
        
        fileJson = open(pathFile, 'w')
        fileJson.write(contentFile)
        fileJson.close()
