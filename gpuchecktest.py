# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:24:13 2021

@author: USER
"""
import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU')
print("Num GPUs:", len(physical_devices))
