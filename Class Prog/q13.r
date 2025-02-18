diabetest1<-read_excel("C:/Users/M.Geetha/Downloads/NARA.xlsx")
A<-c(diabetest1$Age)
Mean<-mean(A)
Minimum<-min(diabetest1$Age)
Maximum<-max(diabetest1$Age)
MinMax<-(A-Minimum)/(Maximum-Minimum)
MinMax