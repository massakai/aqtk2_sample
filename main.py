# -*- coding: utf-8 -*-
from pyaqtk.native.aqtk2 import synthe_utf8, free_wave
from ctypes import *
import wave

koe = "ハローワールド".encode('utf-8')
i_speed = 100
size = c_int(0)
phont_data = 0

wav = synthe_utf8(koe, i_speed, pointer(size), phont_data)
if wav:
    with open('hello_world2.wav', 'wb') as wav_file:
        data = bytes(wav[:size.value])
        wav_file.write(data)
    free_wave(wav)
else:
    print("synthe failed, error code =", size)
