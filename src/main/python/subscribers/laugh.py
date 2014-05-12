'''
Created on 11 May 2014

@author: Don Najd
@description: Nao will simply laugh
'''
from datetime import datetime, timedelta
import random

class Laugh(object):

    def __init__(self, nao, log):

        self.nao = nao 
        self.log = log


    # CALLBACKS
    def callback(self, dataName, value, message):
        self.log('laugh.py callback')
        self.nao.say('ha ha')


    def setup(self):
        self.log('laugh.py setup')
            

    def teardown(self):
        self.log('laugh.py teardown')
        