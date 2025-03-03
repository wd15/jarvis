import unittest
import os
from pymatgen.core.structure import Structure
from pymatgen.io.vasp.inputs import Poscar
from jarvis.lammps.jlammps import *
from jarvis.lammps.Surf_Def import vac_antisite_def_struct_gen,surfer

def test_read_data():
    dat=(str('../lammps/examples/Al03.eam.alloy_nist/bulk@mp-134_fold/mp-134/data'))
    ff=str('../lammps/examples/Al03.eam.alloy_nist/bulk@mp-134_fold/mp-134/potential.mod')
    data= (read_data(data=dat,ff=ff))
    assert len(data)== 1

def test_vac_antisite_def_struct_gen():
    dat=(str('../lammps/examples/Al03.eam.alloy_nist/bulk@mp-134_fold/mp-134/data'))
    ff=str('../lammps/examples/Al03.eam.alloy_nist/bulk@mp-134_fold/mp-134/potential.mod')
    data= (read_data(data=dat,ff=ff))
    vacs=vac_antisite_def_struct_gen(struct=data,c_size=0)
    assert len(vacs)== 2

def sample_strt():
    dat=(str('../lammps/examples/Al03.eam.alloy_nist/bulk@mp-134_fold/mp-134/data'))
    ff=str('../lammps/examples/Al03.eam.alloy_nist/bulk@mp-134_fold/mp-134/potential.mod')
    data= (read_data(data=dat,ff=ff))
    return (data)

def test_get_get_phonopy_atoms():
    s=sample_strt()
    phn=get_phonopy_atoms(mat=s)
    assert phn.symbols==['Al']

def test_write_lammps_data():
    success=False
    try:
      s=sample_strt()
      file='in1'
      write_lammps_data(structure=s,file=file)
      success=True
    except:
       pass
    assert success==True 

def test_analyz_loge():
    log='../lammps/examples/Al03.eam.alloy_nist/bulk@mp-134_fold/mp-134/log.lammps'
    x=len(analyz_loge(log))
    assert x==23

#def test_smart_surf():
#    s=sample_strt()
#    parameters = {'phonon_control_file':'/users/knc6/in.phonon','surf_control_file':'/users/knc6/inelast_nobox.mod','def_control_file':'/users/knc6/inelast_nobox.mod','json_dat':'/rk2/knc6/JARVIS-DFT/MDCS/all_mp.json','c_size':3,'vac_size':25,'surf_size':25,'phon_size':20,'cluster':'pbs','exec':'/users/knc6/Software/LAMMPS/lammps-master/src/lmp_serial <in.main >out','pair_style':'eam/alloy','pair_coeff':'../lammps/examples/Al03.eam.alloy','atom_style': 'charge' ,'control_file':'/users/knc6/inelast.mod'}
#    cwd=str(os.getcwd())
#    os.chdir('../lammps/examples/Al03.eam.alloy_nist/bulk@mp-134_fold')
#    sl,sh=smart_surf(strt=s,parameters=parameters)
#    print (sl,sh)
#test_smart_surf()
