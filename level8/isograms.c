/* Challenge: An isogram is a word that has no repeating letters, 
consecutive or non-consecutive. Implement a function that determines 
whether a string that contains only letters is an isogram. Assume 
the empty string is an isogram. Ignore letter case.

https://www.codewars.com/kata/54ba84be607a92aa900000f1 */

//My solution

#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool IsIsogram(char *str) 
  {
    //Get length of string
    int length = strlen(str);
  
    //Declare & initialize array with # of elements equal to number of lowercase alphabetical characters
    char array[26];
    for (int i = 0; i < 26; i++)
      {
        array[i] = 0;
      }
  
    //For each character in string, convert to lowercase & increment corresponding element in array
    char c;
    for (int i = 0; i < length; i++)
      {
        c = str[i];
        c = tolower(c);
        array[c - 97]++;
      }
  
    //If any character appears more than once, set iso to 1 and return false; otherwise, return true
    int iso = 0;
    for (int i = 0; i < 26; i++)
      {
        if (array[i] > 1)
          {
            iso = 1;
          }
      }
    if (iso == 1)
      return false;
    else
      return true;
  }
