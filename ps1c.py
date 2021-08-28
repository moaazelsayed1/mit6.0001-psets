def main():
    annual_salary = float(input("Enter your annual salary: "))
    target = 0.25 * 1000000
    #number_of_months = 36
    steps = 0
    # bisection search
    low = 0
    high = 10000
    # print(f"ans: {ans}")
    currunt_savings = 0.0

    while abs(currunt_savings - target) > 100:
        # for i in range(14):
        steps += 1

        #print(f"Steps in bisection search: {steps}")
        ans = (low + high) // 2
        #print(f"Best savings rate: {ans}")
        monthly_savings = (annual_salary / 12) * (ans / float(10000))
        currunt_savings = 0.0
        for i in range(1, 37):
            if (i % 6 == 0):
                monthly_savings += monthly_savings * 0.07
            currunt_savings += monthly_savings + \
                ((currunt_savings * 0.04) / 12)
        #print(f"currunt_savings: {currunt_savings}")
        if currunt_savings > target:
            high = ans
        else:
            low = ans
        #print(f"high: {high}")
        #print(f"low: {low}")
        if high - low == 1:
            print('It is not possible to pay the down payment in three years.')
            return
    print("Best savings rate: {:.4f}".format(ans / 10000))
    print(f"Steps in bisection search: {steps}")


if __name__ == "__main__":
    main()
