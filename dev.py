#!/opt/homebrew/bin/python3
from account.contract_account import ContractAccount
from account.spot_account import SpotAccount
from snapshot_list import Snapshot, SnapshotList

if __name__ == '__main__':
  snapshot_list = SnapshotList()
  snapshot_list.append(Snapshot(None, 1))
  snapshot_list.append(Snapshot(None, 2))#1
  snapshot_list.append(Snapshot(None, 3))
  snapshot_list.append(Snapshot(None, 4))#1
  snapshot_list.append(Snapshot(None, 5))
  snapshot_list.append(Snapshot(None, 7))#1
  snapshot_list.append(Snapshot(None, 7))
  snapshot_list.append(Snapshot(None, 6))#1
  snapshot_list.append(Snapshot(None, 9))
  snapshot_list.append(Snapshot(None, 10))
  # length 10
  # size 3
  # (4 * 2) + 1 = 9
  print(snapshot_list.return_ratio(3))
  print(snapshot_list.return_ratio_std(3))
