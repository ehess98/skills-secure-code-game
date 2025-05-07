'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0
    valid_types = {"payment", "product"}

    for item in order.items:
        # Ensure item type is valid
        if item.type not in valid_types:
            return "Error: Invalid item type '%s' in Order ID: %s" % (item.type, order.id)

        # Validate numeric values
        if item.amount < 0 or item.quantity < 0:
            return "Error: Negative amount or quantity in Order ID: %s" % order.id

        # Calculate net total
        if item.type == 'payment':
            net += item.amount
        elif item.type == 'product':
            net -= item.amount * item.quantity

    # Verify payment balance
        if net != 0:
            return "Order ID: %s - Payment imbalance detected: $%0.2f" % (order.id, net)
        else:
            return "Order ID: %s - Full payment received successfully!" % order.id