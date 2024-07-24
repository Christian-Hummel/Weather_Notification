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
        res.append(html[s+len(DIV):e])



    # remove whitespaces with replace function
    res = [elem.replace(" ", "") for elem in res]


    # convert list into dictionary
    res = {lst[0]: (lst[1].split(",") if "," in lst[1] else lst[1]) for lst in
            [line.split(":", maxsplit=1) for line in res]}


    return res

def save_to_file(msg):

    with open('../conf/commands.json', 'w') as outfile:
        json.dump(msg, outfile)

# email credentials saved in local file
with open('../conf/email.yaml', 'r') as f:
    conf = yaml.safe_load(f)


email_address = conf["email_address"]
password = conf["password"]

with MailBox("imap.gmail.com", port=993).login(email_address, password) as mailbox:

    # end program if there are no messages
    if not len(list(mailbox.fetch())):
        sys.exit("No messages received")

    # capture only the latest mail received
    msg = list(mailbox.fetch(limit=1, reverse=True, mark_seen=True))[0].html


message = convert_message(msg)
save_to_file(message)






