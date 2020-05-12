#!/usr/bin/env   

import sys

def get_seq(seqfile):
    seq=''
    for line in open(seqfile):
        if line[0] != '>' :seq=seq+line.rstrip()
    return seq
        
def get_ranges(bedfile):
    l=[]
    for line in open(bedfile):
        v=line.split()
        l.append([v[1], int(v[2]), int(v[3])])
    return l

def match_seq(bed, seq): # go from beginning to the end of the ranges and got one by one and assign the ranges to gpc island
    ''' Create a string that is as long as the chromosome with a chain of 'N' for the Non GCP regions and 'Y' for GCP regions.
    We are trying to generate the same sequence oth the chromosome. To match the things on top of the other. So we start from
    p0 wich is a No region and '''
    s=''
    n=len(bed)
    p0=0 # we start from the initial pos 'like a cursor' - so this will move along the seq
    for i in range(n): #in this case we dont check for the chomosome because we know allready where it is
        s=s+(bed[i][1]-p0-1)*'N'
        s=s+(bed[i][2]-bed[i][1])*'Y'
        p0=bed[i][2]
    print(len(s))
    s=s+(len(seq)-bed[i][2])*'N'
    return s
         
if __name__ == '__main__': #makes your program executable even if it is a module with several files.
    bedfile=sys.argv[1]
    seqfile=sys.argv[2]
    seq=get_seq(seqfile)
    bed=get_ranges(bedfile)
    chr21=len(seq)
    nseq=match_seq(bed, seq)
    print(len(nseq), len(seq))
