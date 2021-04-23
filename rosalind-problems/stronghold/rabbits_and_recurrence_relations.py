# Problem http://rosalind.info/problems/fib/

'''
A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2‾√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent the n-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if Fn
represents the number of rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. 
This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40and k≤5. 


Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

** Notes **
n = months and 
k = number of rabbit pairs
'''

# recursive solution from https://medium.com/algorithms-for-life/rosalind-walkthrough-rabbits-and-recurrence-relations-4812c0c2ddb3


def rabbit_pairs(num_months, num_offspring):
    if num_months == 1:
        return 1
    elif num_months == 2:
        return num_offspring

    one_gen = rabbit_pairs(num_months - 1, num_offspring)
    two_gen = rabbit_pairs(num_months - 2, num_offspring)

    if num_months <= 4:
        return one_gen + two_gen

    return (one_gen + (two_gen * num_offspring))


# print(rabbit_pairs(29, 2))


def pythonic_rabbit_pairs(months, offspring):
    parent, child = 1, 1
    for _ in range(months - 1):
        child, parent = parent, parent + (child * offspring)
    return child

print(pythonic_rabbit_pairs(35, 5))
'''
o - children have to mature and reproduce the next cycle only
O - parent can reproduce and move to the next cycle

Month 1: [o]
Month 2: [O]
Month 3: [O o o]
Month 4: [O o o O o o O o o ]
Month 5: [O o o O O Ooo Ooo ]
month 6: []
'''