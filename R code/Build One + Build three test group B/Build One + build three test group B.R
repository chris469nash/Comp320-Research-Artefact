y <-values <- c(23, 30)                                                          ##### Assigned Values

group <- LETTERS[1:2]                                                            ##### Prints 'A' and 'B'
x<-barplot(values, names.arg = group, ylim=c(0,54), space = 0.5, width = 0.4, xlim=c(0, 2), col = rainbow(2)) ##### Barplot
text(x,y+2,labels=as.character(y))                                               ##### Text above bars

legend("topright",                                                               ##### Legend/Key
       legend = c("A: Test Group B Build 1", "B: Test Group B Build 3"),
       fill = c("#ff0000", "#00ffff"))

#####a <- c (3, 1, 2, 3, 1, 0, 1, 1, 1, 1, 0, 1, 3, 2, 1, 0, 1, 1)               ##### Box Plot 
#####b <- c (2, 1, 1, 2, 1, 1, 3, 1, 2, 1, 2, 3, 2, 2, 1, 2, 1, 2)               ##### Box Plot

#####boxplot(a, b, horizontal = TRUE)                                            ##### Box Plot

t.test(a, b, paired = TRUE, alternative = "two.sided")                           ##### Paired T Test