import os, sys
localtag = '_RP'
sys.path[0:0] = [((os.getcwd().replace('EXE','|')).split('|'))[0] + 'EXE' +localtag]
#########################################
import ENVdicts
nd ={}
nd = ENVdicts.ENVdicts(localtag)
for var in nd.keys():
##    print var
    locals()[var] = nd[var]
##################
global timedate_format, nextorderID, date, today,recentlimit, time_format
from time import sleep, strftime, localtime
import  rpu_rp, rpInd, ibutiles, TicksUtile, RP_Snapshot, glob, csv, subprocess, datetime, shutil, time, BarUtiles
from time import sleep, strftime, localtime
import RulesEngine
from datetime import datetime
import ctypes
####################
###################################
print 'entry sender'
global  decimalboost
####################
online = 'online'
if online == 'online':
    repliesfile = TMP + 'entryreplys'
    pass
else:
    repliesfile =  TMP + 'entryreplys.test.txt'
###############
from ib.ext.Contract import Contract  
from ib.opt import ibConnection, message
from ib.ext.Order import Order
from ib.opt import Connection, message   ##??
#######################
def localreply_handler(msg):
    if msg.typeName == 'nextValidId':
        nextorderID = msg.orderId
        rpu_rp.WriteStringsToFile(TMP +'OrderIdsSavedlocalsigcreate.csv',str(nextorderID)+ ',')   
    rpu_rp.WriteStringsToFileAppend(repliesfile,str(msg))
    print str(msg)
####################
print 'mode is ' + online
if online == 'online':
    global tws_conn
    tws_conn = Connection.create(port=7496, clientId=55)
    tws_conn.connect()
    tws_conn.register(ibutiles.error_handler, 'Error')
    tws_conn.registerAll(localreply_handler)
###################
def get_orderid():
    tws_conn.reqIds(100)
    sleep(1)
    for l in rpu_rp.CsvToLines(TMP + 'OrderIdsSavedlocalsigcreate.csv'):
        order_id = int(l[0])
    return order_id
###################################
def get_orderidfromfile():
##    tws_conn.reqIds(100)
##    sleep(1)
    for l in rpu_rp.CsvToLines(TMP + 'OrderIdsSavedlocalsigcreate.csv'):
        order_id = int(l[0])
    return order_id
###################################
def get_latest_tick(sym):
    lasttick = TicksUtile.recenttick(sym,'mode')
    return lasttick
##############################
def check_for_CP_change(fname): ##read timestamp from the control panel file
##    from datetime import datetime
    fstring = '%a %b %d %H:%M:%S %Y'
    now_epoch = time.time() 
    filetime = time.ctime(os.path.getmtime(fname))
    filetime_ep = int(time.mktime(time.strptime(filetime, fstring)))
    diff = now_epoch - filetime_ep
    return diff
#########################3
global entryordsstatus_dict,entryordside_dict,entryordsym_dict
###############################
def check_status():
    print entryordsstatus_dict.keys()
    for ordid in entryordsstatus_dict.keys():
        ordsym = entryordsym_dict[ordid]
        ordside = entryordside_dict[ordid]
        currstatus = entryordsstatus_dict[ordid]
        for l in  rpu_rp.grep_Csvfile_to_array(repliesfile,'orderStatus orderId=' + str(parent_order_id)):
##            print 'xxx',l
            newstatus= l[1]
            filledstatus= l[2]
            avgprice = l[4]
#####['<orderStatus orderId=133', ' status=None', ' filled=None', ' remaining=None', ' avgFillPrice=None', ' permId=None',' parentId=None', ' lastFillPrice=None', ' clientId=None', ' whyHeld=None>']
        print newstatus, filledstatus, avgprice, ordid, ordsym, ordside, currstatus
        entryordsstatus_dict[ordid] = newstatus
    print entryordsstatus_dict
##    print entryordside_dict
##    print entryordsym_dict
######################
print 'starting entry sender...'
################
def create_con_dict():
    symcontrdict = {}
    counter = 0
    symbol_list = ['ES','FDAX']
    print symbol_list
    for sym in symbol_list:
        counter +=1
        strike = '2'
        expiry ='20154'
        symcontract =  ibutiles.create_contract(sym,strike,expiry)
        print sym, counter
        sleep (1)
        dict2 = {sym : symcontract}
        symcontrdict.update(dict2)
        print 'adding to dict', sym
    print 'done with dict'
    return symcontrdict
####################
global symcontrdict
symcontrdict = {}
if online == 'online':
    symcontrdict = {}
    symcontrdict = create_con_dict()
##################
entryordsstatus_dict ={}
entryordside_dict ={}
entryordsym_dict ={}
loopmax = 300
agelimit = 1200
loop = 0
cycledelay = 2
################################
rpu_rp.WriteStringsToFile(TMP +'Entry.orders.Sent.csv','')
############
sizemult = 1
#################
while loop < loopmax:
    loop +=1
    check_status()
    print 'entry trader hbeat.',loop, loopmax
    sleep(cycledelay)   
    siglistfile = sigarea + today +'.recentsigsexecHARD.csv'
    if os.path.isfile(siglistfile):
        sigfileage = check_for_CP_change(siglistfile)
        pass
    else:
        sigfileage = 99999999
    if os.path.isfile(siglistfile) and  sigfileage < (cycledelay + agelimit):
        recentsigs =  rpu_rp.CsvToLines(siglistfile)
        if online == 'online':                    
            parent_order_id = get_orderidfromfile()
        else:
            parent_order_id = '888'
            #################3
        for  lastsig in recentsigs:
            sym = lastsig[0]
            profsig = float(lastsig[12])
            tsizesig = float(lastsig[13])
            showdecimal = int(showdecimaldict[sym])
            tside = lastsig[1]
