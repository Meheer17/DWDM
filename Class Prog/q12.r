diabetest1 <- read_excel("C:/Users/M.Geetha/Downloads/NARA.xlsx")
A <- diabetest1$Age
Mean <- mean(A)
Std <- sd(A)
Zscore <- (A - Mean) / Std
Zscore