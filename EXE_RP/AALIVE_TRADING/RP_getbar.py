################################
import os, sys, importlib,glob, csv, subprocess, datetime, shutil, time
from time import sleep, strftime, localtime
from datetime import datetime
titleself = (os.path.basename(__file__)).replace('.pyc','')
print titleself
###########
localtag = '_RP'
sys.path[0:0] = [((os.getcwd().replace('EXE','|')).split('|'))[0] + 'EXE' +localtag]
#########################################
import ENVdicts,rpu_rp 
nd ={}
nd = ENVdicts.ENVdicts(localtag)

for var in nd.keys():
##    print var
    locals()[var] = nd[var]
##################
global timedate_format, nextorderID, date, today,recentlimit, time_format,sym, symbol_list, symdict
moduleNames = open('importmodlist.txt').readlines()
for module in moduleNames:
    modulestripped = module.strip()
    if modulestripped != titleself:
##        print '...',modulestripped,'xxx',titleself
        my_module = importlib.import_module(modulestripped)
        pass
    else:
        print 'is self'
######################
import Mod_TicksUtile
######################
sym = 'ES'
date =  today  ######## <<<<<<<
print '1 : ES \n2 : FDAX'
symnum = '1' #raw_input('sym: ')
if symnum == '1':
    sym = 'ES'
else:
    sym = 'FDAX'
for ind in indlist_oscils:
    dur = '5mins'
teststr = 'grnNnotailNbigbar' #'2016-02-19 21:'
closestr = 'grnNnotailN'
pos = netcost = 0
####################
global recentlimit, time_format,today,timedate_format, nextorderID
from time import sleep, strftime, localtime
import ctypes
date = yesterday
#####################3
##########    pivot = Mod_Mod_rpInd.gatherline(sym,'pivot')
##########    R1 = Mod_Mod_rpInd.gatherline(sym,'R1')
##########    S1 = Mod_Mod_rpInd.gatherline(sym,'S1')
##########    print S1,R1,pivot
    ##do the same for weekly by adding dur to variables and create a weekly  from dailys..
##    find pivots, find fibbo retraces on recnt moves[rangebars,hi,lo]
##    read spots from file
##    calculate two roundies
##    calculate 10 handles off high of day,lowday,openday,yestclose,prevhourhilow
#############################################
print '   '
sym = 'ES'      
###############
def create_roundies(sym):
    curprice = 2100 #need to read froma bar ranger
##    take curr price
##    factor = price / 100
##    using factor, calculate 3 roundies up and 3 down
##    write them to roundie file
##    create combined lines file with adding lines to roundies
####################
tag_listall = tagsdict.values()
tag_list = []
for a in tag_listall:
    f = 'absent'
    c=0
    while c < len(tag_list):
        if a == tag_list[c]:
            f = 'found'
        c+=1
    if f == 'absent':
        tag_list.append(a)
##tag_list = ['RTH','LastHour']
print todaydash
bla =str(todaydash)
def get_info(date):
    todayhyphen = rpu_rp.todaysdatehypens(date)
##    Mod_Mod_Mod_Mod_RP_Snapshot.snapshot_sym(sym,date,['5mins']) ## need this to create good both bars ## 
    btime = '15:30:0'
    Mod_RP_Snapshot.show_one_bar('ES','1min',btime,date)
    ###############
    ############
    regionlist = ['USA','EUROPE','ASIA']
    for r in regionlist:
        for tag in tag_list:
            ctag = r+tag
            startbartime = tagsstartdict[ctag]
            endbartime = tagsenddict[ctag]
##            print r,tag,ctag,startbartime,endbartime
            rangehilos = BarUtiles.show_hi_lo_bar_range(sym,'5mins',startbartime,endbartime,date)
            LOW = rangehilos[0]
            HIGH = rangehilos[1]
            HIGHTIME = rangehilos[3].replace(bla,'')
            LOWTIME = rangehilos[2].replace(bla,'')
            CLOSE = rangehilos[4]
            OPEN = rangehilos[6] ## closetime is in 5
            print('%8s %8s %8s %8s %8s %8s %8s %8s %8s %8s' % (r,tag,LOW,HIGH,CLOSE,LOWTIME,HIGHTIME,startbartime,endbartime,OPEN))
