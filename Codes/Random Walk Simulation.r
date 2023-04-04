
# Random Walk Simulation of a Markov Chain with the given transition matrix
sample_space <- c(1, 2, 3, 4, 5)
col1 <- c(0.47, 0.2, 0.3, 0, 0)
col2 <- c(0.1, 0.32, 0.2, 0, 0)
col3 <- c(0.16, 0.2, 0.38, 0, 0)
col4 <- c(0.01, 0.22, 0.05, 1, 0)
col5 <- c(0.26, 0.06, 0.07, 0, 1)
p_matrix <- matrix(c(col1, col2, col3, col4, col5), nrow = 5, ncol = 5)
current_state <- 1
process_states <- c(current_state)
steps <- 350

# - Returns the final state achieved after n steps.                                                                              # nolint
find_final_state <- function(sample_space, p_matrix, current_state, steps, process_states) {                                     # nolint
    steps <- steps - 1
    for (i in 1:steps) {
        if (current_state == 1) {
            next_state <- sample(x = sample_space, size = 1, replace=TRUE, prob = c(p_matrix[1],                                 # nolint
            p_matrix[6], p_matrix[11], p_matrix[16], p_matrix[21]))                                                              # nolint
        } else if (current_state == 2) {
            next_state <- sample(x = sample_space, size = 1, replace=TRUE, prob = c(p_matrix[2],                                 # nolint
            p_matrix[7], p_matrix[12], p_matrix[17], p_matrix[22]))                                                              # nolint
        } else if (current_state == 3) {
            next_state <- sample(x = sample_space, size = 1, replace=TRUE, prob = c(p_matrix[3],                                 # nolint
            p_matrix[8], p_matrix[13], p_matrix[18], p_matrix[23]))                                                              # nolint
        } else if (current_state == 4) {
            return (4)
        } else if (current_state == 5) {
            return (5)
        }

        if (current_state != next_state) {
            current_state <- next_state
            process_states <- append(process_states, current_state)
        }
        else {                                                                                                                   # nolint
            process_states <- append(process_states, current_state)
        }
    }
    return (process_states)                                                                                                      # nolint
}

# setting initial values
no_of_bad_loans <- 0
no_of_paid_up_loans <- 0
simulations <- 10000

# plotting simulation
simulations <- simulations - 1
for (i in 1:simulations) {
    process_states <- find_final_state(sample_space, p_matrix, current_state, steps, process_states)                              # nolint
    if (process_states == 4) {
        no_of_bad_loans <- no_of_bad_loans + 1
    } else if (process_states == 5) {
        no_of_paid_up_loans <- no_of_paid_up_loans + 1
    }
}
simulations <- simulations + 1
prob_paid_up_loan <- no_of_paid_up_loans / simulations
prob_bad_loan <- no_of_bad_loans / simulations
prob <- c(prob_paid_up_loan, prob_bad_loan)
print(prob_paid_up_loan)
print(prob_bad_loan)

# barchart with added parameters
print("Sum is-")
print(prob_bad_loan + prob_paid_up_loan)
barplot(prob, main = "Random Walk Simulation with n=10000", xlab = "Initial  State: Good Loan",                                     # nolint
ylab = "Probabilities", ylim = c(0, 1), names.arg = c("Paid Up Loan", "Bad Loan"), col = "darkred")                               # nolint


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

# for (i in 11:20) {
#     multiplication_matrix <- multiplication_matrix %*% p_matrix
# }
# print("P20-")
# print(multiplication_matrix)

# for (i in 21:50) {
#     multiplication_matrix <- multiplication_matrix %*% p_matrix
# }
# print("P50-")
# print(multiplication_matrix)
