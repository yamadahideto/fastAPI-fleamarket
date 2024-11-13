from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ItemStatus(Enum):
  SOLD_OUT = "SOLD_OUT"
  ON_SALE = "ON_SALE"

# 商品作成のバリデーションを定義
class ItemCreate(BaseModel):
  name: str = Field(min_length=2, max_length=20, examples=["PC"])
  price: int = Field(gt=0, examples=[10000])
  description: Optional[str] = Field(default=None, examples=["美品です"])
  # exampleに設定した値がルーティングのSwaggerUIのExample Valueに表示される。

class  ItemUpdate(BaseModel):
  name: Optional[str] = Field(None, min_length=2, max_length=20, examples=["PC"])
  price: Optional[int] = Field(None, gt=0, examples=[1000])
  description: Optional[str] = Field(None, examples=["美品です"])
  status: Optional[ItemStatus] = Field(None, examples=[ItemStatus.SOLD_OUT])

# レスポンスの型の定義
class ItemResponse(BaseModel):
  id: int = Field(gt=0, examples=[1])
  name: str = Field(min_length=2, max_length=20, examples=["PC"])
  price: int = Field(gt=0, examples=[10000])
  description: Optional[str] = Field(None, examples=["美品です"])
  status: ItemStatus = Field(examples=[ItemStatus.ON_SALE])