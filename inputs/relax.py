import vasp_config as vc 
import sys
v = vc.Vasp_Config()
v.POSCAR_writer()
v.POTCAR_writer()
v.KPOINT_writer()
params = v.params
params["ISIF"]=3
params["NPAR"]=6
v.INCAR_writer(v.params)

vasp_filepath = sys.argv[1]
v.vasp_run(vaspdir=vasp_filepath)