#####################

######################
def scan_bars_for_tag(bars,price,sym,start,end,date):
    bars = Mod_Mod_Mod_Mod_RP_Snapshot.show_bar_range(sym,'5mins',start,end,date)
    for bar in bars:
        print bar
        ## check if line price has been tagged
#############################
def detect_sliceDice(lineprice,start,end):
    bars = Mod_Mod_Mod_Mod_RP_Snapshot.show_bar_range(sym,'5mins',start,end,date)

    startprice = float(head(bars)[6])
    if startprice <  lineprice :
        position = 'below'
        pass
    else:
        position = 'above'
        pass
    sflag = 'untagged'
    for bar in bars:
        currprice = bar[6]
        if position == 'below':
            if currprice > lineprice:
                sflag='firsttag'
                pass
            if sflag == 'firsttag':
                pass
######################
def OBV(date,sym):
##    bars = Mod_Mod_Mod_Mod_RP_Snapshot.show_bar_range(sym,'5mins',start,end,date)
    ticks = bars
######bs = [1,2,6,6,5,6,7,8,9]
######bshighs = [1,2,13,4,5,6,7,8,9]
######bslows = [1,2,3,4,5,5,5,5,5]
######
######scanvalue = 3
######stochval2 = 3            
######def StochD(Kpercarray,emaval):
######    Dpercarray =  EMAmvavgToArray(Kpercarray,emaval)
######    return Dpercarray
#################################
def find_swing_points(sym,barsize,start,end,mode,threefive):
    tag = mode
    if mode == 'CLOSEPRICE ':
        highnum = 5
        lownum = 5
        pass
    else:
        highnum = 3
        lownum = 4
    import Mod_Mod_Mod_Mod_RP_Snapshot
    barsdaily =[]
    bars = Mod_Mod_Mod_Mod_RP_Snapshot.show_bar_range(sym,barsize,start,end,date)
    prevhigh = 0.0
    prevlow = 9999
    prevprevlow = 9999
    prevprevhigh = 1
    prevtime = prevprevtime = ''
    c=0
    lenbars = len(bars)
    tailamt = 20
    minbars = lenbars - tailamt
    for bar in bars:
        stag =''
        c+=1
        if c==1:
            prevbar = prevprevbar = bar
##        print bar
        #compare highs
        high = float(bar[highnum])
        low = float(bar[lownum])
        time = bar[1]
##        print prevprevhigh,prevhigh,high
        if prevprevhigh < prevhigh and  prevhigh > high:
            stag = 'swingHIGH '+tag + str(prevhigh)
##            print prevhigh, prevtime, 'swinghigh',tag
        if prevprevlow > prevlow and  prevlow < low:
##            print prevlow, prevtime, 'swinglow', tag
            stag = 'swingLOW '+tag + str(prevlow)
##        print bar,'now'
        if c > minbars:
            print prevbar,stag #,high,prevhigh,prevprevhigh
        prevprevhigh = prevhigh
        prevhigh = high
        prevprevlow = prevlow
        prevlow = low
        prevprevtime = prevtime
        prevtime = time
        
        prevbar = bar
        prevprevbar = prevbar
        
###################################
def find_swing_points5(sym,barsize,start,end,mode,threefive):
    tag = mode
    if mode == 'CLOSEPRICE ':
        highnum = 5
        lownum = 5
        pass
    else:
        highnum = 3
        lownum = 4
    import Mod_Mod_Mod_Mod_RP_Snapshot
    barsdaily =[]
    bars = Mod_Mod_Mod_Mod_RP_Snapshot.show_bar_range(sym,barsize,start,end,date)
    b1low = b2low = b3low =  b4low = 9999
    b1high = b2high =  b3high = b4high  = 0
    b1time = b2time =  b3time = b4time  = ''
    c=0
    lenbars = len(bars)
    tailamt = 2000
    minbars = lenbars - tailamt
    for bar in bars:
        stag =''
        c+=1
        if c==1:
            b1bar = b2bar = b3bar = b4bar = bar
        high = float(bar[highnum])
        low = float(bar[lownum])
        time = bar[1]
