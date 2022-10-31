* Stata Textbook Examples
* Introductory Econometrics: A Modern Approach by Jeffrey M. Wooldridge (1st & 2nd eds.)
* Chapter 7 - Multiple Regression Analysis with Qualitative Information: Binary (or Dummy) Variables
clear all
ssc install bcuse
* http://fmwww.bc.edu/ec-p/data/wooldridge/datasets.list.html

* Example 7.1: Hourly Wage Equation
* use http://fmwww.bc.edu/ec-p/data/wooldridge/wage1
bcuse wage1
reg wage female educ exper tenure

reg wage female

* comparison of means test
* https://www.stata.com/manuals13/rttest.pdf
ttest wage, by(female)

*Average wage for women
lincom female+_cons


* Example 7.2: Effects of Computer Ownership on College GPA
use http://fmwww.bc.edu/ec-p/data/wooldridge/gpa1
reg colGPA PC hsGPA ACT
reg colGPA PC

* Example 7.3: Effects of Training Grants on Hours of Training in 1988
use http://fmwww.bc.edu/ec-p/data/wooldridge/jtrain
reg hrsemp grant lsales lemploy if year==1988

* to see avg number of training hours and min max
sum hrsemp if year  == 1988

* Example 7.4: Housing Price Regression
use http://fmwww.bc.edu/ec-p/data/wooldridge/hprice1
reg lprice llotsize lsqrft bdrms colonial

* Example 7.5: Log Hourly Wage Equation
use http://fmwww.bc.edu/ec-p/data/wooldridge/wage1
reg lwage female educ exper expersq tenure tenursq

* Difference between woman's and man's wage
di exp(_b[female]*1)-1


* Example 7.6: Log Hourly Wage Equation
use http://fmwww.bc.edu/ec-p/data/wooldridge/wage1
gen male = (!female)
gen single = (~married)
gen marrmale = (married & ~female)
gen marrfem = (married & female)
gen singfem = (female & ~married)
gen singmale = (~female & ~married)
reg lwage marrmale marrfem singfem educ exper expersq tenure tenursq

* Difference in lwage between married and single women
lincom singfem-marrfem
reg lwage marrmale singmale singfem educ exper expersq tenure tenursq

* Example 7.8: Effects of Law School Rankings on Starting Salaries
clear
use http://fmwww.bc.edu/ec-p/data/wooldridge/lawsch85
gen r61_100 = (rank>60 & rank<101)

* dividing the rank into different categories
reg lsalary top10 r11_25 r26_40 r41_60 r61_100 LSAT GPA llibvol lcost

* Difference in starting wage between top 10 below 100 school
di exp([top10]*1)-1
reg lsalary rank LSAT GPA llibvol lcost


* Example 7.10: Log Hourly Wage Equation (Compare it to Ex 7.6)
clear
use http://fmwww.bc.edu/ec-p/data/wooldridge/wage1
gen femed = female*educ
reg lwage female educ femed exper expersq tenure tenursq

reg lwage female educ exper expersq tenure tenursq

* Example 7.11: Effects of Race on Baseball Player Salaries
clear 
use http://fmwww.bc.edu/ec-p/data/wooldridge/mlb1
reg lsalary years gamesyr bavg hrunsyr rbisyr runsyr fldperc allstar black hispan blckpb hispph

* Difference in lwage between black and white in cities with 10% of blacks
lincom _b[black]+_b[blckpb]*10

* Difference in lwage between black and white in cities with 20% of blacks
lincom _b[black]+_b[blckpb]*20

* City percentage of hispanic people when wages of hispanic and whites are equal
di _b[hispan]*-1/_b[hispph]


* Example 7.12: A Linear Probability Model of Arrests
use http://fmwww.bc.edu/ec-p/data/wooldridge/crime1
gen arr86=(~narr86)
reg arr86 pcnv avgsen tottime ptime86 qemp86


* Change in probability of arrest if pcnv increases by .5
lincom _b[pcnv]*.5

* Change in probability of arrest if ptime86 increases by 6
lincom _b[ptime86]*6

* Change in probability of arrest if ptime86 decreases by 12
lincom _b[_cons]- _b[ptime86]*12

* Change in probability of arrest if qemp86 increases by 4
lincom _b[qemp86]*4

reg arr86 pcnv avgsen tottime ptime86 qemp86 black hispan


* This page prepared by Oleksandr Talavera (revised 8 Nov 2002)
* Send your questions/comments/suggestions to Kit Baum at baum@bc.edu
* These pages are maintained by the Faculty Micro Resource Center's GSA Program,
* a unit of Boston College Academic Technology Services
