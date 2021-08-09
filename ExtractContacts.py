# In powershell run: `python ExtractContacts.py > contacts_list.txt`, to save it in a .txt file.

import vobject

file = open("Contacts.vcf", "r")
for vcard in vobject.readComponents(file):
    print({vcard.contents["fn"][0].value: [tel.value for tel in vcard.contents["tel"]]})