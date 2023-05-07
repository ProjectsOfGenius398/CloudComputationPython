from etherpad_lite import EtherpadLiteClient
from datetime import datetime
etherclient=EtherpadLiteClient(base_params={'apikey': '5ff7ea9032814c34a8f8daf05038aa9d48d29052678ca34eb40c69a981b118f9'})

new_pad=etherclient.createPad(padID='pad1', text='Hello! How are you?')
print("New pad: ", new_pad)

createAuthor=etherclient.createAuthor(name='CloudMan')
print(createAuthor)

padCount=etherclient.padUsersCount(padID='pad1')
print(padCount)

timestamp=etherclient.getLastEdited(padID='pad1')
print(timestamp)
lastEdit=timestamp['lastEdited']

dateConversion=datetime.fromtimestamp(lastEdit/1000.0)
print("date_time", dateConversion)

deletePad=etherclient.deletePad(padID='pad1')
print(deletePad)