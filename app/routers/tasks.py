from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv

from fastapi import Request

from fastapi import status

from fastapi.responses import (
    JSONResponse,
)

from fastapi.encoders import jsonable_encoder

from app.database.model import (
    Item,
    UpdateItem
)

from app.database import crud

router = InferringRouter()

@cbv(router=router)
class UnauthenticatedCBV:
    
    @router.get(path="/")
    async def retrieve_tasks(self, request: Request):
        items = await crud.retrieve_tasks()
        if not items:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={})
        return JSONResponse(status_code=status.HTTP_200_OK, content=items)

    @router.get(path="/{task_id}")
    async def retrieve_item(self, request: Request, task_id: str):
        context = {"request": request}
        item = await crud.retrieve_item(task_id)
        if not item:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={})
        return JSONResponse(status_code=status.HTTP_200_OK, content=item)
    
    @router.post(path="/")
    async def create_item(self, item: Item):
        item_dict = jsonable_encoder(item)
        new_item = await crud.create_item(item_dict)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=new_item)

    @router.delete(path="/{task_id}")
    async def delete_item(self, request: Request, task_id: str):
        res = await crud.delete_item(task_id)
        if not res:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={})
        return JSONResponse(status_code=status.HTTP_200_OK, content={})

    @router.put(path="/{task_id}")
    async def update_item(self, task_id: str, item: UpdateItem):
        item_dict = jsonable_encoder(item)
        res = await crud.update_item(task_id, item_dict)
        if not res:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={})
        return JSONResponse(status_code=status.HTTP_200_OK, content={})
    
    @router.delete(path="/")
    async def delete_all_items(self, request: Request):
        await crud.delete_all_items()
        return JSONResponse(status_code=status.HTTP_200_OK, content={})


@cbv(router=router)
class AuthenticatedCBV:
    pass