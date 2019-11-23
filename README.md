# stock-prices-exercise

This is a simple exercise to calculate the highest profitable trade in a day based on stock prices in a per minute interval

A sample tests.sh has been provided for easy local execution, as well as a buildkite file for a more robust example.
flake was used for linting and style formatting, and pytest for a really simple test.

Tests could have been extended by ensuring that the method only calculated buy/sale intervals after the reference index posiiton.

Thought about using a python library more focused on finding the "minima and maxima" values, but decided the complexity would increase too much and the code would be less readable for little value.