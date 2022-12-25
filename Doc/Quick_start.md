# Manual Description

This tutorial illustrates  an integrated workflow for  WRF-AQM (CMAQ or CAMx) base on ISAT. As the capital of China, Beijing has a large population and many vehicles, making it a hot spot for air pollution research in China. This tutorial configured a triple-nested domains for mainland China, Beijing-Tianjin-Hebei(BTH) and Beijing with spatial resolution of 27, 9 and 3 km, respectively (see Figure).

<img src="fig/快速启动-模拟域示意图.png" alt="快速启动-模拟域示意图" style="zoom:50%;" />

# Tool Description

* **prepgrid**

Configuring nested domain parameters based on shapefile in research domain.

Generating parameters in `namelist.wps` and `namelist.input` in WRF model.

* **downscale**

Downscaling gridded emission inventories into defined domain based on spatial allocators (roads, population, etc.).

* **mapinv**

Allocating region-based emission inventory into defined domain.

* **prepmodel**

Generating inline model-ready emission inventory for AQM.

# Start

System: Windows 10 or Linux

## Step 1: Configuration of nested domains

This section is based on `prepgrid` module.

Go to "/ISAT_V2/prepgrid/" and configure the `par.ini` file below.

```ini
[projection]
# lat in lcc project
lat1:33.0       
lat2:42.0
[domain]
#number of domian
casename:3nestdomain
numdom:3
#shpfile in ecah domain
shpath: ./shp/mainlandchina.shp,./shp/JJJ.shp,./shp/beijing.shp
# grid space in ecah domian
dx:27000,9000,3000
# add grid in each domian,
#xl:left in x direction;xr:right in xdirection;yd:down;yt:top 
# attention the added grid different directoin muse be equal,eg xladd=xradd
#in other domian added grid must be  a multiple of dx_parent/dx_son
xladd:2,3,3
xradd:2,3,3
ytadd:2,3,3
ydadd:2,3,3
domname:china,JJJ,beijing
model_clip:1,1,1
```

After configuring the `par.ini` file, enter the following command in the terminal to run the program.

```shell
python prepgrid.py
```

If a print message similar to the following is displayed on the screen, the program has run successfully.

```
Prepgrid tool for allocating regional emissions, created  by Kun Wang from IUSE Beijing in 2022.
LCC projection:  mid lon:102.07366854247363,mid lat:36.68731137325006
processing Domain ID:0
getting gridding parameters for Domain:0
creating fishnet for WRF of WRF:0
creating fishnet for AQM of AQM:0
clip x or y direction by 1 grid
processing Domain ID:1
getting gridding parameters for Domain:1
modifying gridnum
no modify gridnum
creating fishnet for WRF of Domain:1
creating fishnet for AQM of Domain:1
clip x or y direction by 1 grid
processing Domain ID:2
getting gridding parameters for Domain:2
no modify gridnum
modifying gridnum
creating fishnet for WRF of Domain:2
creating fishnet for AQM of Domain:2
clip x or y direction by 1 grid
finish
```

The second line of the printed information here: `LCC projection: mid lon:102.07366854247363,mid lat:36.68731137325006` are **central longitude** and **central latitude** for LCC projection respectively.

In addition, you can see the output files in the `output` directory.

```
├── 3nestdomain_gridinfo.csv
├── aqmJJJ.csv ---- CMAQ grid information of D02, will be used in mapinv.
├── aqm_JJJ.shp
├── aqm_beijing.shp
├── aqm_china.shp 
├── aqmbeijing.csv ---- CMAQ grid information of D03, will be used in mapinv.
├── aqmchina.csv ---- CMAQ grid information of D01, will be used in mapinv.
├── wrf_JJJ.csv
├── wrf_JJJ.shp
├── wrf_beijing.csv
├── wrf_beijing.shp
├── wrf_china.csv
├── wrf_china.shp
```

