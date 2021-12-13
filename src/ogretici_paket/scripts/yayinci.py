#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:06:17 2021

@author: emirhan
"""

import rospy
from ogretici_paket.msg import BataryaDurum

def mesajYayinla():
    rospy.init_node("yayinci_dugumu",anonymous = True)
    pub = rospy.Publisher("batarya_konusu",BataryaDurum,queue_size = 10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        durum = "%25"
        rospy.loginfo(durum)
        pub.publish(durum)
        rate.sleep()
mesajYayinla()
