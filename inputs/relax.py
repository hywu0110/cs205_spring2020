# ziyan zhu
import vasp_config as vc
import multilayer_config_generator as mcg
import sys
import os
import re
from shutil import copyfile
import time

vasp_dir = "/vasp_relax_test/" # master directory to run vasp

align = []
for arg in sys.argv[2:]:
    align.append(int(arg))
# generate input files for 20 different layer separations
# 05/02/2020: consider general cases
masterdir = os.getcwd()
copyfile(masterdir + '/bat_vasp', masterdir+vasp_dir+'/bat_vasp')
for dz in range(15):
    # create config file
    set = mcg.MultilayerSet(layer_number=[2], alignments=align, verticals=[0,3.6+0.14*dz])
    set.config_writer()
    dir = set.multilayer_directory[1:]
    print(dir)
    fname = set.fname
    
    for f in fname:
        folder=f[7:]
        # os.system("cd " + vasp_dir)
        os.makedirs(os.getcwd()+vasp_dir+folder, exist_ok = True)
        copyfile(os.getcwd()+dir+f,os.getcwd()+vasp_dir+folder+"/config")
        
        subdir = vasp_dir+folder
        # print(subdir)
        v = vc.Vasp_Config(target=os.getcwd()+subdir+"/config")
    
        v.POSCAR_writer(subdir+"/POSCAR")
        v.POTCAR_writer(subdir+"/POTCAR",subdir+"/POSCAR")
        v.KPOINT_writer(subdir+"/KPOINTS")
        params = v.params
        params["ISIF"]=3
        params["NPAR"]=2
        params["NSW"]=2
        v.INCAR_writer(v.params,subdir + "/INCAR")
        
        print(subdir)
        os.chdir(os.getcwd()+subdir)
        copyfile(masterdir + '/bat_vasp', masterdir+vasp_dir+'/bat_vasp')
        #copyfile(masterdir + '/bat_vasp', os.getcwd()+'/bat_vasp')
        copyfile(masterdir + '/params.conf', os.getcwd()+'/params.conf')
        os.chdir(masterdir)
