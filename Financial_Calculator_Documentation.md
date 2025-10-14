# Financial Calculator for Engineering Economics
## Portfolio 2 Assignment - Option C

### Overview
This financial calculator is a comprehensive Python program designed to solve various types of engineering economics problems that would typically appear on an exam. The program is flexible and can handle multiple calculation types through a well-structured class-based approach.

### Capabilities

#### 1. Basic Equivalence Calculations
The calculator can solve for any unknown value in basic time value of money problems involving:
- **Present Value (P)**: Find the current worth of future cash flows
- **Future Value (F)**: Find the future worth of present investments
- **Annual Payment (A)**: Find uniform periodic payments
- **Interest Rate (i)**: Find the rate of return
- **Number of Periods (n)**: Find the time required

**Supported Interest Factors:**
- (P/F, i%, n) - Single Payment Present Worth Factor  
- (F/P, i%, n) - Single Payment Compound Amount Factor
- (P/A, i%, n) - Uniform Series Present Worth Factor
- (F/A, i%, n) - Uniform Series Compound Amount Factor  
- (A/P, i%, n) - Capital Recovery Factor
- (A/F, i%, n) - Sinking Fund Factor

#### 2. Deferred Annuity Calculations
The program can calculate present values for annuities that don't start immediately. This is useful for problems where uniform payments begin after a deferral period.

**Example Use Case:** Find the present value of $2,000 annual payments for 4 years, starting in year 3, with 10% interest.

#### 3. Gradient Series Calculations
The calculator handles both arithmetic and geometric gradient series:

**Arithmetic Gradient:** Payments that increase by a uniform amount each period
- Supports (P/G, i%, n) and (A/G, i%, n) factors
- Can handle base payment + gradient calculations

**Geometric Gradient:** Payments that increase by a uniform percentage each period
- Handles growth rates equal to, greater than, or less than the interest rate

#### 4. Interest Rate Conversions
The program converts between different interest rate formulations:
- **Nominal to Effective:** Convert stated annual rates with compounding to effective annual rates
- **Effective to Nominal:** Reverse conversion 
- **Continuous Compounding:** Handle continuously compounded rates

#### 5. Equivalence Analysis
Advanced features for comparing alternatives:
- **Net Present Value (NPV):** Calculate NPV of cash flow series
- **Equivalent Payments:** Find single equivalent payments at any point in time
- **Iterative Interest Rate Finding:** Solve for unknown interest rates using numerical methods

### Usage Instructions

#### Basic Usage
```python
from financial_calculator import FinancialCalculator

# Create calculator instance
calc = FinancialCalculator()

# Example: Find present value of $10,000 in 5 years at 8%
present_value = calc.calculate_present_value(future_value=10000, i=0.08, n=5)
print(f"Present Value: ${present_value:.2f}")
```

#### Method Reference

**Basic Calculations:**
```python
# Present Value calculations
calc.calculate_present_value(future_value=F, i=rate, n=periods)
calc.calculate_present_value(annual_payment=A, i=rate, n=periods)

# Future Value calculations  
calc.calculate_future_value(present_value=P, i=rate, n=periods)
calc.calculate_future_value(annual_payment=A, i=rate, n=periods)

# Annual Payment calculations
calc.calculate_annual_payment(present_value=P, i=rate, n=periods)
calc.calculate_annual_payment(future_value=F, i=rate, n=periods)
```

**Deferred Annuity:**
```python
# Present value of deferred annuity
pv = calc.calculate_deferred_annuity_present_value(
    annual_payment=2000, i=0.10, n_payments=4, n_defer=2)
```

**Gradient Series:**
```python
# Arithmetic gradient present value
pv = calc.calculate_arithmetic_gradient_present_value(
    base_payment=1000, gradient=200, i=0.12, n=6)

# Geometric gradient present value  
pv = calc.calculate_geometric_gradient_present_value(
    first_payment=1000, growth_rate=0.05, i=0.10, n=8)
```

**Interest Rate Conversions:**
```python
# Nominal to effective
effective_rate = calc.nominal_to_effective_rate(nominal_rate=0.12, compounding_periods=12)

# Find unknown interest rate
rate = calc.find_interest_rate_iterative(present_value=1000, future_value=2000, n=10)
```

**Utility Features:**
```python
# Display formatted results
calc.display_calculation_summary("Problem Description", inputs_dict, result)

# Print interest factor tables
calc.print_interest_factors_table(interest_rate=0.10, max_periods=10)

# NPV analysis
npv = calc.net_present_value(cash_flows=[-1000, 300, 400, 500, 600], interest_rate=0.10)
```

### Program Structure

The calculator is built using object-oriented programming principles:

**FinancialCalculator Class:** Main class containing all calculation methods
- **Interest Factor Methods:** Calculate standard engineering economics factors
- **Equivalence Methods:** High-level methods for common calculations  
- **Advanced Methods:** Gradient series, deferred annuities, rate conversions
- **Utility Methods:** Formatting, tables, result tracking

**Error Handling:** The program includes appropriate error checking for:
- Division by zero in interest calculations
- Invalid parameter combinations
- Non-convergent iterative solutions

**Results Tracking:** All calculations are stored in a history for reference.

### Running the Program

**Command Line Execution:**
```bash
python3 financial_calculator.py
```

This runs the demonstration examples and shows the calculator's capabilities.

**Interactive Usage:**
```python
# Import and use in interactive mode
from financial_calculator import FinancialCalculator
calc = FinancialCalculator()

# Run your specific calculations
result = calc.calculate_present_value(future_value=5000, i=0.06, n=8)
```

### Educational Value

This calculator serves as both a problem-solving tool and a learning aid:

1. **Formula Verification:** Students can verify hand calculations against programmed formulas
2. **Factor Tables:** Generates interest factor tables for reference
3. **Step-by-Step Output:** Shows detailed calculation summaries
4. **Multiple Methods:** Demonstrates different approaches to the same problem
5. **Error Prevention:** Reduces arithmetic errors in complex calculations

The program is designed to complement, not replace, understanding of engineering economics fundamentals. Students should still learn to set up problems by hand and understand the underlying principles.