#!/usr/bin/python
import sys


def get_ids(idfile):
	ids = open(idfile).read().rstrip().split()
	return ids

def print_seq(ids, dbfile):
	count = 0
	with open(dbfile,'r') as fdb:	#with is better then just open
		for line in fdb:
			if line[0] == '>':
				#pid=line.split('|')[1]
				pid = line[1:].rstrip()
			if pid not in ids:
				print (line.rstrip())


if __name__ == '__main__':
	idfile=sys.argv[1]
	dbfile = sys.argv[2]
	ids = get_ids(idfile)
	print_seq(ids, dbfile)
    