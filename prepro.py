# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:00 2017

@author: Paul
"""
import glob
import os
import shutil

def prepro(basedir):
    print('Hello data is the path '+basedir)
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*task-bart_bold.nii.gz')):
        input=item
        output_path=item.split('.')[0]
        output=output_path+('_brain')
        os.system("usr/lcoal/fsl/bin/bet %s %s -F"%(input, output))
        pdb.set_trace()
def main():
    basedir='/Users/Paul/Desktop/ds000030_R1.0.5_sub10159-10299/data'
    prepro(basedir)
main()



input=glob.glob('/Users/Paul/Desktop/ds000030_R1.0.5_sub10159-10299/data/sub-*/func/sub-*.nii.gz')
print(input[0:10])
len(input)

x=input[0]
print('my path is '+x)
y=x.split('/')
print(y)
whatcomp=y[2]
sub=y[5]
print(sub)

subtask=input[1].split('/')[7].split('.')[0]
print(subtask)

output=subtask+'_brain'
print(output)

os.system('bet %s %s -F %(x, output))