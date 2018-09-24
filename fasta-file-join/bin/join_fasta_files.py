#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:09:19 2018

@author: akshay yadav
"""

import sys
import re

def get_fasta_seq_dict(fasta_fileName):
    fasta_seq_dict={}
    fasta_file = open(fasta_fileName,"r")
    for line in fasta_file:
        line=line.rstrip()
        if(re.match('^\>',line)):
            fasta_seq_dict[line[1:]]=1
    fasta_file.close()
    
    return(fasta_seq_dict)
 
    
def left_join(fasta1_seq_dict, fasta2_seq_dict):
    for seq in fasta1_seq_dict:
        if(fasta2_seq_dict.has_key(seq)):
            print '{0} {1}'.format(seq,seq)
        else:
            print '{0} {1}'.format(seq,'---')
            
def right_join(fasta1_seq_dict, fasta2_seq_dict):
    for seq in fasta2_seq_dict:
        if(fasta1_seq_dict.has_key(seq)):
            print '{0} {1}'.format(seq,seq)
        else:
            print '{0} {1}'.format('---', seq)
    


def inner_join(fasta1_seq_dict, fasta2_seq_dict):
     for seq in fasta1_seq_dict:
        if(fasta2_seq_dict.has_key(seq)):
            print '{0} {1}'.format(seq,seq)
    
    
def full_join(fasta1_seq_dict, fasta2_seq_dict):
    seq_dict={}
    seq_arr = fasta1_seq_dict.keys()+fasta2_seq_dict.keys()
    
    for seq in seq_arr:
        seq_dict[seq]=1

    for seq in seq_dict:
        if(fasta1_seq_dict.has_key(seq) and fasta2_seq_dict.has_key(seq)):
            print '{0} {1}'.format(seq,seq)
        
        elif(fasta1_seq_dict.has_key(seq)):
            print '{0} {1}'.format(seq,'---')
        
        elif(fasta2_seq_dict.has_key(seq)):
            print '{0} {1}'.format('---', seq)


def call_join(join_type, fasta1_seq_dict, fasta2_seq_dict):
    if(join_type=='left'):
        left_join(fasta1_seq_dict, fasta2_seq_dict)
    
    elif(join_type=='right'):
        right_join(fasta1_seq_dict, fasta2_seq_dict)
        
    elif(join_type=='inner'):
        inner_join(fasta1_seq_dict, fasta2_seq_dict)
        
    elif(join_type=='full'):
        full_join(fasta1_seq_dict, fasta2_seq_dict)

fasta1_fileName = sys.argv[1]
fasta2_fileName = sys.argv[2]
join_type = sys.argv[3]


fasta1_seq_dict = get_fasta_seq_dict(fasta1_fileName)
fasta2_seq_dict = get_fasta_seq_dict(fasta2_fileName)

call_join(join_type, fasta1_seq_dict, fasta2_seq_dict)


        

