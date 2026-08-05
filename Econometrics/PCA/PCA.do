****************************************************
* Principal Component Analysis in Stata 19
* Dataset: 1978 Automobile Data
****************************************************

clear all
set more off
version 19

* 1. Load dataset
webuse auto, clear

* 2. Inspect the dataset
describe
summarize price mpg rep78 headroom weight length displacement

* 3. Check missing values
misstable summarize price mpg rep78 headroom weight length displacement

* 4. Keep only complete observations for selected variables
drop if missing(price, mpg, rep78, headroom, weight, length, displacement)

* 5. Check correlation matrix
correlate price mpg rep78 headroom weight length displacement

* 6. Run PCA
pca price mpg rep78 headroom weight length displacement

* 7. Scree plot: helps decide how many components to keep
screeplot

* 8. Run PCA keeping first two components
pca price mpg rep78 headroom weight length displacement, components(2)

* 9. Display component loadings
estat loadings

* Optional: Display cleaner loadings by hiding small values
* estat loadings, blanks(.30)

* 10. Generate component scores
predict pc1 pc2, score

* 11. Check that components are uncorrelated
correlate pc1 pc2

* 12. Scatter plot of the first two principal components
scatter pc2 pc1, ///
    title("PCA Score Plot") ///
    xtitle("Principal Component 1") ///
    ytitle("Principal Component 2")

* 13. Optional: use PC1 as an index
summarize pc1 pc2
list make price mpg weight length displacement pc1 pc2 in 1/10
