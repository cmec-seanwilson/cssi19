class Transaction(object):
    
    def __init__(self, txType, amount, updatedBalance):
        self.tx_type = txType
        self.amount = amount
        self.updated_balance = updatedBalance

    def __str__(self):
        return 'Type: %s, Amount: %s, Updated Balance: %s' % (self.tx_type, self.amount, self.updated_balance)