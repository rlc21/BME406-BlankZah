import pyrosetta_installer

pyrosetta_installer.install_pyrosetta()
import pyrosetta
from pyrosetta import *
import sys
from tqdm import tqdm
from pyrosetta.toolbox import cleanATOM, mutate_residue
from random import randrange, choice
import copy
from datetime import datetime

job_id = int(sys.argv[1])

pyrosetta.init("-mute all")
# pyrosetta.init("-mute core basic protocols")

AA = [
    "A",
    "R",
    "N",
    "D",
    "C",
    "Q",
    "E",
    "G",
    "H",
    "I",
    "L",
    "K",
    "M",
    "F",
    "P",
    "S",
    "T",
    "W",
    "Y",
    "V",
]
residue_mut = [[32], [33, 34, 36, 44, 45], [41], [57]]
AA_options = [
    ["D", "N", "S", "T"],
    ["A", "R", "N", "D", "Q", "E", "H", "K", "S", "T", "W", "Y"],
    ["A", "S", "T", "V", "L"],
    ["N", "H", "Y"],
]
all_mutations = [[]]
for i in range(len(residue_mut)):
    for j in range(len(residue_mut[i])):
        for k in range(len(AA_options[i])):
            for l in range(3):
                all_mutations.append([residue_mut[i][j] + 1 + l * 33, AA_options[i][k]])
all_mutations = all_mutations[1:]

sfxn = get_score_function()
fr = pyrosetta.rosetta.protocols.relax.FastRelax(
    scorefxn_in=sfxn, standard_repeats=1
)  # , standard_repeats=1
# fr.constrain_relax_segments()

ligand_params = Vector1(["./Autoinduced_Peptide_1.params"])
pose = pyrosetta.Pose()
pose_old = pyrosetta.Pose()
res_set = pose.conformation().modifiable_residue_type_set_for_conf()
res_set.read_files_for_base_residue_types(ligand_params)
pose.conformation().reset_residue_type_set_for_conf(res_set)
pose_old.conformation().reset_residue_type_set_for_conf(res_set)

pose_from_file(pose, "./input/DARPin_Bound_" + str(job_id // 5 + 1) + ".pdb")
for i in range(10000):  # terrible way to randomize mut positions
    mut = choice(all_mutations)
    mutate_residue(pose, mut[0], mut[1])  # 1-indexed AA to mutate

fr.apply(pose)

pose.dump_pdb("./output/flex_" + str(job_id) + ".pdb")

print("starting loop:<" + str(sfxn(pose)) + "," + str(pose.sequence()) + ">")
start_time = datetime.now()
for i in range(100000):
    pose_from_file(pose, "./output/flex_" + str(job_id) + ".pdb")
    mut = choice(all_mutations)
    mutate_residue(pose, mut[0], mut[1])  # 1-indexed AA to mutate
    fr.apply(pose)
    pose_from_file(pose_old, "./output/flex_" + str(job_id) + ".pdb")
    if sfxn(pose) < sfxn(pose_old):
        pose.dump_pdb("./output/flex_" + str(job_id) + ".pdb")
        print(
            "["
            + str(datetime.now() - start_time)
            + "]saved:<"
            + str(sfxn(pose))
            + ","
            + str(pose.sequence())
            + ">"
        )
