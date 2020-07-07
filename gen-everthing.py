import sys, os, shutil
from string import Template
import Bio
from Bio import SeqIO

for record in SeqIO.parse("templates/MmPylRS.fasta", "fasta"):
    mm = record

for record in SeqIO.parse("templates/MbPylRS.fasta", "fasta"):
    mb = record

#print mm.seq
#print mb.seq
enz_dict = {}
pdb_dict = {}
nat_dict = {
    302: 'A',
    305: 'L',
    306: 'Y',
    309: 'L',
    346: 'N',
    348: 'C',
    384: 'Y',
    401: 'V',
    408: 'D',
    417: 'W',
}

cst1_tmpl = Template("AtomPair O 154 $atm 271 SCALARWEIGHTEDFUNC 10.0 HARMONIC 2.8 0.2\n") #k1
cst2_tmpl = Template("AtomPair H 154 $atm 271 SCALARWEIGHTEDFUNC 10.0 HARMONIC 2.2 0.2\n") #k2
cst3_tmpl = Template("AtomPair H 238 $atm 271 SCALARWEIGHTEDFUNC 10.0 HARMONIC 2.3 0.2\n") #k3
cst4_tmpl = Template("AtomPair MG 270 $atm 271 SCALARWEIGHTEDFUNC 10.0 HARMONIC 2.3 0.2\n") #k4
cst5_tmpl = Template("AtomPair MG 270 $atm 211 SCALARWEIGHTEDFUNC 10.0 HARMONIC 2.3 0.5\n") #OE1
cst6_tmpl = Template("AtomPair MG 270 $atm 211 SCALARWEIGHTEDFUNC 10.0 HARMONIC 2.6 0.5\n") #OE2
cst7_tmpl = Template("AtomPair NH1 145 $atm 271 SCALARWEIGHTEDFUNC 10.0 HARMONIC 3.0 0.2\n") #k5
cst8_tmpl = Template("AtomPair NH2 145 $atm 271 SCALARWEIGHTEDFUNC 10.0 HARMONIC 3.0 0.2\n") #k5
cst9_tmpl = Template("AtomPair NH2 145 $atm 271 SCALARWEIGHTEDFUNC 10.0 HARMONIC 3.0 0.2\n") #k6

lines = open("Enz-info-2020.csv", 'r').readlines()
for l in lines[1:]:
    es = l.strip(). split(',')
    ndx = int(es[0])
    name = es[1]
    muts = es[2].split('|')
    print ndx, name, name
    if name == "MmPylRS":
        ref = mm
        shift = 185
        pdb_dict[ndx] = "mm"
    elif name == "MbPylRS":
        ref = mb
        shift = 150
        pdb_dict[ndx] = "mb"
    else:
        assert(False)
    enz_dict[ndx] = []
    if muts[0] == "-":
        seq = ref.seq
        seq_str = str(seq)
    else:
        #parse muts
        for mut in muts:
            nat = mut[0]
            pos = int(mut[1:-1])
            mut = mut[-1]
            if seq[pos-1] != nat:
                seq_str = seq_str[:pos-2] + mut + seq_str[pos:]
                #print ndx, name, seq[pos-1], pos, nat
                #print seq_str[shift:]
            enz_dict[ndx].append((nat, pos-1, mut))
    #for n, p, m in enz_dict[ndx]:
    #    print n, str(p-shift)

lines = open("pairs.txt", 'r').readlines()
nr = 0
for l in lines:
    #deal with native protein first
    es = l.split(',')
    enz = int(es[1])
    uaa = es[0]
    nr = nr + 1

    print "log=", nr, enz, uaa, pdb_dict[enz]
    #create dir and prepare init file
    react_dir = "R"+str(nr)
    if not os.path.exists(react_dir):
        os.mkdir(react_dir)

    #copy scaffold and lig
    shutil.copyfile("templates/"+pdb_dict[enz]+"/scaffold_ala.pdb", react_dir+"/scaffold_ala.pdb")
    shutil.copyfile("templates/"+pdb_dict[enz]+"/bbCA.cst", react_dir+"/opt.cst")
    shutil.copyfile("templates/"+pdb_dict[enz]+"/pssm1.txt", react_dir+"/pssm1.txt")

    #mutate to enzN.pdb
    shutil.copyfile("resfile.tmpl", react_dir+"/resfile")
    fp = open(react_dir+"/resfile", 'a')
    if pdb_dict[enz] == "mm":
        shift = 1
        shift2 = 0
    else:
        shift = -88
        shift2 = 35
    #gen resfile with all pos
    for n, p, m in enz_dict[enz]:
        print n, p, m
        nat_dict[p+1+shift2] = m
    for p in nat_dict.keys():
        fp.write("%d A PIKAA %c\n" % (p-shift2+shift-1, nat_dict[p]) )
    fp.close()

    #copy lig.pdb and params
    shutil.copyfile("ligands/U"+uaa+"/rotlib/LIG_0001.pdb", react_dir+"/LIG_0001.pdb")
    shutil.copyfile("ligands/U"+uaa+"/rotlib/LIG.params", react_dir+"/LIG.params")
    shutil.copyfile("ligands/U"+uaa+"/rotlib/LIG.tors", react_dir+"/LIG.tors")
    shutil.copyfile("ligands/U"+uaa+"/rotlib/rotlib.pdb", react_dir+"/rotlib.pdb")
    atoms = open("ligands/U"+uaa+"/rotlib/key_atoms.txt", 'r').readlines()[0].split()
    with open(react_dir+"/opt.cst", 'a') as f:
      f.write(cst1_tmpl.substitute(atm=atoms[0]))
      f.write(cst2_tmpl.substitute(atm=atoms[1]))
      f.write(cst3_tmpl.substitute(atm=atoms[2]))
      f.write(cst4_tmpl.substitute(atm=atoms[3]))
      f.write(cst5_tmpl.substitute(atm="OE1"))
      f.write(cst6_tmpl.substitute(atm="OE2"))
      f.write(cst7_tmpl.substitute(atm=atoms[4]))
      f.write(cst8_tmpl.substitute(atm=atoms[4]))
      f.write(cst9_tmpl.substitute(atm=atoms[5]))

    #relax with cst

