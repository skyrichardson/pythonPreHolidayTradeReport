import csv
from jinja2 import Environment, FileSystemLoader
import markdown
import os


max_dollars_risk = 10000
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template('report_0.html')

with open('target_directory.txt', 'r') as f:
    directory = f.read()

with open(f'{directory}/report.csv', 'r') as f:
    csvreader = csv.reader(f)
    reports_list = list(csvreader)
    # print(reports_list)

with open(f'{directory}/holiday_label.txt', 'r') as f:
    holiday_label = f.read()

data = []
for r in reports_list:
    row = []
    row.append(r)
    price_change = float(r[2]) - float(r[1])  # profit/loss
    row.append(price_change)
    price_change_pct = ((float(r[2]) - float(r[1]))/float(r[1]))*100  # profit/loss percentage
    row.append(price_change_pct)
    stop_price = float(r[1]) - float(r[3])
    data.append(row)

html_output = ''
file_path = f'{root}/{directory}/notes.md'
if os.path.exists(file_path):
    # print(f"The file '{file_path}' exists.")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        html_output = markdown.markdown(content)


filename = f"{root}/{directory}/index.html"
with open(filename, 'w') as fh:
    fh.write(template.render(
        title='foo',
        date_str=directory,
        holiday_label=holiday_label,
        data=data,
        notes=html_output,
        last_edit='November 27, 2025'
    ))

# for c in charts:
#     shares = int(max_dollars_per_trade/float(c[3]))
#     if float(c[6]) != float(c[5]):
#         gain_loss = int((float(c[6]) - float(c[3])) * shares)
#     else:
#         gain_loss = int((float(c[5]) - float(c[3])) * shares)
#     c.append(shares)
#     c.append(gain_loss)
#     print(c)
#
# total = sum(sublist[-1] for sublist in charts)
# print(total)
# if total > 0:
#     total_str = str(f"${int(total):,}")
# else:
#     total_str = str(f'-${abs(int(total)):,}')
# change_in_equity = round((total/(max_dollars_per_trade * max_trades)) * 100, 2)
# print(str(change_in_equity) + '%')
# equity_available = max_dollars_per_trade * max_trades
#
# # Switch gain_loss to a string for presentation
# for c in charts:
#     if float(c[8]) > 0:
#         c[8] = str(f"${int(c[8]):,}")
#     else:
#         c[8] = str(f'-${abs(int(c[8])):,}')
# # print(charts)
#
#
# df = get_ticker_history('SPY')
# price_change = df['Open'].iloc[-1] - df['Open'].iloc[0]
# price_change_pct = round((price_change / df['Open'].iloc[0]) * 100, 2)
# # print(df.index[0], df['Open'].iloc[0])
# # print(df.index[-1], df['Open'].iloc[-1])
# print('price_change_pct', price_change_pct)
#
#
# exceeded = []
# file_path = f'{root}/{directory}/trades_exceed_max_allocation.csv'
# if os.path.exists(file_path):
#     print(f"The file '{file_path}' exists.")
#     with open(f'{directory}/trades_exceed_max_allocation.csv', 'r') as f:
#         csvreader = csv.reader(f)
#         for row in csvreader:
#             exceeded.append(row)
# # print(exceeded)
# for c in exceeded:
#     shares = int(max_dollars_per_trade/float(c[3]))
#     if float(c[6]) != float(c[5]):
#         gain_loss = int((float(c[6]) - float(c[3])) * shares)
#     else:
#         gain_loss = int((float(c[5]) - float(c[3])) * shares)
#     c.append(shares)
#     c.append(gain_loss)
#     print(c)
# for c in exceeded:
#     if float(c[8]) > 0:
#         c[8] = str(f"${int(c[8]):,}")
#     else:
#         c[8] = str(f'-${abs(int(c[8])):,}')
#
# my_trades = []
# file_path = f'{root}/{directory}/trades_closed_weekly.json'
# if os.path.exists(file_path):
#     print(f"The file '{file_path}' exists.")
#     with open(f'{directory}/trades_closed_weekly.json', 'r') as f:
#         my_trades = json.load(f)
#
#
#
#
# for c in my_trades:
#     print(c[0], c[3][4], c[5][4], c[3][3], 'shares')
#     gain_loss = int((float(c[5][4]) - float(c[3][4])) * int(c[3][3]))
#     c.append(gain_loss)
#     print(c[0], gain_loss)
# my_total = sum(sublist[-1] for sublist in my_trades)
# print(my_total)
# my_total_pct = round((my_total / (max_dollars_per_trade * max_trades)) * 100, 2)
#
# if my_total > 0:
#     my_total_str = str(f'${my_total:,}')
# else:
#     my_total_str = str(f'-${abs(my_total):,}')
#
# for c in my_trades:
#     if c[6] > 0:
#         c[6] = str(f"${int(c[6]):,}")
#     else:
#         c[6] = str(f'-${abs(int(c[6])):,}')
#
#
# html_output = ''
# file_path = f'{root}/{directory}/notes.md'
# if os.path.exists(file_path):
#     # print(f"The file '{file_path}' exists.")
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#         html_output = markdown.markdown(content)
#
# url= ''
# file_path = f'{root}/{directory}/url.txt'
# if os.path.exists(file_path):
#     # print(f"The file '{file_path}' exists.")
#     with open(file_path, 'r', encoding='utf-8') as f:
#         url = f.read()
#
# filename = f"{root}/{directory}/index.html"
# with open(filename, 'w') as fh:
#     fh.write(template.render(
#         title=directory,
#         charts=charts,
#         total=total_str,
#         change_in_equity=change_in_equity,
#         equity_available=equity_available,
#         max_trades=max_trades,
#         notes=html_output,
#         price_change_pct=price_change_pct,
#         exceeded=exceeded,
#         my_trades=my_trades,
#         my_total=my_total_str,
#         url=url
#     ))
#
# print(f'{directory},{total},{change_in_equity},{price_change_pct},{my_total},{my_total_pct}')
# file_path = f'{root}/{directory}/report.csv'
# with open(file_path, 'w') as f:
#     csvwriter = csv.writer(f)
#     csvwriter.writerow([directory, total, change_in_equity, price_change_pct, my_total, my_total_pct])
