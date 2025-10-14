# Excel Financial Calculator Spreadsheet
## Alternative to Python Program

Since the assignment allows for either a spreadsheet or program code, here are instructions for creating an Excel-based financial calculator that can handle the same types of problems.

## Spreadsheet Structure

### Sheet 1: Basic Calculations
**Columns A-F: Input Parameters**
- A1: "Present Value (P)"
- B1: "Future Value (F)" 
- C1: "Annual Payment (A)"
- D1: "Interest Rate (i)"
- E1: "Number of Periods (n)"
- F1: "Result"

**Row 3: Present Value from Future Value**
- A3: Enter P value (leave blank if calculating)
- B3: Enter F value
- C3: (leave blank)
- D3: Enter interest rate (as decimal, e.g., 0.08)
- E3: Enter number of periods
- F3: `=B3/(1+D3)^E3`

**Row 4: Future Value from Present Value**
- A4: Enter P value
- B4: (leave blank if calculating)
- C4: (leave blank)
- D4: Enter interest rate
- E4: Enter number of periods  
- F4: `=A4*(1+D4)^E4`

**Row 5: Present Value from Annuity**
- A5: (leave blank if calculating)
- B5: (leave blank)
- C5: Enter annual payment
- D5: Enter interest rate
- E5: Enter number of periods
- F5: `=IF(D5=0,C5*E5,C5*((1+D5)^E5-1)/(D5*(1+D5)^E5))`

**Row 6: Future Value from Annuity**
- A6: (leave blank)
- B6: (leave blank if calculating)
- C6: Enter annual payment
- D6: Enter interest rate
- E6: Enter number of periods
- F6: `=IF(D6=0,C6*E6,C6*((1+D6)^E6-1)/D6)`

**Row 7: Annual Payment from Present Value**
- A7: Enter P value
- B7: (leave blank)
- C7: (leave blank if calculating)
- D7: Enter interest rate
- E7: Enter number of periods
- F7: `=IF(D7=0,A7/E7,A7*D7*(1+D7)^E7/((1+D7)^E7-1))`

**Row 8: Annual Payment from Future Value**
- A8: (leave blank)
- B8: Enter F value
- C8: (leave blank if calculating)
- D8: Enter interest rate
- E8: Enter number of periods
- F8: `=IF(D8=0,B8/E8,B8*D8/((1+D8)^E8-1))`

### Sheet 2: Deferred Annuity
**Setup:**
- A1: "Annual Payment (A)"
- B1: "Interest Rate (i)"
- C1: "Payment Periods"
- D1: "Deferral Periods"
- E1: "Present Value"

**Formula in E2:**
```excel
=A2*((1+B2)^C2-1)/(B2*(1+B2)^C2)/(1+B2)^D2
```

### Sheet 3: Arithmetic Gradient
**Setup:**
- A1: "Base Payment"
- B1: "Gradient"
- C1: "Interest Rate (i)"
- D1: "Periods (n)"
- E1: "Present Value"

**Helper calculations:**
- F1: "(P/A,i,n)" 
- F2: `=IF(C2=0,D2,((1+C2)^D2-1)/(C2*(1+C2)^D2))`
- G1: "(P/G,i,n)"
- G2: `=IF(C2=0,D2*(D2-1)/2,(1/C2)*(F2-D2/(1+C2)^D2))`

**Main formula in E2:**
```excel
=A2*F2+B2*G2
```

### Sheet 4: Interest Rate Conversions
**Nominal to Effective:**
- A1: "Nominal Rate"
- B1: "Compounding Periods"
- C1: "Effective Rate"
- C2: `=(1+A2/B2)^B2-1`

**Continuous Compounding:**
- A4: "Nominal Rate"
- B4: "Effective Rate (Continuous)"
- B5: `=EXP(A4)-1`

### Sheet 5: Interest Factor Tables
Create a table with periods 1-20 and calculate all six factors:

**Headers (Row 1):**
A1: "n", B1: "(P/F)", C1: "(F/P)", D1: "(P/A)", E1: "(F/A)", F1: "(A/P)", G1: "(A/F)"

**Interest rate cell:** I1 (enter as decimal)

**Formulas for row 2 (copy down to row 21):**
- A2: 1 (then 2, 3, etc.)
- B2: `=1/(1+$I$1)^A2`
- C2: `=(1+$I$1)^A2`
- D2: `=IF($I$1=0,A2,((1+$I$1)^A2-1)/($I$1*(1+$I$1)^A2))`
- E2: `=IF($I$1=0,A2,((1+$I$1)^A2-1)/$I$1)`
- F2: `=IF($I$1=0,1/A2,$I$1*(1+$I$1)^A2/((1+$I$1)^A2-1))`
- G2: `=IF($I$1=0,1/A2,$I$1/((1+$I$1)^A2-1))`

## Usage Instructions

1. **Create a new Excel workbook** with the sheets described above
2. **Enter the formulas** exactly as shown (Excel will automatically handle cell references)
3. **Input your problem values** in the appropriate cells
4. **Read the calculated results** from the result cells
5. **For factor tables**, change the interest rate in cell I1 to get different tables

## Advantages of Excel Version

- **Visual Interface:** Easy to see inputs and outputs
- **Multiple Scenarios:** Can quickly change inputs to test different scenarios
- **Built-in Charts:** Can create graphs of factor values vs. periods
- **No Programming Knowledge Required:** Uses familiar Excel interface
- **Immediate Recalculation:** Results update automatically when inputs change

## Sample Problems in Excel

**Problem 1:** Find PV of $10,000 in 5 years at 8%
- Enter in row 3: B3=10000, D3=0.08, E3=5
- Result appears in F3: $6,805.83

**Problem 2:** Find PV of deferred annuity
- Go to Sheet 2
- Enter: A2=2000, B2=0.10, C2=4, D2=2  
- Result in E2: $5,239.45

**Problem 3:** Arithmetic gradient
- Go to Sheet 3
- Enter: A2=1000, B2=200, C2=0.12, D2=6
- Result in E2: $5,897.44

This spreadsheet approach provides the same functionality as the Python program but in a more accessible format for users comfortable with Excel.