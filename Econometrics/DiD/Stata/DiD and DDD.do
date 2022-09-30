clear all

use https://www.stata-press.com/data/r17/hospdd

didregress (satis) (procedure), group(hospital) time(month)

estat trendplots 

estat ptrends

estat granger

**** DDD ****

generate hightrt = procedure==1 & (frequency==3 | frequency==4)
label define trt 0 "Untreated" 1 "Treated"
label values hightrt trt

didregress (satis) (hightrt), group(hospital frequency) time(month)


* The above experiments should tell us about DiD and DDD for now (2022 09 30)



clear all

use https://www.stata-press.com/data/r17/patents
xtset classid

xtdidregress (uspatents fpatents) (gotpatent), group(classid) time(year)





clear all

use https://www.stata-press.com/data/r17/parallelt

xtset id1

xtdidregress (y1 c.x1##c.x2) (treated1), group(id1) time(t1)

estat trendplots

estat ptrends

estat granger




xtset id2

xtdidregress (y2 c.z1##c.z2) (treated2), group(id2) time(t2)

estat trendplots

estat ptrends

estat granger


xtset id3

xtdidregress (y3 c.w1##c.w2) (treated3), group(id3) time(t3)

estat trendplots

estat ptrends

estat granger






clear all

use https://www.stata-press.com/data/r17/hospdd

didregress (satis) (procedure), group(hospital) time(month)

estat grangerplot

estat grangerplot, nodraw verbose

estat grangerplot, nodraw verbose nleads(1) nlags(0)

estat grangerplot, nodraw verbose post nlags(0)

quietly didregress (satis) (procedure), group(hospital) time(month)
estat granger







