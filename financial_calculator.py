#!/usr/bin/env python3
"""
Financial Calculator for Engineering Economics
Portfolio 2 Assignment - Option C

This program provides flexible calculations for various financial engineering problems
including basic equivalence, deferred annuities, gradient series, and interest rate conversions.

Author: Portfolio Assignment Submission
Date: October 2024
"""

import math

class FinancialCalculator:
    """
    A comprehensive financial calculator for engineering economics problems.
    """
    
    def __init__(self):
        self.results_history = []
    
    # Basic Interest Factor Calculations
    def single_payment_present_worth_factor(self, i, n):
        """Calculate (P/F, i%, n) factor"""
        return 1 / ((1 + i) ** n)
    
    def single_payment_compound_amount_factor(self, i, n):
        """Calculate (F/P, i%, n) factor"""
        return (1 + i) ** n
    
    def uniform_series_present_worth_factor(self, i, n):
        """Calculate (P/A, i%, n) factor"""
        if i == 0:
            return n
        return ((1 + i) ** n - 1) / (i * (1 + i) ** n)
    
    def uniform_series_compound_amount_factor(self, i, n):
        """Calculate (F/A, i%, n) factor"""
        if i == 0:
            return n
        return ((1 + i) ** n - 1) / i
    
    def capital_recovery_factor(self, i, n):
        """Calculate (A/P, i%, n) factor"""
        if i == 0:
            return 1/n
        return (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    
    def sinking_fund_factor(self, i, n):
        """Calculate (A/F, i%, n) factor"""
        if i == 0:
            return 1/n
        return i / ((1 + i) ** n - 1)
    
    # Basic Equivalence Calculations
    def calculate_present_value(self, future_value=None, annual_payment=None, i=None, n=None):
        """Calculate Present Value given F, A, i, or n"""
        if future_value is not None:
            return future_value * self.single_payment_present_worth_factor(i, n)
        elif annual_payment is not None:
            return annual_payment * self.uniform_series_present_worth_factor(i, n)
        else:
            raise ValueError("Either future_value or annual_payment must be provided")
    
    def calculate_future_value(self, present_value=None, annual_payment=None, i=None, n=None):
        """Calculate Future Value given P, A, i, or n"""
        if present_value is not None:
            return present_value * self.single_payment_compound_amount_factor(i, n)
        elif annual_payment is not None:
            return annual_payment * self.uniform_series_compound_amount_factor(i, n)
        else:
            raise ValueError("Either present_value or annual_payment must be provided")
    
    def calculate_annual_payment(self, present_value=None, future_value=None, i=None, n=None):
        """Calculate Annual Payment given P, F, i, or n"""
        if present_value is not None:
            return present_value * self.capital_recovery_factor(i, n)
        elif future_value is not None:
            return future_value * self.sinking_fund_factor(i, n)
        else:
            raise ValueError("Either present_value or future_value must be provided")
    
    # Deferred Annuity Calculations
    def calculate_deferred_annuity_present_value(self, annual_payment, i, n_payments, n_defer):
        """
        Calculate present value of a deferred annuity
        annual_payment: uniform payment amount
        i: interest rate per period
        n_payments: number of payments
        n_defer: number of periods to defer (before first payment)
        """
        # First find the present value at the beginning of the payment period
        pv_at_payment_start = annual_payment * self.uniform_series_present_worth_factor(i, n_payments)
        # Then discount back by the deferral period
        pv_today = pv_at_payment_start * self.single_payment_present_worth_factor(i, n_defer)
        return pv_today
    
    # Gradient Series Calculations
    def arithmetic_gradient_present_worth_factor(self, i, n):
        """Calculate (P/G, i%, n) factor for arithmetic gradient"""
        if i == 0:
            return (n * (n - 1)) / 2
        return (1/i) * (self.uniform_series_present_worth_factor(i, n) - n/((1 + i)**n))
    
    def arithmetic_gradient_uniform_series_factor(self, i, n):
        """Calculate (A/G, i%, n) factor for arithmetic gradient"""
        if i == 0:
            return (n - 1) / 2
        return (1/i) - (n / ((1 + i)**n - 1))
    
    def calculate_arithmetic_gradient_present_value(self, base_payment, gradient, i, n):
        """
        Calculate present value of arithmetic gradient series
        base_payment: first payment amount
        gradient: uniform increase each period
        i: interest rate per period
        n: number of periods
        """
        base_pv = base_payment * self.uniform_series_present_worth_factor(i, n)
        gradient_pv = gradient * self.arithmetic_gradient_present_worth_factor(i, n)
        return base_pv + gradient_pv
    
    def calculate_geometric_gradient_present_value(self, first_payment, growth_rate, i, n):
        """
        Calculate present value of geometric gradient series
        first_payment: first payment amount
        growth_rate: rate of growth per period (as decimal, e.g., 0.05 for 5%)
        i: interest rate per period
        n: number of periods
        """
        if abs(growth_rate - i) < 1e-10:  # g ≈ i
            return first_payment * n / (1 + i)
        else:
            factor = (1 - ((1 + growth_rate)/(1 + i))**n) / (i - growth_rate)
            return first_payment * factor
    
    # Interest Rate Calculations
    def nominal_to_effective_rate(self, nominal_rate, compounding_periods):
        """Convert nominal interest rate to effective annual rate"""
        return (1 + nominal_rate/compounding_periods)**compounding_periods - 1
    
    def effective_to_nominal_rate(self, effective_rate, compounding_periods):
        """Convert effective annual rate to nominal rate"""
        return compounding_periods * ((1 + effective_rate)**(1/compounding_periods) - 1)
    
    def continuous_compounding_effective_rate(self, nominal_rate):
        """Calculate effective rate for continuous compounding"""
        return math.exp(nominal_rate) - 1
    
    def find_interest_rate_iterative(self, present_value, future_value, n, tolerance=1e-6, max_iterations=100):
        """
        Find interest rate using iterative method (Newton-Raphson)
        for P and F values over n periods
        """
        # Initial guess
        i = (future_value/present_value)**(1/n) - 1
        
        for iteration in range(max_iterations):
            f = present_value * (1 + i)**n - future_value
            df = present_value * n * (1 + i)**(n-1)
            
            i_new = i - f/df
            
            if abs(i_new - i) < tolerance:
                return i_new
            
            i = i_new
        
        raise ValueError(f"Interest rate did not converge after {max_iterations} iterations")
    
    # Equivalence Analysis
    def net_present_value(self, cash_flows, interest_rate):
        """
        Calculate NPV of a series of cash flows
        cash_flows: list of cash flows by period (period 0 is today)
        interest_rate: discount rate
        """
        npv = 0
        for period, cash_flow in enumerate(cash_flows):
            npv += cash_flow * self.single_payment_present_worth_factor(interest_rate, period)
        return npv
    
    def find_equivalent_payment(self, cash_flows, interest_rate, target_period):
        """
        Find equivalent single payment at target_period for given cash flows
        """
        npv = self.net_present_value(cash_flows, interest_rate)
        if target_period == 0:
            return npv
        else:
            return npv * self.single_payment_compound_amount_factor(interest_rate, target_period)
    
    # Utility Methods
    def display_calculation_summary(self, description, inputs, result):
        """Display a formatted summary of calculations"""
        print(f"\n{'='*60}")
        print(f"CALCULATION: {description}")
        print(f"{'='*60}")
        print("INPUTS:")
        for key, value in inputs.items():
            if isinstance(value, float):
                print(f"  {key}: {value:.4f}")
            else:
                print(f"  {key}: {value}")
        print(f"\nRESULT: {result:.2f}")
        print(f"{'='*60}")
        
        # Store in history
        self.results_history.append({
            'description': description,
            'inputs': inputs,
            'result': result
        })
    
    def print_interest_factors_table(self, interest_rate, max_periods=10):
        """Print a table of interest factors for given rate"""
        print(f"\nINTEREST FACTORS TABLE (i = {interest_rate*100:.1f}%)")
        print("="*80)
        print(f"{'n':<3} {'(P/F)':<8} {'(F/P)':<8} {'(P/A)':<8} {'(F/A)':<8} {'(A/P)':<8} {'(A/F)':<8}")
        print("-"*80)
        
        for n in range(1, max_periods + 1):
            pf = self.single_payment_present_worth_factor(interest_rate, n)
            fp = self.single_payment_compound_amount_factor(interest_rate, n)
            pa = self.uniform_series_present_worth_factor(interest_rate, n)
            fa = self.uniform_series_compound_amount_factor(interest_rate, n)
            ap = self.capital_recovery_factor(interest_rate, n)
            af = self.sinking_fund_factor(interest_rate, n)
            
            print(f"{n:<3} {pf:<8.4f} {fp:<8.4f} {pa:<8.4f} {fa:<8.4f} {ap:<8.4f} {af:<8.4f}")


def main():
    """Main function demonstrating calculator capabilities"""
    calc = FinancialCalculator()
    
    print("FINANCIAL CALCULATOR FOR ENGINEERING ECONOMICS")
    print("Portfolio 2 Assignment - Option C")
    print("=" * 60)
    
    # Example 1: Basic P, F, A calculations
    print("\n1. BASIC EQUIVALENCE CALCULATIONS")
    
    # Calculate present value of $10,000 due in 5 years at 8%
    i = 0.08
    n = 5
    F = 10000
    P = calc.calculate_present_value(future_value=F, i=i, n=n)
    calc.display_calculation_summary(
        "Present Value of Future Sum",
        {"Future Value (F)": F, "Interest Rate (i)": i, "Periods (n)": n},
        P
    )
    
    # Example 2: Deferred Annuity
    print("\n2. DEFERRED ANNUITY CALCULATION")
    
    # $2000 per year for 4 years, starting in year 3, i = 10%
    A = 2000
    i = 0.10
    n_payments = 4
    n_defer = 2
    PV_deferred = calc.calculate_deferred_annuity_present_value(A, i, n_payments, n_defer)
    calc.display_calculation_summary(
        "Deferred Annuity Present Value",
        {"Annual Payment (A)": A, "Interest Rate (i)": i, 
         "Payment Periods": n_payments, "Deferral Periods": n_defer},
        PV_deferred
    )
    
    # Example 3: Arithmetic Gradient
    print("\n3. ARITHMETIC GRADIENT CALCULATION")
    
    # Base payment $1000, gradient $200, 6 years, i = 12%
    base = 1000
    gradient = 200
    i = 0.12
    n = 6
    PV_gradient = calc.calculate_arithmetic_gradient_present_value(base, gradient, i, n)
    calc.display_calculation_summary(
        "Arithmetic Gradient Present Value",
        {"Base Payment": base, "Gradient": gradient, "Interest Rate (i)": i, "Periods (n)": n},
        PV_gradient
    )
    
    # Example 4: Interest Rate Conversion
    print("\n4. NOMINAL TO EFFECTIVE INTEREST RATE")
    
    # 12% nominal compounded monthly
    nominal = 0.12
    m = 12
    effective = calc.nominal_to_effective_rate(nominal, m)
    calc.display_calculation_summary(
        "Effective Interest Rate",
        {"Nominal Rate": f"{nominal*100:.1f}%", "Compounding Periods": m},
        effective*100  # Show as percentage
    )
    
    # Display interest factors table
    print("\n5. INTEREST FACTORS TABLE")
    calc.print_interest_factors_table(0.10, 8)
    
    return calc


if __name__ == "__main__":
    calculator = main()