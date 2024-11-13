from fastapi import APIRouter, Path, Query, HTTPException
from cruds import item as item_cruds
from schemas import ItemCreate, ItemUpdate, ItemResponse
from starlette import status

# APIRouterの引数prefixに共通するパスを
# 指定することでパスを省略して記載することができる
router= APIRouter(prefix="/items", tags=["items"])

# 一覧表示 引数にresponse_modelを指定することでレスポンスの型を指定することができる
# allの場合はリスト型で返ってくるので、listを使用
@router.get("", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_all():
  return item_cruds.find_all()

# 個別表示
@router.get("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
# pathパラメーターでバリデーションの設定
async def find_by_id(id: int = Path(gt=0)):
  found_item = item_cruds.find_by_id(id)
  if not found_item:
    raise HTTPException(status_code=404, detail="Item Not Found")
  return found_item

# 名前検索
@router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
# Queryパラメーターでバリデーションの設定
async def find_by_name(name: str = Query(min_length=2, max_length=20)):
  return item_cruds.find_by_name(name)

# 登録処理
@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(create_item: ItemCreate):
  return item_cruds.create(create_item)

# 更新処理
@router.put("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def item_update(item_update: ItemUpdate, id: int = Path(gt=0)):
  update_item = item_cruds.update(id, item_update)
  if not update_item:
    raise HTTPException(status_code=404, detail="Item Not Update")
  return update_item

# 削除処理
@router.delete("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def item_delete(id: int = Path(gt=0)):
  deleted_item= item_cruds.delete(IsADirectoryError)
  if not deleted_item:
    raise HTTPException(status_code=404, detail="Item Not Deleted")
  return deleted_item