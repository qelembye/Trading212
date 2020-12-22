import psycopg2
# import datetime

# values = ('GBP-USD' , 1.35477 , 1.33676 , 1.35477 , 1.34622 , '2020-12-16 14:56:01')
#
# currency = values[0]
# valuex = values[1]
# valuemin = values[2]
# valuemax = values[3]
# valueaverage = values[4]
# date1 = values[5]
# id = int(datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S').timestamp())
# # date2 = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S').timestamp()
# # print('EPOCH = ', date2)



# dbtable = 'dbtestsix'

# sqlcommand = "INSERT INTO " + str(dbtable) \
#     + "(currencyid, currency, currencvalue, currencmin, currencmax, currencaverage, datex)" \
#     + " VALUES (" + str(id) + ", '" + str(currency) + "', " + str(valuex) + ', ' + str(valuemin) + ', ' + str(valuemax) + ', ' \
#     + str(valueaverage) + ', ' + "TO_TIMESTAMP('" + str(date1) + "', 'YYYY-MM-DD HH24:MI:SS')" + ');'

# sqlcommand = """INSERT INTO dbtestsixx
# (id, currency, currencvalue, currencmin, currencmax, currencaverage, datex)
# SELECT DISTINCT 1608134161, 'GBP-USD', 1.35477, 1.33676, 1.35477, 1.34622, TO_TIMESTAMP('2020-12-16 15:56:01', 'YYYY-MM-DD HH24:MI:SS')
# WHERE NOT EXISTS
# (SELECT * FROM dbtestsixx WHERE ID = 1608134161);
# """

sqlcommand = '''INSERT INTO dbtestsixx
(id, currency, currencvalue, currencmin, currencmax, currencaverage, datex)
SELECT DISTINCT 1608141361, 'GBP-USD', 1.35477, 1.33676, 1.35477, 1.34622, TO_TIMESTAMP('2020-12-16 17:56:01', 'YYYY-MM-DD HH24:MI:SS')
WHERE NOT EXISTS
(SELECT * FROM dbtestsixx WHERE ID = 1608141361); '''
print(sqlcommand)

host="localhost"
user="postgres"
pswd="H0meBase"

conn = psycopg2.connect(host=host, user=user, password=pswd)
cur = conn.cursor()

cur.execute(sqlcommand)

conn.commit()
cur.close()
conn.close()
