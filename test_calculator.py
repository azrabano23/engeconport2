#!/usr/bin/env python3

from financial_calculator import FinancialCalculator

calc = FinancialCalculator()

print('=== ADDITIONAL TESTING ===')
print()

# Test geometric gradient
print('Geometric Gradient Test:')
try:
    pv_geom = calc.calculate_geometric_gradient_present_value(1000, 0.05, 0.10, 8)
    print(f'Geometric gradient PV: ${pv_geom:.2f}')
except Exception as e:
    print(f'Error: {e}')

# Test continuous compounding
print()
print('Continuous Compounding Test:')
try:
    cont_eff = calc.continuous_compounding_effective_rate(0.12)
    print(f'Continuous compounding effective rate: {cont_eff*100:.2f}%')
except Exception as e:
    print(f'Error: {e}')

# Test NPV calculation
print()
print('NPV Test:')
try:
    cash_flows = [-1000, 300, 400, 500, 600]
    npv = calc.net_present_value(cash_flows, 0.10)
    print(f'NPV of cash flows {cash_flows}: ${npv:.2f}')
except Exception as e:
    print(f'Error: {e}')

# Test zero interest rate edge case
print()
print('Zero Interest Rate Test:')
try:
    pv_zero = calc.calculate_present_value(annual_payment=1000, i=0.0, n=5)
    print(f'PV with 0% interest: ${pv_zero:.2f}')
except Exception as e:
    print(f'Error: {e}')

# Test equivalent payment calculation
print()
print('Equivalent Payment Test:')
try:
    cash_flows = [-1000, 300, 400, 500, 600]
    equiv = calc.find_equivalent_payment(cash_flows, 0.10, 5)
    print(f'Equivalent payment at year 5: ${equiv:.2f}')
except Exception as e:
    print(f'Error: {e}')

print()
print('All tests completed successfully!')