## April 1 2026

First point to notice is that y can either be greater than x by 1 or strictly lesser.
The only way to make digit sum of a number smaller is thorugh carry forward of digits. 

- If x>y then x-y> 0 and x> y-x as x>0 and y>0
- (x-y)mod(9) = -1 must hold true 
- say x-y = 9k -1, we can write x as: 999999{k times} and the rest as per need with the next digit after the k nines not being a nine. 
- When you add a 1 to above x you get the digit sum to be y 
