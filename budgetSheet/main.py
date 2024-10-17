import pandas as pd

# data = {
#     'Date': ['06/25/2024'],
#     'Amount': [2],
#     'Spend': [1],
#     'Save': [1],
#     'totalSpend': [1],
#     'totalSave': [1]

# }


# df = pd.DataFrame(data)

path = 'data.csv'
# df.to_csv(path, index=False)


df = pd.read_csv(path)
def addData(date, hours, amount, spend, save):
    global df
    newTotalSave = save + df['totalSave'].iloc[-1]
    newTotalSpend = spend + df['totalSpend'].iloc[-1]
    df2 = pd.DataFrame([[date, hours, amount, spend, save, newTotalSpend, newTotalSave]], columns=['Date', 'Hours', 'Amount', 'Spend', 'Save', 'totalSpend', 'totalSave'])
    df = pd.concat([df, df2], ignore_index=True)
    print(f"{date} was added to the record")
    df.to_csv(path, index=False)


todo = input("What would you like to do: \n1: Add an entry\n2: Print entire record\n3: Print record for a date\n4: Print total saved\n5: Print total spend\n0: exit\n\n")

match todo:
    case "1":
        print("Enter the data requested: \n")
        date = input("Enter a date: \n")
        hours = input("Enter the amount of hours you worked: \n")
        amount = int(input("Enter the total amount you earned: \n"))
        percentSave = float(input("Enter the percent that youd like to save: "))
        saved = percentSave * amount
        spent = amount - saved
        addData(date, hours, amount, spend=spent, save=saved)

    case "2":
        print(df)
    case "3":
        print("temp")   
    case "4":
        print("temp")
    case "5":
        print("temp")
    case "0":
        print("exit")
        exit()
    case _:
        print("pick a number from 0 to 5!")