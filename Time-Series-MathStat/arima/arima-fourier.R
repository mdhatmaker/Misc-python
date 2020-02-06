n <- 2000
m <- 200
y <- ts(rnorm(n) + (1:n)%%100/30, f=m)
print (y)
quit()
fourier <- function(t,terms,period)
{
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
fit <- Arima(y, order=c(2,0,1), xreg=fourier(1:n,4,m))
f = forecast(fit, h=2*m, xreg=fourier(n+1:(2*m),4,m))
plot(f)

print (y)
print (f)
