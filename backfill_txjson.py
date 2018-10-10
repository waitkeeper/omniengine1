from sqltools import *
from rpcclient import *
import json

dbInit()
rows = dbSelect("select * from transactions where txdbserialnum < 46631497;");
print rows
for each in rows:
  print each , gettransaction_MP(each[0])['result'] 
  statement = "insert into txjson (txdbserialnum, txdata, protocol) values (" + str(each[3]) + ", \'" + json.dumps(gettransaction_MP(each[0])['result']) + "\', \'" + each[2] + "\')"
  print statement
  dbExecute(statement);
  dbCommit();
