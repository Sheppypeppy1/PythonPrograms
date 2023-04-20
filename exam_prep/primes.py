def calculate_number_of_primes_in_range():
    prime_count = 0
    for i in range(4,25):
        #Assumes i is prime until factor is found that disproves
        i_prime = True
        #Loop through possible factors
        for x in range(2,i):
            #Check if factor
            if (i%x)==0:
                i_prime=False
                #If factor then not prime so exit loop for current i
                break
        if i_prime:
            prime_count += 1
    return prime_count