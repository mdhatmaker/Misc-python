forecast_results <- function(res)
{
  return (res$mean)
}

fourier <- function(t,terms,period)
{
  print (terms)
  n <- length(t)
  X <- matrix(,nrow=n,ncol=2*terms)
  for(i in 1:terms)
  {
    X[,2*i-1] <- sin(2*pi*i*t/period)
    X[,2*i] <- cos(2*pi*i*t/period)
  }
  colnames(X) <- paste(c("S","C"),rep(1:terms,rep(2,terms)),sep="")
  return(X)
}

library(forecast)

yy <- read.table ("garan.dat", header=T)
y <- yy[,'price']

n <- length(y)
print (n)
m <- 10 # how many points in the future
terms = 4

fit <- Arima(y, order=c(2,0,1), xreg=fourier(1:n,terms,m))

f = forecast(fit, h=2*m, xreg=fourier(n+1:(2*m),terms,m))

print (forecast_results(f))

plot(f)
