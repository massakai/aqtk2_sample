# -*- coding: utf-8 -*-
u"""AquesTalk2 インタフェース"""

from ctypes import cdll, c_int, c_ubyte, c_char_p, c_void_p, POINTER
from ctypes.util import find_library

# FIXME: MacではFrameworkでライブラリが提供されているので、
#        ctypesでどのように読み込めば良いか調べる。
# Mac でも LD_LIBRARY_PATH でディレクトリを指定できるか確認する
lib_path = find_library('AquesTalk2')
if not lib_path:
    lib_path = find_library('AquesTalk2Eva')
if not lib_path:
    raise ImportError

aqtk2_lib = cdll.LoadLibrary(lib_path)

synthe = aqtk2_lib.AquesTalk2_Synthe
synthe_euc = aqtk2_lib.AquesTalk2_Synthe_Euc
synthe_utf8 = aqtk2_lib.AquesTalk2_Synthe_Utf8
synthe_utf16 = aqtk2_lib.AquesTalk2_Synthe_Utf16
synthe_roman = aqtk2_lib.AquesTalk2_Synthe_Roman
free_wave = aqtk2_lib.AquesTalk2_FreeWave

_synthe_funcs = (synthe, synthe_euc, synthe_utf8, synthe_utf16, synthe_roman)
for synthe_func in _synthe_funcs:
    # const char *koe
    # int iSpeed
    # int *size
    # void *phontDat
    synthe_func.argtypes = (c_char_p, c_int, POINTER(c_int), c_void_p)
    synthe_func.restype = POINTER(c_ubyte)

free_wave.argtypes = (POINTER(c_ubyte), )
free_wave.restype = None
