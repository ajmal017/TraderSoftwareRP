# -*- coding: utf-8 -*-
import os, sys, glob, csv, subprocess, datetime, shutil, subprocess, time
#########################################
path = os.getcwd() + '/'
rootpath = ((path.replace('EXE','|')).split('|'))[0]
localtagSLASH = '_RP/'
localtag = '_RP'
EXEnoslash = rootpath + 'EXE' + localtag
EXE = rootpath + 'EXE' + localtag + '/'
sys.path[0:0] = [EXEnoslash]
DataDown = 'C:/TS/TSIBData/'
DataDownNoSlash = 'C:/TS/TSIBData'
########################
timeFormat = "%Y%m%d %H:%M:%S"
dateFormat = "%Y%m%d"
##########################
import rpu_rp, rpInd, ibutiles
from time import sleep, strftime, localtime  
from ib.ext.Contract import Contract  
from ib.opt import ibConnection, message
from ib.ext.Order import Order
from ib.opt import Connection, message   #
############################################
global today, sym, fname
today =  rpu_rp.todaysdateunix()
newDataList = []
########
mode = 'intraday'#'intraday' #'hourly' ## 'daily'  'intraday'
answer=1#raw_input('1. intraday \n 2. hourly \n 3. daily')
if answer == '1':
    mode = 'intraday'
elif answer == '2':
    mode = 'hourly'
else:
    mode = 'daily'
#################################
libbars = EXE + 'library.bars.csv'
libsyms = EXE + 'library.syms.csv'
bardict = rpu_rp.create_dict(libbars,0,1)
modedict  = rpu_rp.create_dict(libbars,0,5)
barlistall = bardict.keys()
barlist =[]
for b in barlistall:
    if modedict[b] == mode:
        barlist.append(b)
##########################
barlist = ['5 secs']
dur = '5 secs'
symdict = rpu_rp.create_dict(libsyms,0,1)
symbol_list = symdict.keys()
##symbol_list = ['ZD']
print symbol_list
print barlist
#################################################
count =0
trans_id = 0
############################################################
def error_handler(msg):
    if  'historicalData' in str(msg):
        print 'error probably pacing hist data'
        pass
    elif 'connection is OK' in str(msg):
        pass
    else:
        print "Server Error: %s" % msg
def reply_handler(msg):
    if msg.typeName == 'historicalData':
        pass
    elif 'connection is OK' in str(msg):
        pass
    else:
        print "Server Response: %s, %s" % (msg.typeName, msg)
####################
def historical_data_handler(msg):  
    global newDataList
##    arrayout = []
    fname = DataDown+ today + '.' + sym + '.'  + bar.replace(' ','')+'.ddload.csv'
    if ('finished' in str(msg.date)) == False:  ### keep building the list
##        print (int(msg.date))
        fstring = "%Y-%m-%d %H:%M:%S"
        dateold = localtime(int(msg.date))
        tdate = strftime(fstring, dateold)       
        if bar == '1 day':
            tdate = str((int(msg.date))) + ' 23:59:58'       
        dataStr = '%s, %s, %s, %s, %s, %s, %s' % (sym, tdate, msg.open, msg.high, msg.low, msg.close, msg.volume)
##        if msg.typeName == 'open':
##            lineout =[]
##        lineout.append(sym)
##        lineout.append(tdate)
##        lineout.append(msg.open)
##        lineout.append(msg.high)
##        lineout.append(msg.low)
##        lineout.append(msg.close)
##        lineout.append(msg.volume)
##        arrayout.append(lineout)
        newDataList = newDataList + [dataStr]  
    else:
        print 'next list'
        if os.path.isfile(fname):
            os.remove(fname) #flush the file
        rpu_rp.WriteArrayToCsvfile(fname,arrayout)

##        for a in newDataList:
##            rpu_rp.WriteStringsToFileAppend(fname,a)
        newDataList = []  
####################################       
tws_conn = Connection.create(port=7496, clientId=91)
tws_conn.connect()
tws_conn.register(error_handler, 'Error')
tws_conn.registerAll(reply_handler)
tws_conn.register(historical_data_handler, message.historicalData)
#######################################
for sym in ['GBP.USD']:#symbol_list:
    for bar in barlist:
##        fname = DataDown +today+'.'+sym+ '.'+bar +'.rthbars.csv'
        duration = bardict[bar]
        print bar, sym
        contract = ibutiles.create_ticksym(trans_id,sym)
        tws_conn.reqHistoricalData(trans_id, contract, '', duration, bar, 'MIDPOINT', 0, 2)
        trans_id = trans_id + 1  
        sleep(2)
###############
print 'disconnecting from ib..'
tws_conn.disconnect()
