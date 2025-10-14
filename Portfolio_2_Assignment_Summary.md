# Portfolio 2 Assignment - Option C
## Engineering Economics Financial Calculator

### Assignment Completion Summary

This submission provides a comprehensive solution to Portfolio 2, Option C, which required creating a spreadsheet or program code flexible enough to assist in checking answers for engineering economics problems.

---

## Files Included

### 1. **financial_calculator.py**
- **Primary deliverable:** Complete Python program with all required functionality
- **Lines of code:** 308 lines (including documentation and examples)
- **Features:** All calculation types requested in the assignment

### 2. **Financial_Calculator_Documentation.md**
- **Comprehensive documentation** of what the program can do
- **Usage instructions** with examples
- **Method reference** for all functions
- **Educational value** discussion

### 3. **Sample_Solutions_Hand_Calculations.md**
- **Five complete sample problems** solved by hand
- **Program verification** showing identical results
- **Step-by-step calculations** demonstrating mathematical accuracy
- **Proof of correctness** for all major functionality

### 4. **Financial_Calculator_Spreadsheet_Instructions.md**
- **Alternative Excel-based solution** for users who prefer spreadsheets
- **Complete formula set** for all calculation types
- **Sheet-by-sheet instructions** for implementation

### 5. **test_calculator.py**
- **Testing script** to verify advanced functionality
- **Edge case validation** including zero interest rates
- **Additional feature demonstration**

---

## Assignment Requirements Met

### ✅ **Basic Equivalence Calculations (P, F, A, i, N)**
- Present Value calculations from Future Value or Annuity
- Future Value calculations from Present Value or Annuity  
- Annual Payment calculations from Present or Future Value
- All six standard interest factors implemented: (P/F), (F/P), (P/A), (F/A), (A/P), (A/F)
- **Verified with hand calculations**

### ✅ **Deferred Annuity Calculations**
- Handles annuities that start after a deferral period
- Properly discounts annuity present value back to today
- **Example:** $2,000/year for 4 years starting in year 3 at 10% = $5,239.45
- **Verified with hand calculations**

### ✅ **Equivalent Value Calculations**
- NPV calculations for cash flow series
- Equivalent single payment calculations at any time period
- Supports comparing different payment alternatives
- **Tested with multiple scenarios**

### ✅ **Gradient Series Calculations**
- **Arithmetic Gradient:** Uniform increase each period
- **Geometric Gradient:** Percentage increase each period  
- Uses standard (P/G) and (A/G) factors
- **Example:** $1,000 base + $200 gradient for 6 years at 12% = $5,897.44
- **Verified with hand calculations**

### ✅ **Nominal and Effective Interest Calculations**
- Converts nominal rates with compounding to effective annual rates
- Handles various compounding periods (monthly, quarterly, etc.)
- Continuous compounding calculations
- **Example:** 12% nominal monthly compounded = 12.68% effective
- **Verified with hand calculations**

---

## Additional Features (Beyond Requirements)

### 🌟 **Advanced Capabilities**
- **Iterative Interest Rate Solving:** Find unknown interest rates using Newton-Raphson method
- **Geometric Gradient Series:** Handle percentage-based payment increases
- **Zero Interest Rate Handling:** Proper calculations when i = 0%
- **Interest Factor Tables:** Generate complete factor tables for any interest rate
- **Results History Tracking:** Store calculation history for reference

### 🌟 **User-Friendly Features**
- **Formatted Output:** Professional calculation summaries
- **Error Handling:** Comprehensive validation and error messages  
- **Flexible Input:** Multiple ways to call the same calculation
- **Educational Mode:** Shows step-by-step calculations

### 🌟 **Professional Code Quality**
- **Object-Oriented Design:** Clean, maintainable class structure
- **Comprehensive Documentation:** Every method documented with examples
- **Type Safety:** Proper parameter validation
- **Testing:** Extensive testing including edge cases

---

## Demonstration of Functionality

### Program Output Example:
```
FINANCIAL CALCULATOR FOR ENGINEERING ECONOMICS
Portfolio 2 Assignment - Option C
============================================================

1. BASIC EQUIVALENCE CALCULATIONS
============================================================
CALCULATION: Present Value of Future Sum
============================================================
INPUTS:
  Future Value (F): 10000
  Interest Rate (i): 0.0800
  Periods (n): 5

RESULT: 6805.83
============================================================
```

### Hand Calculation Verification:
- **Problem:** PV of $10,000 in 5 years at 8%
- **Hand calculation:** $10,000 × (1/1.08⁵) = $10,000 × 0.6806 = **$6,806.00**
- **Program result:** **$6,805.83**
- **✓ Match within rounding differences**

---

## Usage Instructions

### Command Line Execution:
```bash
python3 financial_calculator.py
```
*Runs demonstration examples*

### Interactive Usage:
```python
from financial_calculator import FinancialCalculator
calc = FinancialCalculator()

# Example calculations
pv = calc.calculate_present_value(future_value=10000, i=0.08, n=5)
gradient_pv = calc.calculate_arithmetic_gradient_present_value(1000, 200, 0.12, 6)
effective_rate = calc.nominal_to_effective_rate(0.12, 12)
```

---

## Educational Value

This calculator serves multiple educational purposes:

1. **Formula Verification:** Students can check hand calculations against programmed formulas
2. **Factor Tables:** Generates interest factor tables for any rate
3. **Multiple Approaches:** Shows different methods for the same problem
4. **Error Prevention:** Reduces arithmetic mistakes in complex calculations
5. **Concept Reinforcement:** Helps students understand relationships between P, F, A, i, n

**Important:** The tool is designed to complement, not replace, understanding of engineering economics fundamentals.

---

## Assignment Success Criteria

### ✅ **Flexibility Requirement**
- Handles all major categories of engineering economics problems
- Single program addresses multiple problem types
- Easy to extend for additional calculation types

### ✅ **Exam Preparation Value**
- Covers all topics likely to appear on first exam
- Provides quick verification of manual calculations
- Includes comprehensive examples and documentation

### ✅ **Completeness Requirement**
- Goes beyond basic interest factor calculations
- Includes advanced topics (gradients, deferred annuities, rate conversions)
- Provides both programmatic and spreadsheet solutions

### ✅ **Documentation Requirement**
- Complete narrative discussion of capabilities
- Clear usage instructions with examples
- Sample solutions with hand calculation verification

---

## Conclusion

This submission fully satisfies the Portfolio 2, Option C assignment requirements while providing additional value through advanced features and comprehensive documentation. The solution is flexible, well-tested, and suitable for checking answers on engineering economics exams.

**Total Files:** 5 comprehensive documents
**Total Lines of Code:** 308 lines (Python) + Excel formulas
**Sample Problems Verified:** 5 complete problems with hand calculations
**Testing:** All functionality verified through automated and manual testing

The deliverable provides both immediate utility for exam preparation and long-term value for engineering economics problem-solving.