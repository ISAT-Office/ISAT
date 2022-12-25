# Manual Description

As the capital of China, Beijing has a large population and many vehicles, making it a hot spot for air pollution research in China. This turorial use a triple-nested domains for mainland China, Beijing-Tianjin-Hebei(BTH) and Beijing with spatial resolution of 27, 9 and 3 km, respectively (see Figure).

<img src="fig/快速启动-模拟域示意图.png" alt="快速启动-模拟域示意图" style="zoom:50%;" />

This tutorial will finish a complete workflow of WRF-AQM (CMAQ or CAMx) base on ISAT.

# Tool Description

* **prepgrid**

Design the simulation nested domain and draw the simulation grid according to the shapefile file, and output the parameters in `namelist.wps` and `namelist.input` in WRF.

* **downscale**

Downscale coarse resolution emission inventories based on a database of emission factors (roads, population, etc.).

* **mapinv**

Map the downscaled emission inventory is to the simulation grid and this part of the output file can be provided to prepmodel.

* **prepmodel**

The process of converting *csv* files into emission inventory files that can be directly imported into the CMAQ model.

# Start

System: Windows 10 or Linux

## Step 1: Draw simulation nested domains

This section is based on `prepgrid`.

Go to the directory where the `prepgrid.exe` executable is located, and then configure the `par.ini` file.

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
./prepgrid.exe
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

The second line of the printed information here: `LCC projection: mid lon:102.07366854247363,mid lat:36.68731137325006` are **central longitude** and **central latitude** respectively.

In addition, you can see the series output files in the `output` directory.

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

The `aqm*.csv` files and the `wrf_*.csv` files are both detailed grid information, where `aqm*.csv` will be used in the `mapinv` program, and `*_gridinfo.csv` is the parameters in `namelist.wps`, and the specific mapping relationship is shown in the figure.

<img src="fig/gridinfo文件映射.png" alt="gridinfo文件映射" style="zoom:100%;" />

The visualization of the output can be done directly through the `*.shp` files.

<img src="fig/网格示意图.png" alt="网格示意图" style="zoom:80%;" />

## Step 2: Downscaled Emissions Inventory

This section is based on `downscale`.

Go to the directory where the `downscale.exe` executable is located, and then configure the `par.ini` file.

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

**invf**: Grid information. **Grid information file exported by `prepgrid.exe`. **

**dx**: Grid resolution.

**ratio**: Sub-grid ratio (3 is recommended above 3km, 1 is recommended below).

**casename**: Case name.

**emission**: Regional inventory file.

**method**：Allocation Method. **Optional `[area, road, pop]` are area allocation, road allocation, and population allocation, respectively.**

---------------------

After configuring the `par.ini` file, enter the following command in the terminal to start running.

```shell
./downscale.exe
```

If no error is reported, the program runs successfully.

---------------------------

**The following is a list of errors that may occur during this process:**

1. `FileNotFoundError: [Errno 2] No such file or directory: b'./input/Temp/tempMEIC.nc'`

Solution: Rename the existing nc format file of any MEIC list to `tempMEIC.nc` and move it to `. /input/Temp` directory.

2. `OSError: Cannot save file into a non-existent directory: 'output\sa'`

Solution: Create the `sa\` directory manually in the `output\` directory.

3. `FileNotFoundError: [Errno 2] No such file or directory: b'./input/SA/popchina1km.nc'`

Solution: Rename `. /input/SA/popchina3km.nc` to `. /input/SA/popchina1km.nc`.

--------------------

The figure shows the result of list allocation under different `ratio`.

<img src="fig/不同ratio下的降尺度结果.png" alt="不同ratio下的降尺度结果" style="zoom:67%;" />

## Step 3: Prepare the emission inventory file

This section is based on `prepmodel`.

Go to the directory where the `area_inlinenew.exe` executable is located, and then configure the `par.ini` file.

```ini
#
#   ISAT.M
#
[runtime]
runtime:720
[gridcro2d]
gridcro2d: ./src/met/GRIDCRO2D_3km
[speciate]
speciate: ./src/speciate/speciate_AR.csv,./src/speciate/speciate_AG.csv,./src/speciate/speciate_TR.csv
#speciate_groups:./src/speciate/speciate_PP.csv,./src/speciate/speciate_BL.csv,./src/speciate/speciate_CE.csv,./src/speciate/speciate_CO.csv,./src/speciate/speciate_IS.csv,./src/speciate/speciate_NH.csv,./src/speciate/speciate_PT.csv,./src/speciate/speciate_SI.csv,./src/speciate/speciate_VO.csv,./src/speciate/speciate_VP.csv,./src/speciate/speciate_VU.csv,./src/speciate/speciate_CPMO.csv,./src/speciate/speciate_CPMI.csv,./src/speciate/speciate_AL.csv,./src/speciate/speciate_YL.csv,./src/speciate/speciate_GL.csv,./src/speciate/speciate_BK.csv,./src/speciate/speciate_HS.csv,./src/speciate/speciate_LM.csv,./src/speciate/speciate_RM.csv
[temporary]
#energy,point,area,mobile,flat
temporary_hour : ./src/temporary/hourly.csv
temporary_week : ./src/temporary/weekly.csv
temporary_month: ./src/temporary/monthly.csv
[emissions]
emissions: ./src/emissions/3kmMY/AR.csv,./src/emissions/3kmMY/AG.csv,./src/emissions/3kmMY/TR.csv
#stack_groups: ./src/emissions/WK/STACK_GROUP_PP.csv,./src/emissions/WK/STACK_GROUP_BL.csv,./src/emissions/WK/STACK_GROUP_CE.csv,./src/emissions/WK/STACK_GROUP_CO.csv,./src/emissions/WK/STACK_GROUP_IS.csv,./src/emissions/WK/STACK_GROUP_NH.csv,./src/emissions/WK/STACK_GROUP_PT.csv,./src/emissions/WK/STACK_GROUP_SI.csv,./src/emissions/WK/STACK_GROUP_VO.csv,./src/emissions/WK/STACK_GROUP_VP.csv,./src/emissions/WK/STACK_GROUP_VU.csv,./src/emissions/WK/STACK_GROUP_CPMO.csv,./src/emissions/WK/STACK_GROUP_CPMI.csv,./src/emissions/WK/STACK_GROUP_AL.csv,./src/emissions/WK/STACK_GROUP_YL.csv,./src/emissions/WK/STACK_GROUP_GL.csv,./src/emissions/WK/STACK_GROUP_BK.csv,./src/emissions/WK/STACK_GROUP_HS.csv,./src/emissions/WK/STACK_GROUP_LM.csv,./src/emissions/WK/STACK_GROUP_RM.csv
```

parameter description of `par.ini`:

---------------------

**runtime**: Length of inventory. (unit: hour)

**gridcro2d**：The path of GRIDCRO2D file.

**speciate**: The path where the species assignment spectrum file is located.

**temporary_***: Time allocation spectrum file path.

**emissions**: The path where the output file of **Step. 2** is located needs to be in one-to-one correspondence with the **species allocation file**.

---------------------------------

After configuring the `par.ini` file, enter the following command in the terminal to start running.

```shell
./area_inlinenew.exe
```

If no error is reported, the program runs successfully.