##        print prevprevhigh,prevhigh,high
        if b3high > high and  b3high > b1high and b3high > b2high and b3high > b4high:
            stag = 'swingHIGH '+tag + str(b3high)
        if b3low < low and  b3low < b1low and b3low < b2low and b3low < b4low:
            stag = 'swingLOW '+tag + str(b3low)
##        print bar,'now'
        if c > minbars:
            print b3bar,stag #,high,prevhigh,prevprevhigh
        b4high = b3high
        b3high = b2high
        b2high = b1high
        b1high = high
        
        b4low = b3low
        b3low = b2low
        b2low = b1low
        b1low = low
        
        b4time =b3time
        b3time = b2time
        b2time =b1time
        b1time =time
    
        b4bar = b3bar
        b3bar = b2bar
        b2bar = b1bar
        b1bar = bar      
###################################  
'''##########################                
######detect_sliceDice(lineprice,start,end)
first pass did not bounce 4 ticks, went 6 ticks [noise] beyond before bounce or retag
bar low v kupper, barhi vs klower, barage, older the worse? what is max?
##########raw_input('click')
####thrust and slope of current bar
## averages of:
# of sigs per period
# average distance between
is it a cross or a bounce....one touch and threw...1st pass, 2nd pass, thru
identify wedges...50/50 chance

stop distances...3x for bigger moves
grab trade data from action forex
use action forex for wide lines 4hour
def create_report(Sigfile,sym,barsize):
    print barsize,sym,'number bars studied=',numberBars,numsigs,'=numsigs'
    print 'if i am 20 bars old in signal, start with trail stop depends on dur...shotrt dur = short age'
##    average number of sigs in 30 bars  has it flipped alot
##    test the ticker perfomance by time delta
##    avg number of ticks should be cycle time...if not issue a warning
##    avg number of bars per hour should match duration/hour
#########
############
####def slice_dice_dectector(sym,date,starttime,endtime,spotline,direction):
####    for bar in rangebars:
####if direction == 'up':
#### firsttouch = if spotline is breached...5sec bar is lowhigh on spot
####    tagstatus = 'touched'
####    if tagstatus =='touched, look for next touch...withing
###   after first touch, should move back minimum 1 point...BEFORE moving 2.75 handleif spotlineStatus1tou
####################
def linetagger(spotline,sym):
    print spotline, 'checking if tagged in last 5 minutes'
    ## am i under or over line at start of 5 mins?...under
    ##diff to spotline = spotline - recentprice
    ## if diff < 0:  then status = tagged print status, spotline, curprice
    ## followthru amount ?
#########################
'''
#################################
def show_spots(sym,date,limit):
    curprice = float(Mod_TicksUtile.recenttick(sym,'recent'))
    spotfile = libarea + 'spotlines.' + sym+ '.csv'
    spotlines= rpu_rp.CsvToLines(spotfile)
    print limit, ' is limit'
    for l in spotlines:
        spotp = float(l[0])
        distance = abs(spotp-curprice)
        if (spotp-curprice) > 0:
            underover = 'under'
        else:
            underover = 'over'
        if distance < limit:
##            print curprice-spotp,spotp,curprice,sym,'spot prices',limit
            if underover == 'under':
                print 'ready to SELL at ',spotp, 'how manypasses?',curprice,sym,distance
            else:
                print 'ready TO BUY at ',spotp, 'how manypasses?',curprice,sym,distance
