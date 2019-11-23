# stock-prices-exercise

##Requirements,
python3, pip, virtualenv

##Usage: 
./tests.sh is intended to be run in a CI workflow, can be executed locally
./run.sh demonstrates it's execution with some mock data.

This is a simple exercise to calculate the highest profitable trade in a day based on stock prices in a per minute interval

Tests could have been extended by ensuring that the method only calculated buy/sale intervals after the reference index posiiton.

Thought about using a python library more focused on finding the "minima and maxima" values, but decided the complexity would increase too much and the code would be less readable for little value.
