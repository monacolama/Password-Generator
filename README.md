# Password Generator

This python program generates random passwords of **14 characters long**, with 3 lowercase letters, 3 uppercase letters, 4 numbers and 4 symbols.

After the password is generated, it is crypted and wrote in a file text. The cryptography method uses the symple Caesar Code, with an alphabetical key which gets translated into an integer number, the real key of the Code.

## Cryptography method

I used an alphabetical key which gets translated into a number to make it easier to remember. The translation is also simple. For example, if you choose the word **"home"**, each letter corresponds to an integer index in the alphabet (from 0 to 25). When the index is a double digit number, for example 13, the digits are added together, in this case -> 1+3=4. 

When every letter in the key has been translated, all the numbers are added togheter. For **"home"**, the final key will be: 19.
