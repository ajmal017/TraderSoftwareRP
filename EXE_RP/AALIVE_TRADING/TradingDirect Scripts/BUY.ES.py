import os, sys
localtag = '_RP'
path = os.getcwd() + '/'
rootpath = ((path.replace('EXE','|')).split('|'))[0]
EXEnoslash = rootpath + 'EXE' + '_RP'
sys.path[0:0] = [rootpath + 'EXE' + '_RP']
#########################################
import ENVvars
nd ={}
nd = ENVvars.ENVvars(localtag)
##resolve vardict back to normal variables
for var in nd.keys():
    locals()[var] = nd[var]
#######################################
import ENVdicts
nd ={}
nd = ENVdicts.ENVdicts(localtag)
for var in nd.keys():
##    print var
    locals()[var] = nd[var]
####################
global recentlimit, time_format,today,timedate_format, nextorderID
import  rpu_rp, rpInd, ibutiles, TicksUtile, RP_Snapshot
import glob, csv, subprocess, datetime, shutil, time, os.path
####################
slibarea = sigarea + 'orderlib/'
print slibarea
sellfile = slibarea  +'nodate.recentsigsexecHARD.SELL.ES.csv'
sellfile = slibarea  +'nodate.recentsigsexecHARD.BUY.ES.csv'
siglistfile = sigarea + today +'.recentsigsexecHARD.csv'
shutil.copy(sellfile,siglistfile)


