def main():
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(
        input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    salary_raise = float(input("Enter the semi­annual raise, as a decimal: "))
    target = 0.25 * total_cost

    monthly_savings = (annual_salary / 12) * portion_saved
    currunt_savings = 0.0
    number_of_months = 0

    while (currunt_savings < target):
        if (number_of_months % 6 == 0 and number_of_months != 0):
            monthly_savings += monthly_savings * salary_raise
        currunt_savings += monthly_savings + ((currunt_savings * 0.04) / 12)
        number_of_months += 1

    print(f"Number of months: {number_of_months} ")


if __name__ == "__main__":
    main()
