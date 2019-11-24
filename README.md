# stock-prices-exercise

##requirements,
python3, pip, virtualenv

##usage: 
./tests.sh is intended to be run in a CI workflow, can be executed locally
./run.sh demonstrates it's execution with some mock data.

##background
This is a simple exercise to calculate the highest profitable trade in a day based on stock prices in a per minute interval

Tests could have been extended by ensuring that the method only calculated buy/sale intervals after the reference index posiiton.

Thought about using a python library more focused on finding the "minima and maxima" values, but decided the complexity would increase too much and the code would be less readable for little value.

##assumptions and background
It was unclear with the brief how to handle a day with only loss-making opportunities, it indicated only that a trade should return the most profitable result, I chose to make the primary function pure and return both positive and negative results, with the executing method interpreting the result.
I regret the use of the negative rolling integer with -999999 for the profit variable, this is where python can be a little bit frustrating.