##            profsig = int(lastsig[10])
##            stopsig = profsig * 4
##            stopsig = int(lastsig[11])
##                tsize = (int(tsizedict[sym])* sizemult
            tfactor = float(0.5)
            tsize = int(max(1,(int(tsizedict[sym]) * tfactor))) * sizemult
##            tsize = int(max(1,(int(tsizedict[sym]) * tfactor))) * sizemult
            ttype = 'LIM'
            print 'get latest price'
            print sym
            pricenow = float(TicksUtile.recenttick(sym,'mode'))
##            (get_latest_tick(sym))
            tickvalue = float(tickvaluedict[sym]) 
            ##################################
            print symcontrdict
            if online == 'online':
                symcontract = symcontrdict[sym]
                pass
            else:
                symcontract = 'bla'
            ##################################
######                create_contract(sym,strike,expiry)
            ########################
            profmult = 0.5
            stpmult = 3  ###   <<<<<<<<<
            treverseside = 'SELL'
            absfadeamount = 9
            if tside == 'SELL':
                treverseside = 'BUY'
                profadd = profmult * (-1) * profsig
                fadeamount = absfadeamount
            else:
                fadeamount = absfadeamount * int(-1)
                profadd = profmult * 1 * profsig
            fadedentryprice = pricenow + fadeamount
            mktentryprice = pricenow 
            #################################
            tranflag =  False #  True # True  ### <<<<<<<<<this needs to be flipped for transmits.....!!!!!!
            #################################
            orderstring = str(parent_order_id) + ',' + tside + ',' + str(tsize)  + ',' + sym  + ',' + str(fadedentryprice)
            print 'placing order', orderstring
            rpu_rp.WriteStringsToFileAppend(TMP +'Entry.orders.Sent.csv',orderstring)    
            fadedentryorder1 = ibutiles.create_order('LMT', tsize, tside, fadedentryprice,tranflag,fadedentryprice,fadedentryprice,'entry')
            fadedentryorder2 = ibutiles.create_order('LMT', tsize, tside, fadedentryprice,tranflag,fadedentryprice,fadedentryprice,'entry')
            mktentryorder1 = ibutiles.create_order('LMT', tsize, tside, mktentryprice,tranflag,mktentryprice,mktentryprice,'entry')
            mktentryorder2 = ibutiles.create_order('LMT', tsize, tside, mktentryprice,tranflag,mktentryprice,mktentryprice,'entry')
            stopprice = mktentryprice - (stpmult*profadd)
            profprice = mktentryprice + profadd
            profprice2 = mktentryprice + profadd +profadd
            tsizeprof1 = tsize  #/ 3 )*2
            tsizeprof2 = tsize #/ 3 )*1
            bracketorder1 = ibutiles.create_bracket_order('LMT', tsizeprof1,treverseside,profprice,tranflag,profprice,profprice,'profittxt', parent_order_id)
            bracketorder2 = ibutiles.create_bracket_order('LMT', tsizeprof2,treverseside,profprice2,tranflag,profprice2,profprice2,'profittxt', parent_order_id+2)
##            bracketorderSTP = ibutiles.create_bracket_order('STP', tsize,treverseside,stopprice,tranflag,stopprice,stopprice,'stoptxt', parent_order_id)

            if online == 'online':
                tws_conn.placeOrder(parent_order_id, symcontract, fadedentryorder1)
                tws_conn.placeOrder(parent_order_id+1, symcontract, bracketorder1)
                
                tws_conn.placeOrder(parent_order_id+2, symcontract, fadedentryorder2)
                tws_conn.placeOrder(parent_order_id+3, symcontract, bracketorder2)
                
                sleep(1)
                tws_conn.placeOrder(parent_order_id, symcontract, mktentryorder1)
                tws_conn.placeOrder(parent_order_id+2, symcontract, mktentryorder2)
                
                tws_conn.orderStatus(parent_order_id)
                tws_conn.orderStatus(parent_order_id+2)
                
                entryordsstatus_dict[parent_order_id] = 'openstatus'
                entryordside_dict[parent_order_id] = tside #{}
                entryordsym_dict[parent_order_id] =  sym #{}
                
                entryordsstatus_dict[parent_order_id+1] = 'openstatus'
                entryordside_dict[parent_order_id+1] = tside #{}
                entryordsym_dict[parent_order_id+1] =  sym #{}
                
                get_orderid() ### simply asks the reply file for next valid number [not read here]
            if os.path.isfile(siglistfile):
                shutil.copyfile(siglistfile, 'temp')
                os.remove(siglistfile)
            ##########  end of if clause sig file changed
print 'finished ',loopmax,' loops  by Signal Creator...dead since..'
print 'disconnecting.. done..'
if online == 'online':
    tws_conn.disconnect()
