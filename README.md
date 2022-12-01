# Inventory Spatial Allocate Tool 

ISAT(Inventory Spatial Allocate Tool，排放清单空间分配工具)是基于城市设施点、人口、道路、土地利用类型等地理信息数据将面源排放清单进行空间分配的工具，实现了如下三项主要功能。

1. 自动绘制WRF和AQM网格，确定`namelist.wps`参数。
2. 高效率的排放清单降尺度工具。
3. 自动构建可以直接输入CMAQ和CAMx的排放清单文件（面源and点源）。

具体流程如图所示：

<img src="Doc/fig/流程图.png" alt="流程图" style="zoom:67%;" />

## 更新日志

### 2022年12月1日更新：

1. 延长公开使用时间至2023年12月1日。
2. 增加[面源清单的inline垂直分配工具](cmaqprofile)。

## 使用手册

* [快速使用手册](./Doc/Quick_start.md)：以MEIC排放清单为例，简要介绍如何快速使用ISAT来设计模拟网格、清单分配以及构建可以直接输入CMAQ以及CAMx的排放清单文件。
* [物种分配文件修改]():
* [时间分配文件修改]():
* [自定义空间分配因子文件]():
* [面源清单的inline垂直分配工具使用方法](Doc/cmaqprofile.md):

...

## 关于我们

**By**：

***北京市科学技术研究院城市安全与环境科学研究所   王堃  （wkty@mail.bnu.edu.cn）***

**Team members**:

中国科学院东北地理与农业生态研究所 高超

中山大学大气科学学院 王浩帆

清华大学 刘开云

海南大学 刘姝涵

## 引用

**欢迎引用、讨论作者及所在团队相关论文**：

Kun Wang et al. Unit-based emissions and environmental impacts of industrial condensable particulate matter in China in 2020,Chemosphere ,2022.

Kun Wang et al., Identification of NOx hotspots from oversampled TROPOMI NO2 column based on image segmentatio n method, Science of the Total Environment, 2021, 803

Kun Wang et al., Measure -specific environmental benefits of air pollution control for coal-fired industrial boilers in China from 2015 to 2017, Environmental Pollution, 2021, 273 

Kun Wang et al., Pinpointing optimized air quality model performance over the Beijing-Tianjin-Hebei region: Mosaic approach, Atmospheric Pollution Research, 2021, 12 

Kun Wang et al., Impacts of LULC, FDDA, Topo-wind and UCM schemes on WRF-CMAQ over the Beijing-Tianjin-Hebei region, Atmospheric Pollution Research, 2021, 12: 292-304

Haofan Wang  et al. Impact of different urban canopy models on air quality simulation in Chengdu, southwestern China[J]. Atmospheric Environment, 2021, 267: 118775.

Kun Wang et al., A comprehensive emissioninventory of multiple air pollutants from iron and steel industry in China:Temporal trends and spatial variation characteristics , Science of the Total Environment, 2016.7.15, 559: 7~14 

Jiajia Gao; Kun Wang et al., Temporal-spatial characteristics and source apportionment of PM2.5 as we ll as its associated chemical species in the Beijing-Tianjin-Hebei region of China, Environmental Pollution, 2017, (233): 714-724 

 Jiajia Gao; Kun Wang et al., Refined spatio-temporal emission assessment of Hg, As, Cd, Cr and Pb from Chinese coal-fired industrial boilers. Science of The Total Environment, 2020, 20(11).

Tao Yue; Kun Wang* et al., Emission Characteristics of Hazardous Atmospheric Pollutants from Ultra-low Emission Coal-fired Industrial Boilers in China. Aerosol and Air Quality Research, 2020, 20(4).

Tao Yue;... ; Kun Wang*, Xiang Gao. Environmental Impacts of the Revised Emission Standard of Air Pollutants for Boilers in the Heating Season of Beijing, China. Aerosol & Air Quality Research, 2018.  

Kun Wang, et al. Vehicle emissions calculation for urban roads based on the Macroscopic Fundamental Diagram method and real-time traffic information. Atmospheric and Oceanic Science Letters, 2020, 13(2):1-8.

王堃,高超等. 基于CSGD的排放清单处理工具研究[J]. 环境科学研究, 2019, 32(6):9.

王堃, 高佳佳, 田贺忠,等. 基于POI兴趣点的排放清单空间分配方法[J]. 中国环境科学, 2017, 37(6):6.

王人洁, 王堃等. 中国国道和省道机动车尾气排放特征[J]. 环境科学, 2017, 38(9):8.
