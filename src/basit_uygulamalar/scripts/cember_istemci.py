#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 19:11:04 2021

@author: emirhan
"""

import rospy
from basit_uygulamalar.srv import CemberHareket

rospy.wait_for_service("cember_servis")
try:
    yaricap = float(input("Yaricap giriniz: "))
    servis = rospy.ServiceProxy("cember_servis",CemberHareket)
    servis(yaricap)
except rospy.ServiceException:
    print("Servisle alakali hata meydana geldi !!!")