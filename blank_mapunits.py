import os
import shutil

grid = list(['A-1','A-2','A-3','A-4','A-5','A-6','A-7','A-8','B-1','B-2','B-3','B-4','B-5','B-6','B-7','B-8','C-1','C-2','C-3','C-4','C-5','C-6','C-7','C-8','D-1','D-2','D-3','D-4','D-5','D-6','D-7','D-8','E-1','E-2','E-3','E-4','E-5','E-6','E-7','E-8','F-1','F-2','F-3','F-4','F-5','F-6','F-7','F-8','G-1','G-2','G-3','G-4','G-5','G-6','G-7','G-8','H-1','H-2','H-3','H-4','H-5','H-6','H-7','H-8','I-1','I-2','I-3','I-4','I-5','I-6','I-7','I-8','J-1','J-2','J-3','J-4','J-5','J-6','J-7','J-8'])
srcpath = '/Volumes/Backup5/Projects/J-4/' #edit this to the location of AoCField J-4's static/dynamic/teratree/clustering files (they're quite empty, I checked)
outdir = '/Volumes/Backup5/Projects/MainField_E' #edit this to be the directory you want this to put the completed mess of new files

if os.path.isdir(outdir) == False:
    os.mkdir(outdir)

for i in grid:
    print('Out: '+i)
    if os.path.isdir(os.path.join(outdir, i)) == False:
        os.mkdir(os.path.join(outdir, i))
    shutil.copyfile(os.path.join(srcpath, 'J-4_Dynamic.smubin'), os.path.join(outdir, i, i+'_Dynamic.smubin')) #dynamic
    shutil.copyfile(os.path.join(srcpath, 'J-4_Static.smubin'), os.path.join(outdir, i, i+'_Static.smubin')) #static
    shutil.copyfile(os.path.join(srcpath, 'J-4_TeraTree.sblwp'), os.path.join(outdir, i, i+'_TeraTree.sblwp')) #teratree
    shutil.copyfile(os.path.join(srcpath, 'J-4.00_Clustering.sblwp'), os.path.join(outdir, i, i+'.00_Clustering.sblwp')) #00clustering
    shutil.copyfile(os.path.join(srcpath, 'J-4.01_Clustering.sblwp'), os.path.join(outdir, i, i+'.01_Clustering.sblwp')) #01clustering
    shutil.copyfile(os.path.join(srcpath, 'J-4.10_Clustering.sblwp'), os.path.join(outdir, i, i+'.10_Clustering.sblwp')) #10clustering
    shutil.copyfile(os.path.join(srcpath, 'J-4.11_Clustering.sblwp'), os.path.join(outdir, i, i+'.11_Clustering.sblwp')) #11clustering
