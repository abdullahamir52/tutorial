# To clear the environment in rstudio
Ctrl + Shift + F10
rm(list=ls())

# To clear the console
Ctrl + L

# To remove an object (factor, list, vector)
rm(object_name)

# To write a comment
Ctrl + Shift + C

# To run a selected section of lines
Ctrl + Enter

# To delete a file
unlink("some_file.csv")

# To delete another file
file.remove("some_other_file.csv")

# To delete a directory -- must add recursive = TRUE
unlink("some_directory", recursive = TRUE)

# Asking question about a function
?subset
# or
args(subset)

# To see the working directory
getwd()

# To change the directory
setwd("E:/GitHub Repositories/datasciencecoursera/Course 2 (R Programming)")

# To see the files in the directory
dir()

# To create a directory within the current working directory
dir.create("directory_name")

# To create a file within the directory
file.create("mytest.R")

# To rename a file
file.rename("mytest.R", "mytest2.R")

# to remove/delete a file
file.remove('mytest.R')

# Make a copy of "mytest2.R" called "mytest3.R" using file.copy().
file.copy("mytest2.R", "mytest3.R")

# to see the margins of the plot window
par("mar")

# to change the margins of the plot window
par(mar=c(1,1,1,1))

# to detach all user installed functions
detachAllPackages <- function() {
  basic.packages <- c("package:stats","package:graphics","package:grDevices","package:utils","package:datasets","package:methods","package:base")
  package.list <- search()[ifelse(unlist(gregexpr("package:",search()))==1,TRUE,FALSE)]
  package.list <- setdiff(package.list,basic.packages)
  if (length(package.list)>0)  for (package in package.list) detach(package, character.only=TRUE)
}
detachAllPackages()

