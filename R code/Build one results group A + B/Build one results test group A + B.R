y <-values <- c(24, 23)                                                          ##### Assigned Values

group <- LETTERS[1:2]                                                            ##### Prints 'A' and 'B'
x<-barplot(values, names.arg = group, ylim=c(0,54), space = 0.5, width = 0.4, xlim=c(0, 2), col = rainbow(2)) ##### Barplot
text(x,y+2,labels=as.character(y))                                               ##### Text above bars

legend("topright",                                                               ##### Legend/Key
       legend = c("Test Group A", "Test Group B"),
       fill = c("#ff0000", "#00ffff"))

#####a <- c (0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3)               ##### Box Plot 
#####b <- c (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3)               ##### Box Plot

#####boxplot(a, b, horizontal = TRUE)                                            ##### Box Plot

t.test(a, b, paired = TRUE, alternative = "two.sided")                           ##### Paired T Test
