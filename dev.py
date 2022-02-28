#!/opt/homebrew/bin/python3
from snapshot_list import Snapshot, SnapshotList
from transaction_list import Transaction, TransactionList

list = SnapshotList()

snp1 = Snapshot(
  datetime=0
)
snp2 = Snapshot(
  datetime=1
)
list = TransactionList()
list.start(snp1)
list.end(snp2)
print(list.last().win())