#####################
def show_bar8_range(start,end,sym,date):
    print 'this is the bar8 range of lines',start,end
    after5lines = Mod_Mod_Mod_Mod_RP_Snapshot.show_bar_range(sym,'5mins',start,end,date)
    linecount =0
    trigger = 'inactive'
    for line in after5lines:
        bartime = line[1]
        linecount +=1
##        print line
        if linecount ==1:
            starthi = line[3]
            startlo = line[4]
            print '>>>> BAR 8 HILO = <<<<<', starthi, startlo, bartime
            pass
        curbarhi = line[3]
        curbarlo = line[4]
        if curbarhi < startlo and trigger != 'active':
            print 'going down',line
            trigger = 'active'
        elif curbarlo > starthi and trigger != 'active':
            print 'going up',line
            trigger = 'active'
        else:
            pass
    print '======================'
##############################
def run_8s(sym): 
    if sym == 'ES' and 'bla' == 'bla':
##        show_bar8_range('04:00:00','7:00:00',sym,date) #asia
        show_bar8_range('09:30:00','12:25:00',sym,date) #europe
        show_bar8_range('16:00:10','18:25:00',sym,date) #usa
###############################
def getslices(sym,barsize,start,end,date,slicesize):
    import Mod_RP_Snapshot
    bars = Mod_RP_Snapshot.show_bar_range(sym,barsize,start,end,date)
    lenbars =len(bars)
    c=0
    while c < (lenbars - slicesize +1 ):
        slicebars = bars[c:c+slicesize]
        mode= 'CLOSEPRICE '
        find_swing_pointsnew(slicesize,slicebars,mode)
        c+=1
#########    
def find_swing_pointsnew(slicesize,slicebars,mode):
##    print len(slicebars)
    if mode == 'CLOSEPRICE ':
        highnum = 5
        lownum = 5
        pass
    else:
        highnum = 3
        lownum = 4
    c=0
    barnum =0
    slicehi = 0
    for bar in slicebars:   
        ##first, locate the hi lo
        barhigh = bar[highnum]
        barlow = bar[lownum]
        if barhigh > slicehi:
            slicehi = barhigh
            barnum = c
        c+=1
    ## now we have slicehi          
    ##make sure slice is not an endbar
    barhi = slicebars[barnum]
    bar1 = slicebars[0]
    barlast = slicebars[slicesize-1]
    if bar1[highnum] == slicehi or barlast[highnum] == slicehi:
        pass
##            print 'invalid swinghi'
    else:
        swinghibar = bar[barnum]
        print 'swhing hi',barhi
##################################       
factor = 10
proximitylimit = 9.0
sym = 'ES'
##run_8s(sym)
##show_spots(sym,date,proximitylimit)
barsize = '15mins'
barsize = '5mins'
##barsize = '1min'
##barsize = '1hour'
sym = 'ES'      
start = '01:00:05'
end   = '20:58:05'
slicesize = 3
getslices(sym,barsize,start,end,date,slicesize)
##find_swing_points(sym,barsize,start,end)
##find_swing_points(sym,barsize,start,end,'CLOSEPRICE ')
##find_swing_points5(sym,barsize,start,end,'HILOWS ','five')

######print 'low high close lowtime,hitime,startrange,endrange'
######get_info(date)


''' boll bands calculation
SMAval = 20
    SMAprice = price at SMAval
    Stdvariable = 0.382
    SMA H23 =AVERAGE(F4:F23)
    Upper Bollinger Band I23 = SMAprice + (std*Stdvariable)
    Lower Bollinger Band J23 = SMAprice - (std *Stdvariable)
    1. Work out the Mean (the simple average of the numbers)
2. Then for each number: subtract the Mean and square the result
3. Then work out the mean of those squared differences.
4. Take the square root of that and we are done!
The formula actually says all of that, and I will show you how.
mean = simpleaverage  of slice array at 20
diffmean = take each value - mean
sqdiffmean = diffmean *diffmean
meansqdiff = meanof sqdiffmeans
sqroot of meanssqdiffs
'''


