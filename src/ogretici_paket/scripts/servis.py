#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:03:24 2021

@author: emirhan
"""

import rospy
from ogretici_paket.srv import GecenZaman

def gecenZamanFonksiyonu(istek):
    robot_hiz = 0.5
    sure = istek.hedef_konum / robot_hiz
    return sure

def cevapGonder():
    rospy.init_node("server_dugumu")
    rospy.Service("zaman",GecenZaman,gecenZamanFonksiyonu)
    rospy.spin()
    
cevapGonder()