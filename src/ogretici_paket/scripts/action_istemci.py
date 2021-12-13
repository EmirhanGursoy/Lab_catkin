#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 22:25:23 2021

@author: emirhan
"""

import rospy
import actionlib
from ogretici_paket.msg import GorevDurumAction, GorevDurumGoal

def bildirimFonksiyonu(bilgi):
    print("Gorev tamamlanma durumu: ", bilgi.oran)

def istekteBulun():
    rospy.init_node("action_istemci_dugumu")
    istemci = actionlib.SimpleActionClient("gorev", GorevDurumAction)
    istemci.wait_for_server()
    istek = GorevDurumGoal()
    istek.birim = 5
    istemci.send_goal(istek,feedback_cb = bildirimFonksiyonu)
    istemci.wait_for_result()
    x = istemci.get_result().sonuc
    return x

cikti = istekteBulun()
print("Gorevin son durumu: ",cikti)