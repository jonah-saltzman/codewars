/* Challenge: A Narcissistic Number is a positive number which is the sum of its own digits, 
each raised to the power of the number of digits in a given base. In this Kata, we will 
restrict ourselves to decimal (base 10).

The Challenge:

Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

*/

//My solution

#include <stdbool.h>
#include <math.h>

//Function prototypes
bool narcissistic(int num);
int narc(int num, int base);
int digits(int num);

//Function takes an integer as input, and returns true if the integer is narcissistic, and false if it is not
bool narcissistic(int num)
  {
    //Call functions to count number of digits & calculate sum of digits raised to power equal to number of digits
    int base = digits(num);
    int result = narc(num, base);
    
    //Compare the result of narc(num) to 'num'; 'num' is narcissistic only if values are equal
    if (num == result)
      {
        return true;
      }
    else
      {
        return false;
      }
  }

//Function to sum each digit of 'num' raised to a power, where the power is equal to the number of digits in 'num'
int narc(int num, int base)
  {
    //Declare an array of floats with a number of elements equal to the number of digits in num
    float array[base];
  
    //Assign each digit of num to an element in 'array'
    for (int i = 0; i < base; i++)
      {
        array[i] = (num % 10) * 1.0;
        num = num / 10;
      }
    
    //Create variable for summing, and convert base to a float, for compatibility with pow()
    int sum = 0;
    float floatbase = (float)base;
    
    //For each element in 'array', raise it to the power of 'floatbase', and add it to the 'sum' variable
    for (int i = 0; i < base; i++)
      {
        sum = sum + (int)pow(array[i], floatbase);
      }
  
    //Return the final sum
    return sum;
  }

//Function to count the digits in 'num'
int digits(int num)
  {
    int dig = 0;
  
    //While 'num' is not equal to zero, increment 'dig' by one and divide 'num' by 10; once 'num' is zero (due to automatic flooring of ints by c), return 'dig'
    do
      {
        dig++;
        num = num / 10;
      }
    while (num != 0);
    return dig;
}
