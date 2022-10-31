* Stata Textbook Examples
* Introductory Econometrics: A Modern Approach by Jeffrey M. Wooldridge (1st & 2nd eds.)
* Chapter 13 - Pooling Cross Sections Across Time. Simple Panel Data Methods


* Example 13.1: Woman's Fertility Over Time

use http://fmwww.bc.edu/ec-p/data/wooldridge/fertil1
reg kids educ age agesq black east northcen west farm othrural town smcity y74 y76 y78 y80 y82 y84
test y74 y76 y78 y80 y82 y84

* Example 13.2: Changes in the Return to Education and the Gender Wage Gap
use http://fmwww.bc.edu/ec-p/data/wooldridge/cps78_85
reg lwage y85 educ y85educ exper expersq union female y85fem

* Example 13.3: Effect of a Garbage Incinerator's Location on Housing Prices
use http://fmwww.bc.edu/ec-p/data/wooldridge/kielmc
reg rprice nearinc if year==1981

scalar b1=_b[nearinc]
reg rprice nearinc if year==1978

scalar b2=_b[nearinc]
* The difference in two coefficients on nearinc
display b1-b2

reg rprice nearinc y81 y81nrinc

reg rprice nearinc y81 y81nrinc age agesq

reg rprice nearinc y81 y81nrinc age agesq intst land area rooms baths

reg lprice nearinc y81 y81nrinc

* Example 13.4: Effect of Worker Compensation laws on Duration
use http://fmwww.bc.edu/ec-p/data/wooldridge/injury
reg ldurat afchnge highearn afhigh if ky

* Example 13.5: Sleeping Versus Working
use http://fmwww.bc.edu/ec-p/data/wooldridge/slp75_81
reg cslpnap ctotwrk ceduc cmarr cyngkid cgdhlth

test ceduc cmarr cyngkid cgdhlth

* Example 13.6: Distributed Lag of Crime Rate on Clear-up Rate
use http://fmwww.bc.edu/ec-p/data/wooldridge/crime3
reg clcrime cclrprc1 cclrprc2

* Example 13.7: Effect of Drunk Driving Laws on Traffic Fatalities
use http://fmwww.bc.edu/ec-p/data/wooldridge/traffic1
reg cdthrte copen cadmn

* Example 13.8: Effect of Enterprise Zones on Unemployment Claims
use http://fmwww.bc.edu/ec-p/data/wooldridge/ezunem
reg guclms d82 d83 d84 d85 d86 d87 d88 cez

bpagan d82 d83 d84 d85 d86 d87 d88 cez

* Example 13.9: Country Crime Rates in North Carolina
use http://fmwww.bc.edu/ec-p/data/wooldridge/crime4
reg clcrmrte d83 d84 d85 d86 d87 clprbarr clprbcon clprbpri clavgsen clpolpc

whitetst, fitted
