#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from pyaqtk.native.aqtk2 import synthe_utf8, free_wave
from ctypes import *
import wave
import sys


def load_phont_data(path):
    with open(path, 'rb') as f:
        return f.read()

argc = len(sys.argv)
if argc > 1:
    koe = sys.argv[1].encode('utf-8')
else:
    koe = "ハローワールド".encode('utf-8')

if argc > 2:
    phont_data = load_phont_data(sys.argv[2])
else:
    phont_data = None

i_speed = 100
size = c_int(0)
wav = synthe_utf8(koe, i_speed, pointer(size), phont_data)
if wav:
    with open('hello_world2.wav', 'wb') as wav_file:
        data = bytes(wav[:size.value])
        wav_file.write(data)
    free_wave(wav)
else:
    print("synthe failed, error code =", size)
