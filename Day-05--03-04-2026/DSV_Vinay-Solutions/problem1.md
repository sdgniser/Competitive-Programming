## 3 April

- First point to observe is that we can always get all zeros in two steps; take the mex of the whole set, if 0 zero is present then the resulting array will have all elements non zero and if 0 is not present then we are done. When we take the mex of a set which has no 0s we get 0.
- If all are 0s then we are done in 0 steps
- If all are non zero then we are done in 1 step
- Now consider the case there are some zeros in the array and some non zero elements, there is still a possibility of being done in 1 step. That is if we can partition the arrray into segments such that only one is not all zeroes and that subarray has no zeros. This only occurs when the array looks like: 000..xxxxx or xxxxx0000.. or 0000..xxxxx..0000 where x are all non zero( need not be same ). If the zeros are not present only at the ends contigiously we need a total of 2 steps.


