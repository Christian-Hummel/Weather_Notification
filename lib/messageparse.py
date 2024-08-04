from imap_tools import MailBox
import yaml
import json
import sys
from bs4 import BeautifulSoup



def convert_mail_gmail(message):
    res = []
    soup = soup = BeautifulSoup(message, "html.parser")

    for child in list(soup.descendants)[1::]:
        if child.name:
            res.append(child.text)

    text = [elem.replace(" ", "").replace("\xa0", "") for elem in res]
    text = [elem for elem in text if len(elem) > 0 and elem not in ["\r"]]

    text_dct = {lst[0]: (lst[1].split(",") if "," in lst[1] else lst[1]) for lst in
                [line.split(":", maxsplit=1) for line in text]}


    return text_dct



def convert_mail_imc_gmx(message):
    soup = BeautifulSoup(message, "html.parser")

    for child in soup.children:
        if child.name:
            text = child.text.split("\n")

    text = [elem.replace(" ", "").replace("\xa0", "") for elem in text]
    text = [elem for elem in text if len(elem) > 0 and elem not in ["\r"]]



    text_dct = {lst[0]: (lst[1].split(",") if "," in lst[1] else lst[1]) for lst in
            [line.split(":", maxsplit=1) for line in text]}


    return text_dct

def fetch_message():
    # email credentials saved in local file
    with open('conf/email.yaml', 'r') as f:
        conf = yaml.safe_load(f)


    email_address = conf["email_address"]
    password = conf["password"]
    imap = conf["imap"]
    imap_port = conf["port"]

    with MailBox(imap, port=imap_port).login(email_address, password) as mailbox:

        # end program if there are no messages
        if not len(list(mailbox.fetch())):
            sys.exit("No messages received")

        # extract latest mail
        mailbox = list(mailbox.fetch(limit=1, reverse=True, mark_seen=True))

        mail = mailbox[0]

        provider = mail.from_.split("@")[1].lower()



        if len([prov for prov in [provider] if "gmx" in prov or "imc" in prov]):
            return convert_mail_imc_gmx(mail.html)
        elif len([prov for prov in [provider] if "gmail" in prov]):
            return convert_mail_gmail(mail.html)

def save_to_file(msg):

    with open('conf/commands.json', 'w', encoding="utf-8") as outfile:
        json.dump(msg, outfile)










