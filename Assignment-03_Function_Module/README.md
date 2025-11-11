# 🧮 Python Assignment — Function & Math Module Programs

This assignment contains two Python programs demonstrating the use of functions, recursion, iteration, exception handling, and the math module.

---

## 📁 Files Included

| File Name | Description |
|------------|-------------|
| `factorial.py` | Calculates the factorial of a given number using both recursive and iterative methods. Handles invalid inputs and large numbers. |
| `module_math.py` | Uses Python’s `math` module to compute square root, natural logarithm (ln), and sine (in radians) of a given number. |

---

## 🧩 factorial.py — Factorial Program

### Description
- Accepts a number from the user.  
- Calculates factorial using:
  - Recursion for numbers ≤ 500  
  - Iteration for numbers > 500 (to avoid recursion depth errors)  
- Validates input and handles errors.  
- Allows the user to continue or exit.

### Example Output
```
----Factorial Program----
Enter a number: 5
Factorial of 5 is 120
Do You want to continue? (y/n)y
Enter a number: 1234
Factorial of 1234 is 452... (large number)
Do You want to continue? (y/n)n
Exiting program. Thank you!
```

---

## 🧮 module_math.py — Math Module Program

### Description
- Accepts a number from the user.  
- Uses the math module to calculate:
  - Square root (`math.sqrt()`)
  - Natural logarithm (`math.log()`)
  - Sine in radians (`math.sin()`)
- Displays results clearly.
- Handles invalid or negative inputs gracefully.

### Example Output
```
---- Math Operations Program ----
Enter a number: 10

Results:
Square root of 10: 3.1622776601683795
Natural log (ln) of 10: 2.302585092994046
Sine of 10 radians: -0.5440211108893698
```

---

## 🚀 How to Run

1. Open a terminal or command prompt.  
2. Navigate to the folder:
   ```bash
   cd Assignment-03_Function_Module
   ```
3. Run either program:
   ```bash
   python factorial.py
   ```
   or
   ```bash
   python math_operations.py
   ```

---

## 🧠 Concepts Covered

- Function definition and usage  
- Recursion and iteration  
- Exception handling  
- Conditional logic (`if`, `elif`, `else`)  
- Using the Python `math` module (`sqrt`, `log`, `sin`)  
- Input validation and user interaction  

---

**Author:** Amit Kumar Singh  
**Course:** Python Programming — Functions & Math Module Assignment  
