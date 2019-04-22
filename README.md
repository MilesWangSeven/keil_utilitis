# keil_utilitis
keil utilitis

## KEIL 自动生成发布版本档案
'''
user run  after build:
1.  $KARM\ARMCC\bin\fromelf.exe !L --bin --output "$L@L.bin"
2.  AdvancedRelease.exe $L @L.hex @L.bin
'''
'''
把exe文件放到和项目文件同一级目录
如果exe报病毒，可将exe替换为py 第2点AdvancedRelease.exe 改为 python AdvancedRelease.py
'''