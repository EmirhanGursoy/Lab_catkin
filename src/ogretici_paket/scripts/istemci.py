#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:03:25 2021

@author: emirhan
"""

import rospy
from ogretici_paket.srv import GecenZaman

def istekteBulun(x):
    rospy.wait_for_service("zaman")
    try:
        servis = rospy.ServiceProxy("zaman", GecenZaman)
        cevap = servis(x)
        return cevap.gecen_sure
    except rospy.ServiceExcepion:
        print("Servisle alakalı hata !!!")

hedef = float(input("Hedef konum giriniz: "))
t = istekteBulun(hedef)
print("Hedefe varana kadar gecen sure: ",t)