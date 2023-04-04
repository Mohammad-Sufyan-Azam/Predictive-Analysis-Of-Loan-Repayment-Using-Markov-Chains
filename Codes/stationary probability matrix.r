# # (b) Verifying it with calculating pow(A, n).                                                                                    # nolint
col1 <- c(0.47, 0.2, 0.3, 0, 0)
col2 <- c(0.1, 0.32, 0.2, 0, 0)
col3 <- c(0.16, 0.2, 0.38, 0, 0)
col4 <- c(0.01, 0.22, 0.05, 1, 0)
col5 <- c(0.26, 0.06, 0.07, 0, 1)
p_matrix <- matrix(c(col1, col2, col3, col4, col5), nrow = 5, ncol = 5)
multiplication_matrix <- diag(5)

for (i in 1:10000) {
    multiplication_matrix <- multiplication_matrix %*% p_matrix
}
print("P10000-")
print(multiplication_matrix)
