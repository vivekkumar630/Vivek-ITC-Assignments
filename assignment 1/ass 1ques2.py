gross_income = int (input ("enter your gross income to nearest penny."))
standard_deduction= 10000
dependent_deduction= 3000
Tax_rate=20%gross_income
No_of_dependents = int(input ("No of dependents:"))
Taxable_income=gross_income -standard_deduction-(dependent_deduction*No_of_dependents)
tax=Taxable_income * 20%gross_income
print("person income tax is=" , tax)
