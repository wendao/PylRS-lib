import sys

from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

mm_WT = "TDRLEVLLNPKDEISLNSGKPFRELESELLSRRKKDLQQIYAEERENYLGKLEREITRFFVDRGFLEIKSPILIPLEYIERMGIDNDTELSKQIFRVDKNFCLRPMLAPNLYNYLRKLDRALPDPIKIFEIGPCYRKESDGKEHLEEFTMLNFCQMGSGCTRENLESIITDFLNHLGIDFKIVGDSCMVYGDTLDVMHGDLELSSAVVGPIPLDREWGIDKPWIGAGFGLERLLKVKHDFKNIKRAARSESYYNGISTNL"
mb_WT = "RVEALLSPEDKISLNMAKPFRELEPELVTRRKNDFQRLYTNDREDYLGKLERDITKFFVDRGFLEIKSPILIPAEYVERMGINNDTELSKQIFRVDKNLCLRPMLAPTLYNYLRKLDRILPGPIKIFEVGPCYRKESDGKEHLEEFTMVNFCQMGSGCTRENLEALIKEFLDYLEIDFEIVGDSCMVYGDTLDIMHGDLELSSAVVGPVSLDREWGIDKPWIGAGFGLERLLKVMHGFKNIKRASRSESYYNGISTNL"

def get_muts( shift, ref, seq ):
  #Kprint(ref)
  #print(seq)
  assert( len(ref) == len(seq) )
  muts = []
  if ref == seq: return muts
  pos = shift[0]
  for (a, b) in zip( ref, seq ):
    pos += 1
    if a != b:
      muts.append( a+str(pos+shift[1])+b )
  return muts

#lines = open("sequencing.txt", 'r').readlines()
lines = open(sys.argv[1], 'r').readlines()
for n,l in enumerate(lines):
  l = l.strip()
  if n % 3 == 0:
    es = l.split()
    pore = es[0]
    pylrs = es[1]
    if pylrs == "Mm":
      ref = mm_WT
      shift = [194, 0]
    elif pylrs == "Mb":
      ref = mb_WT
      shift = [161, 35]
    else: ref == None
  elif n % 3 == 1:
    dna = Seq.Seq(l, IUPAC.unambiguous_dna)
    mrna = dna.transcribe()
    prot = mrna.translate()
    muts = get_muts( shift, ref, prot )
    if len(muts)>0:
      print pore, pylrs, "|".join(muts)
