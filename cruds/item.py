from typing import Optional
from enum import Enum
from schemas import ItemCreate, ItemStatus, ItemUpdate

class Item:
  def __init__(
    self,
    id: int,
    name: str,
    price: int,
    description: Optional[str],
    status: ItemStatus
  ):
    self.id = id
    self.name = name
    self.price = price
    self.description = description
    self.status = status

items = [
  Item(1, "PC", 100000, "備品です", ItemStatus.ON_SALE),
  Item(2, "スマートフォン", 50000, None, ItemStatus.ON_SALE),
  Item(3, "Python本", 1000, "使用感あり", ItemStatus.SOLD_OUT),
]

def find_all():
  return items

def find_by_id(id: int):
  for item in items:
    if id == item.id:
      return item
  return None

def find_by_name(name: str):
  find_name_list = []

  for item in items:
    if name in item.name:
      find_name_list.append(item)

  return find_name_list

  # BaseModelを継承したクラスは、FastAPI のエンドポイントに
  # 渡されたリクエストボディを、自動的にこのモデルのインスタンスに変換すので
  # create_item.プロパティ名でアクセス可能
def create(create_item: ItemCreate):
  new_item = Item(
    len(items) + 1,
    create_item.name,
    create_item.price,
    create_item.description,
    ItemStatus.ON_SALE
  )
  items.append(new_item)
  return new_item

def update(item_update: ItemUpdate, id: int):
  for item in items:
    if item.id == id:
      item.name = item.name if item_update.name is None else item_update.name
      item.price = item. price if item_update.price is None else item_update.price
      item.description = item.description if item_update.description is None else item_update.description
      item.status = item.status if item_update.status is None else item_update.status
    return item
  return None

def delete(id: int):
  for i in range(len(items)):
    if items[i].id == id:
      delete_item = items.pop(i)
      return delete_item
  return None

