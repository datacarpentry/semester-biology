Debugging with a Debugger
=========================

Break points
------------
1. Insert breakpoint
2. Press Debug
3. Program runs until breakpoint and stops (before executing the line of code)
4. Stack Data gives the current values for all variables (Local vs. Global)
5. Pressing Debug again continues to the next breakpoint

Why
---
* Like a print statement but better
* Doesn't accidentally get left in the code
* Contains a complete snapshot of the status of the program
* Let's you walk through the code dynamically

Stepping
--------
* Step Into – goes line by line through the code including entering functions
* Step Over – does not enter functions
* Step Out – leaves the current function and return to whatever called it

Conditional breakpoints (Pro and other debuggers)
------------------------------------------
* Breakpoints can be made conditional
* Only stop the program if certain conditions are met
* Right click the breakpoint and add condition

Example
-------

    """Exponential growth debugging example"""
    
    def get_pop_size_at_t(init_pop_size, reprod_rate, time_of_sample):
	n = init_pop_size
	for t in range(1, time_of_sample + 1):
	    n_tplus1 = n + reprod_rate * n
	    n = n_tplus1
	return n_tplus1
    
    def doubling_time_exponential_growth(reprod_rate, init_pop_size):
	n = init_pop_size
	t = 0
	while n < 2 * init_pop_size:
	    n = n + reprod_rate * n
	    t += 1
	return t
    
    #Problem 2
    print get_pop_size_at_t(10, 0.152, 10)
    print get_pop_size_at_t(10, 0.152, 50)
    print get_pop_size_at_t(10, 0.152, 100)
    
    #Problem 3
    print doubling_time_exponential_growth(0.0001, 1000)
    print doubling_time_exponential_growth(0.005, 1000)
    print doubling_time_exponential_growth(0.21, 1000)