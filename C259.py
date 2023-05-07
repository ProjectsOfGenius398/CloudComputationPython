from etherpad_lite import EtherpadLiteClient
etherclient=EtherpadLiteClient(base_params={'apikey':'5ff7ea9032814c34a8f8daf05038aa9d48d29052678ca34eb40c69a981b118f9'})

group=etherclient.createGroup()
print('Group: ', group)
newPad=etherclient.createPad(padID='blackhat', text='hi')
print('Pad: ',newPad)