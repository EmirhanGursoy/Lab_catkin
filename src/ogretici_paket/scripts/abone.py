#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:09:52 2021

@author: emirhan
"""

import rospy
from ogretici_paket.msg import BataryaDurum

def bataryaFonksiyonu(mesaj):
    rospy.loginfo("Robot şarjı: %s"%mesaj.batarya)
    
def mesajDinle():
    rospy.init_node("abone_dugumu")
    rospy.Subscriber("batarya_konusu",BataryaDurum,bataryaFonksiyonu)
    rospy.spin()
    
mesajDinle()