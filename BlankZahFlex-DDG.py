import pyrosetta_installer; pyrosetta_installer.install_pyrosetta()
import pyrosetta; pyrosetta.init()
from pyrosetta import *
import glob
print(glob.glob("*.pdb"))

from pyrosetta.toolbox import cleanATOM, mutate_residue
from random import randrange,choice
import copy
AA= ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
sfxn = get_score_function()
fr = pyrosetta.rosetta.protocols.relax.FastRelax(scorefxn_in=sfxn , standard_repeats=1)# , standard_repeats=1
# fr.constrain_relax_segments()

ligand_params = Vector1(['./Autoinduced_Peptide_1.params'])
pose = pyrosetta.Pose()
pose_old = pyrosetta.Pose()
res_set = pose.conformation().modifiable_residue_type_set_for_conf()
res_set.read_files_for_base_residue_types( ligand_params )
pose.conformation().reset_residue_type_set_for_conf( res_set )
pose_old.conformation().reset_residue_type_set_for_conf( res_set )
print("starting loop")
for i in range(100000):
    pose_from_file(pose, "./flexddg_run.pdb")
    mutate_residue(pose,randrange(1,len(pose.sequence())+1),choice(AA)) # 1-indexed AA to mutate
    fr.apply(pose)
    print(pose.sequence())
    pose_from_file(pose_old, "./flexddg_run.pdb")
    if sfxn(pose)<sfxn(pose_old):
        pose.dump_pdb("./flexddg_run.pdb")
        print("saved")