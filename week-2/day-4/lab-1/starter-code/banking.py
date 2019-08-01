#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code
from transaction import Transaction

class BankAccount(object):
    
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return '%s: $%s' % (self.label, self.balance)
    
    def create_transaction(self, txType, amount):
        tx = Transaction(txType, amount, self.balance)
        self.transactions.append(tx)

    def withdraw(self, amount):
        if amount > self.balance:
            print 'You can\'t withdraw more than you have'
        elif amount < 0:
            print 'You can\'t withdraw a negative amount'
        else:
            self.balance -= amount
            self.create_transaction('withdraw', amount)
    
    def deposit(self, amount):
        if amount < 0:
            print 'You can\'t deposit a negative amount'
        else:
            self.balance += amount
            self.create_transaction('deposit', amount)

    def rename(self, label):
        if not label:
            print 'You can\'t set a blank label'
            return
        self.label = label

    def transfer(self, dest_acc, amount):
        if amount > self.balance:
            print 'You can\'t transfer more than you have'
        elif amount < 0:
            print 'You can\'t transfer a negative amount'
        else:
            self.balance -= amount
            dest_acc.deposit(amount)
            self.create_transaction('transfer', amount)
            dest_acc.create_transaction('deposit', amount)