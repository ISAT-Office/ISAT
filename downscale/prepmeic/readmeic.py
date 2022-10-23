import pandas as pd
import os
files = os.listdir(".")
def readmeic(inv):
    df = pd.read_csv(inv,header=5)
    tmp=[]
    uid=[]
    nrows = 200
    ncols = 320
    ids = 0 
    for nx in range(nrows):
        for ny in range(ncols):
#            print(nx)
#            tmpv = str(df[df.columns[0]][0]) #[nx])
#            print(tmpv)
            value = float(df[df.columns[0]][nx].split(" ")[ny])
            if value <0 :
               value = 0
            tmp.append(value)
    return tmp 

def poptype(inv):
    print(inv.split('_'))
    out=inv.split('_')[5][:(len(inv.split('_')[5])-4)]
    return out

def readids():
    uid=[]
    ulon=[]
    ulat=[]
    uarea=[]
    nx = 320
    ny = 200
    ids = 0 
    lon1 = 70
    lat1 = 60
    dgrid = 0.25
    for j in range(0,ny):
        for i in range(0,nx):
#            uid.append(ids)
            ids = i +(ny-1-j)*nx
            lon = lon1 +dgrid*(i+0.5)
            lat = lat1 -dgrid*(j+0.5)
            uid.append(ids)
            ulat.append(lat)
            ulon.append(lon)

    return uid,ulat,ulon

#for i in files:  
for mon in ['01','02','03','04','05','06','07','08','09','10','11','12']:
      for sect in ['power','residential','industry','transportation','agriculture']:
          dftmp = pd.DataFrame()
          uid,ulat,ulon = readids()
          print(len(uid))
          print(len(ulat))
 
          dftmp['ID']=uid
          dftmp['LAT']=ulat
          dftmp['LON']=ulon
          dftmp['month']=mon
          dftmp['sector']=sect
          print(mon)
          print(sect)
          for popu in ['PM2.5','PMcoarse','PM10more','SO2','NOx','NH3','CO','BC','OC']:
              for i in files:
                   if ("_"+mon in i) and (sect in i) and (popu in i):
                      print(i)
                      pop=poptype(i)
                      tmp=readmeic(i)
                      dftmp[pop]= tmp
          dftmp.to_csv(mon+sect+".csv",index=False)      
          dftmp=[]
