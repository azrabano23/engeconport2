# Engineering Economics Financial Calculator

A comprehensive Python-based financial calculator designed for engineering economics problems, developed as part of Portfolio 2 assignment.

## 🚀 Features

### Core Functionality
- **Present Value (P)** calculations
- **Future Value (F)** calculations  
- **Annuity (A)** calculations
- **Interest Rate (i)** calculations
- **Number of Periods (N)** calculations

### Advanced Capabilities
- **Deferred Annuity Calculations** - Handle annuities that start at future periods
- **Gradient Series** - Both arithmetic and geometric gradient calculations
- **Net Present Value (NPV)** - Evaluate investment alternatives
- **Nominal/Effective Interest Rates** - Including continuous compounding
- **Equivalent Payment Calculations** - Convert between different payment structures

## 📁 Project Structure

```
├── financial_calculator.py                           # Main calculator program (308 lines)
├── Financial_Calculator_Documentation.md             # Complete usage documentation
├── Financial_Calculator_Spreadsheet_Instructions.md  # Excel alternative instructions
├── Sample_Solutions_Hand_Calculations.md             # 5 verified sample problems
├── Portfolio_2_Assignment_Summary.md                 # Assignment overview
├── test_calculator.py                               # Testing and validation script
└── README.md                                        # This file
```

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/azrabano23/engeconport2.git
   cd engeconport2
   ```

2. **Run the calculator:**
   ```bash
   python financial_calculator.py
   ```

3. **Run tests to verify functionality:**
   ```bash
   python test_calculator.py
   ```

### Example Usage

```python
from financial_calculator import FinancialCalculator

calc = FinancialCalculator()

# Calculate future value
future_value = calc.future_value(present=1000, rate=0.08, periods=5)
print(f"Future Value: ${future_value:.2f}")

# Calculate NPV of cash flows
cash_flows = [-1000, 300, 400, 500, 600]
npv = calc.net_present_value(cash_flows, 0.10)
print(f"NPV: ${npv:.2f}")
```

## 📊 Problem Types Solved

✅ **Basic Time Value Problems**
- Single payment present/future worth
- Uniform series present/future worth
- Capital recovery and sinking fund

✅ **Advanced Applications**
- Deferred annuities with varying start periods
- Arithmetic gradient series (increasing payments)
- Geometric gradient series (percentage increases)
- Nominal vs. effective interest rate conversions

✅ **Investment Analysis**
- Net Present Value (NPV) calculations
- Equivalent uniform annual worth
- Rate of return analysis

## 🧮 Alternative: Excel Implementation

For users preferring spreadsheet solutions, complete Excel formulas and instructions are provided in `Financial_Calculator_Spreadsheet_Instructions.md`.

## ✅ Verification

All calculations have been verified through:
- Hand calculations for 5 sample problems
- Cross-validation with standard engineering economics formulas
- Edge case testing and error handling validation

See `Sample_Solutions_Hand_Calculations.md` for detailed verification examples.

## 📖 Documentation

- **`Financial_Calculator_Documentation.md`** - Complete method reference and usage examples
- **`Portfolio_2_Assignment_Summary.md`** - Assignment requirements and completion checklist
- **`Sample_Solutions_Hand_Calculations.md`** - Worked examples with verification

## 🏗️ Architecture

The calculator uses object-oriented design with:
- **Comprehensive error handling** - Input validation and meaningful error messages
- **Modular structure** - Separate methods for each calculation type
- **Extensible design** - Easy to add new financial functions
- **Clean interface** - Both programmatic and interactive usage modes

## 🧪 Testing

Run the test suite to validate all functionality:

```bash
python test_calculator.py
```

Tests cover:
- Basic calculation accuracy
- Edge cases and boundary conditions
- Error handling and input validation
- Advanced feature verification

## 👨‍💻 Author

**Azra Bano**
- Engineering Economics Portfolio Assignment
- Comprehensive solution exceeding basic requirements

## 📝 License

This project is part of an academic assignment. Please respect academic integrity policies when referencing or using this code.

---

*This calculator provides a complete solution for engineering economics problems, combining mathematical accuracy with practical usability.*