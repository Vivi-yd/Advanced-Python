#Lambda, Map, Filter and Reduce
####Lambda -:
1. The format of declaring a lambda function is `f = lambda argument_list: expression`.

####Map -:
1. The map function combines a sequence with another function : `r = map(func, seq)`
2. It returns a new list with the elements changed by func.
3. An example for generation fifth power of numbers upto 10 is : `map(lambda x: x**5 , [j for j in range(1, 11)])`
4. map can be applied to more than one sequences, provided they are of same length.

####Filter -:
1. The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False.
2. This function will be applied to every element of the list l. Only if f returns True will the element of the list be included in the result list.

####Reduce -:
1. The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.
2. An example of finding sum of first 100 numbers using reduce : `num = reduce(lambda a,b: a+b, range(1, 101))`
