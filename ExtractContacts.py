# In powershell run: `python ExtractContacts.py > contacts_list.txt`, to save it in a .txt file.

import vobject

file = open("Contacts.vcf", "r")

non_tele_count = 0

with open("extracted_contacts.txt", "a+") as extracted_contacts:
    for vcard in vobject.readComponents(file):
        if 'tel' in vcard.contents:
            extracted_contacts.write(str({vcard.contents["fn"][0].value: [tel.value for tel in vcard.contents["tel"]]}))
            extracted_contacts.write("\n")
            # print({vcard.contents["fn"][0].value: [tel.value for tel in vcard.contents["tel"]]})
        else:
            non_tele_count += 1
            continue

    extracted_contacts.write(f"Number of contacts without phone number: {non_tele_count}")
    # print("Number of contacts without phone number: ", non_tele_count)



### OLD Code ###

# In powershell run: `python ExtractContacts.py > contacts_list.txt`, to save it in a .txt file.

# import vobject

# file = open("Contacts.vcf", "r")
# for vcard in vobject.readComponents(file):
#     print({vcard.contents["fn"][0].value: [tel.value for tel in vcard.contents["tel"]]})
