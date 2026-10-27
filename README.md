# Efficient Divisor Finder

This project is an optimized Python algorithm designed to find all exact divisors of a given positive integer quickly and efficiently. Moving beyond traditional loop logic, it utilizes a mathematical optimization method to prevent performance loss and save time, especially when processing large numbers.

## How the Algorithm Works (Optimization Logic)

The basic `find_divisor` functions (which are commented out in the code) check every single number from 1 up to the target number. While this works for small numbers, it causes severe performance drops and time delays for larger numbers (e.g., 1,000,000) because the computer has to run a million checks.

The active `find_divisor_mod` function optimizes the process using the following mathematical principles:

*   **Divisor Pairs:** Divisors of a number always come in pairs. For example, if we divide 36 by 2, the result is 18. This means both 2 and 18 are exact divisors.
*   **Square Root Limit:** In every divisor pair, at least one of the numbers is always less than or equal to the square root of the target number (the square root of 36 is 6).
*   **The Optimization:** Instead of looping all the way up to the number itself, the algorithm only loops up to its **square root**. When it finds a divisor (e.g., 2), it automatically calculates the paired divisor (36 // 2 = 18) and adds both to the list.
*   **Efficiency:** Thanks to this logic, finding the divisors for 1,000,000 takes only 1,000 steps instead of 1,000,000 steps.
*   **Data Structure:** To prevent adding duplicate divisors for perfect squares (like 6 and 6 for 36), a `set` data structure is used. Finally, the collected divisors are sorted in ascending order using the `sorted()` method and presented to the user.

## Technologies Used
*   Python 3.x
*   `math` module (for square root operations)

## How to Use

1. Download the Python file to your local machine.
2. Open your terminal or command prompt and navigate to the directory where the file is located.
3. Run the script using the command: `python file_name.py` (replace `file_name.py` with your actual file name).
4. When prompted with `enter a positive number :`, type the integer you want to analyze and press Enter.
5. The program will print a sorted list of all exact divisors. If you enter zero or a negative number, the program will prompt you again to enter a valid positive number.
