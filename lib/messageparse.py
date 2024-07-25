from imap_tools import MailBox
import yaml
import json
import sys


def convert_message(html):

    """

    filter out the contents of the message by extracting slices of the "div" html tags

    Args:
        html: email in html format

    Returns: content of the div html tags in a list

    """
    DIV = "<div>"
    res = []
    s, e = 0, 0
    while True:
        s = html.find(DIV, e)
        if s == -1:
            break
        e = html.find('</div>',s)
        line = html[s+len(DIV):e]
        if line != "&nbsp;":
            res.append(line)



    # remove whitespaces with replace function
    res = [elem.replace(" ", "") for elem in res]
    res = [elem.replace("&nbsp;","") for elem in res]

    # convert list into dictionary
    res = {lst[0]: (lst[1].split(",") if "," in lst[1] else lst[1]) for lst in
            [line.split(":", maxsplit=1) for line in res]}


    return res


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

        # capture only the latest mail received
        return convert_message(list(mailbox.fetch(limit=1, reverse=True, mark_seen=True))[0].html)

def save_to_file(msg):

    with open('conf/commands.json', 'w') as outfile:
        json.dump(msg, outfile)











