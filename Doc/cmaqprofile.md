# 简介

将由`prepmodel`输出的面源清单进行垂直分配。

# 运行说明

1. 配置`par.ini`。

-------------------

```ini
[parameters]
emission:I:\zhn-emission\MEIC2017_3km_v1\*_PP.nc
metcro3d:I:\zhn-emission\METCRO3D_3km.nc
output_dir:I:\zhn-emission\MEIC2017_3km_v1
vertical_factor:0,0.2,0.3,0.4,0.1
```

-----------------------------

**emission**: 由`prepmodel`输出的排放清单路径，支持批量处理。`*`为通配符。

**metcro3d**: 任意METCRO3D文件。

**output_dir**: 输出目录。

**vertical_factor**: 垂直分配因子。由最底层开始。

举例：

```python
# 当`vertical_factor: 0,0.2,0.3,0.4,0.1`时，
第一层数值 = 0.0 * values
第二层数值 = 0.2 * values
第三层数值 = 0.3 * values
第四层数值 = 0.4 * values
第五层数值 = 0.1 * values
其余层数值 = 0.0 * values
```

2. 运行`cmaqprofile.exe`。

```shell
./cmaqprofile.exe
```

