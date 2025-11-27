import csv

with open('target_directory.txt', 'r') as f:
    directory = f.read()

with open('tickers.txt', 'r') as f:
    tickers = f.read().splitlines()


def get_report(ticker):
    with open(f'{directory}/{ticker}.csv', mode='r', newline='', encoding='utf-8') as file:
        # Pass the file object to csv.reader()
        csv_reader = csv.reader(file)

        # *** KEY STEP: Use next() to skip the first row ***
        try:
            next(csv_reader)
        except StopIteration:
            # Handle empty file case gracefully
            data = []

        # Convert the remaining reader object to a list
        data = list(csv_reader)

    # print(data)
    entry_price = float(data[-2][4])
    exit_price = float(data[-1][4])
    price_change = float(data[-1][4]) - float(data[-2][4])
    # print(f'Profit/loss:', f'{price_change:.2f}', f'({float(data[-1][4])} - {float(data[-2][4])})')
    # print('Range')
    reversed_data = data[::-1]
    last_ten_of_reversed = reversed_data[:10]
    list_of_ranges = []
    for d in last_ten_of_reversed:
        # print(f'Range: {float(d[2]) - float(d[3])} ({d[2]} ~ {d[3]}), {d[0]}')
        list_of_ranges.append([float(d[2]) - float(d[3]), d[0]])
    max_sublist = max(list_of_ranges, key=lambda sublist: sublist[0])
    # print(f"The list with the maximum first element is: {max_sublist}")
    max_range = max_sublist[0]
    max_range_date_str = max_sublist[1]
    report = [ticker.upper(), entry_price, exit_price, max_range, max_range_date_str]
    # print(report)
    return report


# print(get_report(tickers[0]))
report_list = []
for ticker in tickers:
    report_list.append(get_report(ticker))
print(report_list)
with open(f'{directory}/report.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(report_list)




