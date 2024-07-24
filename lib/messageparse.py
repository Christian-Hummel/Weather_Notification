from imap_tools import MailBox
import yaml
import sys

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


def search(html):

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
    return res


print(search(msg))

