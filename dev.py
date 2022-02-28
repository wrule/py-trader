#!/opt/homebrew/bin/python3
from snapshot_list import Snapshot, SnapshotList

list = SnapshotList()

snp1 = Snapshot(
  datetime=0
)
snp2 = Snapshot(
  datetime=1
)
list.append(snp1)
list.append(snp2)
list.dataframe().to_excel('1.xlsx');
