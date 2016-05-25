import os, sys
path = os.getcwd() + '/'
EXEnoslash = ((path.replace('\\AALIVE_TRADING','|')).split('|'))[0]
rootpath = ((path.replace('EXE','|')).split('|'))[0]
sys.path[0:0] = EXEnoslash
localtag = ((EXEnoslash.replace('EXE','|')).split('|'))[1] #'_RP'
print localtag,'is local'
#########################################
import ENVvars
nd ={}
nd = ENVvars.ENVvars(localtag)
##resolve vardict back to normal variables
for var in nd.keys():
    if 'tickval' in var:
        print var
    locals()[var] = nd[var]
#######################################
import ENVdicts
nd ={}
nd = ENVdicts.ENVdicts(localtag)
for var in nd.keys():
    if 'tickval' in var:
        print var
        print var, nd[var]
    locals()[var] = nd[var]
##################
global recentlimit, time_format,timedate_format, nextorderID
from time import sleep, strftime, localtime
import  rpu_rp, rpInd, ibutiles, TicksUtile,RulesEngine, RP_Snapshot, glob, csv, subprocess, datetime, shutil, time
from datetime import datetime
import ctypes
global date
date =   today  ######## <<<<<<<
teststr = 'grnNnotailNbigbar' #'2016-02-19 21:'
closestr = 'grnNnotailN'
pos = netcost = 0
'''
add 5 bar moving average, vwap study, breakpoints assembler option
'''
import Createlines
#################################
def show_spots(sym,date,limit,spotfile):
    curprice = float(TicksUtile.recenttick(sym,'recent'))
    spotlines= rpu_rp.CsvToLines(spotfile)
    for l in spotlines:
        spotp = float(l[0])
        if len(l) > 1 :
##            print l
            spotid = l[1]
            pass
        else:
            spotid=''
        distance = abs(spotp-curprice)
        if (spotp-curprice) > 0:
            underover = 'under'
        else:
            underover = 'over'
        if distance < limit:
            if underover == 'under':
                sflag = 'SELL'
            else:
                sflag = 'BUY'
            print ('>>%4s at %8.2f %s|%s |%4.2f |%8.2f > pass#? range=%d' % (sflag,spotp,spotid,sym,distance,curprice,limit))
#####################
def showlines(sym,dur,buysell):
    filen = DataDown +date +'.'+sym+'.'+dur + '.both.HA.csv'
    lines = rpu_rp.CsvToLines(filen)
    newlines = []
    pnlsign = -1    
    if buysell == 'sell':
        teststr = 'redNnotailNbigbar' #'2016-02-19 21:'
        closestr = 'redNnotailN'
        pnlsign = (1)
        pass
    elif buysell == 'buy':
        teststr = 'grnNnotailNbigbar' #'2016-02-19 21:'
        closestr = 'grnNnotailN'
        pass
    else:
        teststr = 't'
        closestr = 'xxxxx'
    pos =  netcost = 0
    for l in lines:
        markprice = round(float(l[5]),2)
        tdate = str(l[1])
        if teststr in str(l):  #if red signal sell one until..
            pos +=1
            netcost += (1 * markprice)
            avgcost = round(netcost / pos,2)
            oneline = str(pos)+ ' | ' + str(avgcost)+ ' | ' +  str(markprice)+ ' | ' + tdate
            if buysell == 'allxx':
                newlines.append(l[1]+l[12])
                pass
            else:
                newlines.append(oneline)
    ##        print l
        if closestr not in str(l):
            pnl = (netcost - (markprice * pos) )*pnlsign
            if pos != 0 :
                oneline = 'closing_' + buysell.upper() +' | ' + str(markprice)+ ' | pnl= ' +str(pnl) + ' | ' + tdate
                if buysell != 'allxx':
                    newlines.append(oneline)
            netcost = 0
            pos = 0
    return newlines
#################
##print spaceYtime_format
now = datetime.strftime(datetime.now(),spaceYtime_format)

def run_oneloop(dur,now,sym):
    now_epoch = int(time.mktime(time.strptime(now, spaceYtime_format)))
    print '##### ',now, dur, sym,' ####### '
    Createlines.create_HAs([sym])
    ##########
    perc = .70
    maxlines = 6
    difflimit = 700
    taglist = ['buy','sell','allxx']
    for tag in taglist:    
        b = showlines(sym,dur,tag)
        print '#############'
        print '>>>>>> ',tag.upper(), 'WINDOW',dur,sym, ' <<<'
        lenha = len(b)
        c=0
        climitlines = int(lenha * perc)
        climit = max((lenha-maxlines),climitlines)
        bar_time = '  2016-02-21 13:16:30'
        for lha in b:
            c+=1
            if tag != 'allxx':
                if len(lha.split('|')) > 2:
                    bar_time = (lha.split('|')[3]).replace(' 201','201')  
                bar_time_epoch =  TicksUtile.time_to_epoch(bar_time)          
                tdiff =  now_epoch - bar_time_epoch
            else:
                    bar_time_epoch =  TicksUtile.time_to_epoch(bar_time)          
                    tdiff =  0# now_epoch - bar_time_epoch                
            if c > climit and tdiff < difflimit :
                print lha,'>>> ',tdiff #,difflimit
            #######   
############################################
loopmax = 505
loop =0
while loop < loopmax:
    sym = 'FDAX'
##    sym = 'ES'
    now = datetime.strftime(datetime.now(),spaceYtime_format)
    dur = '5mins'
    run_oneloop(dur,now,sym)
##    dur = '1min'
##    run_oneloop(dur,now,sym)
    factor = 1
    limitlines = 5.0
    
    daxcurprice = float(TicksUtile.recenttick('FDAX','recent'))
    escurprice = float(TicksUtile.recenttick('ES','recent'))
    sym = 'ES'
    print '###### LINEFADE #### ',escurprice ,sym
    spotfile = libarea + 'spotlines.' + sym+ '.csv'
    show_spots(sym,date,limitlines,spotfile)
##    print 'dailies'
##    spotfile = libarea +'ES.daily.spotlines2.csv'
##    show_spots(sym,date,limitlines,spotfile)
    
##    spotfile = libarea +'spotlinesDaily.ES.csv'
##    show_spots(sym,date,limitlines,spotfile)   
    spfile = libarea + 'spotlinesRoundies.' +sym+'.csv'
    show_spots(sym,date,limitlines,spfile)   
##    sym = 'FDAX'
##    limitlines = 15.0
##    spfile = libarea + 'spotlinesRoundies.' +sym+'.csv'
##    show_spots(sym,date,limitlines,spfile)

    loop+=1
    sleep(15)
'''
['ES', ' 2016-02-19 22:05:00', '1913.75', '1914.5', '1913.75', '1914.0',
'8603.0', 'full', '300', '0.25', '0.5', '0.0', 'grnNnotailNshortbar']
['ES', ' 2016-02-19 22:30:00', '1914.25', '1914.25', '1913.75', '1914.0', '471.0', 'full', '960', '-0.25', '0.0', '-0.25', 'redNnotailNshortbar']
'''
