#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:26:38 2020

@author: carmen

Comparing scrists or text files
"""

def Comparison1():
    file1 = open('d2010_ParticleTracking.py', 'r')
    file2 = open('d2010_ParticleTracking1.py', 'r')
    # FO = open('some_output_file.txt', 'w')
    
    for line1 in file1:
        for line2 in file2:
            if line1 != line2:
                # FO.write("%s\n" %(line1))
                print(line1)
    
    # FO.close()
    file1.close()
    file2.close()


def Comparison2():
    with open('d2010_ParticleTracking.py', 'r') as file1:
        with open('d2010_ParticleTracking1.py', 'r') as file2:
            same = set(file1).intersection(file2)
    
    
    for line in enumerate(same):
        continue
    else:
        print(line)
    
    
    # with open('some_output_file.txt', 'w') as file_out:
    #     for line in same:
    #         file_out.write(line)


Comparison2()
