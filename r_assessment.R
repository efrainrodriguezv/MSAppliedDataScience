# Function fibseq(n)

fibseq <- function(n) {
    
   fib <- c()
   
   if (n == 1) return(1)
   if (n == 2) return(c(1, 1))

   fib[1] <- 1 
   fib[2] <- 1

   for (k in 3:n) {
    fib[k] <- fib[k - 1] + fib[k - 2]               
   }
  
   return(as.integer(fib))

}

elcheck <- function(x, y) {
  
  x[is.na(x)] <- 0
  y[is.na(y)] <- 0                             
                           
  lst <- list(x, y) 
  max <- max(lengths(lst)) 

  x_reshaped <- rep(x, length.out = max) 
  y_reshaped <- rep(y, length.out = max)
  
  eq <- integer(length(x_reshaped)) 
  
  for (i in seq_along(x)) {
    if (is.na(x_reshaped[i]) || is.na(y_reshaped[i])) {
      eq[i] <- as.integer(identical(x_reshaped[i], y_reshaped[i]))
    } else {
      eq[i] <- as.integer(x_reshaped[i] == y_reshaped[i])
    }
  }
  return(eq)
}

topingredients <- function(recipes)  {
  
  df <- read.csv(filename, stringsAsFactors = FALSE)
  ings <- unlist(strsplit(df$ingredients, ", "))
  ings <- tolower(trimws(ings))
  tab <- sort(table(ings), decreasing = TRUE)
  data.frame(
    name  = names(tab)[1:3],
    count = as.integer(tab[1:3]),
    row.names = NULL
  )
}