The `aqm*.csv` files and the `wrf_*.csv` files are grid information for AQM and WRF model respectively. `aqm*.csv` can be used in the `mapinv` and `downscale`module, and `*_gridinfo.csv` can adopted in `namelist.wps` and `namelist.input` in WRF model.

<img src="fig/gridinfo文件映射.png" alt="gridinfo文件映射" style="zoom:100%;" />

The visualization of the output can be display directly through the `*.shp` files.

<img src="fig/网格示意图.png" alt="网格示意图" style="zoom:80%;" />

## Step 2: Downscaled Regional Gridded Emissions Inventory

This section is based on `downscale` module.

Go to "/ISAT_V2/downscale" and configure the `par.ini` file.

```ini
[preinv]
invf:./input/domain/aqmJJJ.csv
dx:9000
ratio:3
casename:3km3
[allocate]
emissions:./regioninv/agricultureannual.csv,./regioninv/transportationannual.csv,./regioninv/residentialannual.csv
method:area,road,pop
```

parameter description of `par.ini`:

-------------------------

**invf**: Grid of target domain. **Grid information file preprocessed by `prepgrid.exe`. **

**dx**: Grid resolution.

**ratio**: Sub-grid ratio (3 is recommended above 3km, 1 is recommended ≤ 3km).

**casename**: Case name.

**emission**: Regional inventory file.

**method**：Allocation Method. **Optional `[area, road, pop]` are area allocation, road allocation, and population allocation, respectively.**

---------------------

After configuring the `par.ini` file, enter the following command in the terminal.

```shell
python downscale.py
```

If no error is reported, the program runs successfully.

---------------------------

**The following is a list of errors that may occur during this process:**

1. `FileNotFoundError: [Errno 2] No such file or directory: b'./input/Temp/tempMEIC.nc'`

Solution: Rename the existing nc format file of any MEIC list to `tempMEIC.nc` and move it to `. /input/Temp` directory.

2. `OSError: Cannot save file into a non-existent directory: 'output\sa'`

Solution: Create the `sa\` directory manually in the `output\` directory.

--------------------

The figure shows the result of list allocation under different `ratio`.

<img src="fig/不同ratio下的降尺度结果.png" alt="不同ratio下的降尺度结果" style="zoom:67%;" />

## Step 3: Generate model ready emission inventory for AQM

This section is based on `prepmodel`.

Go to "/ISAT/prepmodel" and configure the `par.ini` file.

```ini
#
#   Prepmodel
#
[runtime]
runtime:193
[gridcro2d]
gridcro2d: ./src/met/GRIDCRO2D_9km
[speciate]
speciate: ./src/speciate/speciate_AR.csv,./src/speciate/speciate_AG.csv,./src/speciate/speciate_TR.csv
speciate_groups:./src/speciate/speciate_PP.csv,./src/speciate/speciate_IN.csv
[temporary]
#energy,point,area,mobile,flat
temporary_hour : ./src/temporary/hourly.csv
temporary_week : ./src/temporary/weekly.csv
temporary_month: ./src/temporary/monthly.csv
[emissions]
emissions: ./src/emissions/MEIC/AR.csv,./src/emissions/MEIC/AG.csv,./src/emissions/MEIC/TR.csv
stack_groups: ./src/emissions/CASE/STACK_GROUP_PP.csv,./src/emissions/CASE/STACK_GROUP_IN.csv
```

parameter description of `par.ini`:

---------------------

**runtime**: Runtime of AQM. (unit: hour)

**gridcro2d**：The path of GRIDCRO2D file created by MCIP.

**speciate**: The path of speciaten profile files.

**temporary_***: The path of temporal profile files.

**emissions**: The path of gridded emission inventory from **Step. 2 **(defined by emissions) and user-defined point emission inventory (definedy by stack_groups) . 

---------------------------------

After configuring the `par.ini` file, enter the following command in the terminal to start running.

```shell
python area_emis.py
python point_emis.py
python point_info.py
```

If no error is reported, the program runs successfully.
