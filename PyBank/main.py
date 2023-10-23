import csv
filename = "budget_data.csv"

with open(filename, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    data = list(csvreader)

    total_months = len(data)

    profit_loss = [int(row[1]) for row in data]
    net_total = sum(profit_loss)

    changes = [profit_loss[i+1] - profit_loss[i] for i in range(len(data) - 1)]

    average_change = sum(changes)/len(changes)

    max_increase = max(changes)
    max_decrease = min(changes)

    max_increase_date = data[changes.index(max_increase)+1][0]
    max_decrease_date = data[changes.index(max_decrease)+1][0]

    print("financial Analysis")
    print("__________________")
    print(f"Total Months:{total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change:${average_change:.2f}")
    print(f"Greatest Increase in Profits:{max_increase_date}(${max_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_date}(${max_decrease})")


        
