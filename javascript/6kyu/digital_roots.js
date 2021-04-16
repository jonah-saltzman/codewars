// Digital root is the recursive sum of all the digits in a number.

// Given n, take the sum of the digits of n. If that value has more 
// than one digit, continue reducing in this way until a single-digit 
// number is produced. The input will be a non-negative integer.



function digital_root(n) {
    // get number of digits in n
    let string = n.toString();
    let digits = string.length;

    // if n has one digit, return n
    if (digits == 1){
        return n;
    }
    
    // populate "list" with each digit in "n"
    let dividend = n;
    let list = [];
    for (let i = 0; i < digits; i++){
        list[i] = dividend % 10;
        dividend = dividend.toString();
        dividend = dividend.slice(0, dividend.length - 1);
        dividend = parseInt(dividend);
    }

    // sum all the digits in n
    let sum = 0;
    for (let i = 0; i < digits; i++){
        sum += list[i];
    }

    // if sum has more than one digit, recursively call digital_root()
    let sumstring = sum.toString();
    let sumlength = sumstring.length;
    if (sumlength > 1){
        return digital_root(sum);
    }
  
    // otherwise, digital root has been found; return sum
    else {
        return sum;
    }

  }
