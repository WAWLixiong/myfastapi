from typing import Optional, List
import time
import asyncio
from fastapi import APIRouter, Response, status, Header, Cookie, Form
from fastapi.responses import HTMLResponse, PlainTextResponse

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'camera', 'phone']


async def time_consuming_functionality():
    await asyncio.sleep(10)
    return 'ok'


@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return products


@router.get('/all')
async def get_all_products():
    # return products
    await time_consuming_functionality()
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    # return response
    return response


@router.get('/withheader')
def get_products(
        response: Response,
        # custom_header: Optional[str] = Header()
        custom_header: Optional[List[str]] = Header(None),  # caution: None的话则不是必传的
        test_cookie: Optional[str] = Cookie(),
):
    # caution: /docs custom_header 传递多个值, custom_header 是一个元素的列表
    # postman 则不同
    # response的下划线不会转为dash
    if custom_header:
        response.headers['custom_response_header'] = ','.join(custom_header)
    return {
        'data': products,
        'custom_header': custom_header,
        'test_cookie': test_cookie,
    }


@router.get('/{id}', responses={
    status.HTTP_200_OK: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            }
        },
        "description": "Returns the HTML for an object"

    },
    status.HTTP_404_NOT_FOUND: {
        "content": {
            "text/plain": {
                "example": "Product not found",
            }
        },
        "description": "A cleartext error message"

    }
})
def get_product(id: int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(content=out, media_type="text/plain", status_code=status.HTTP_404_NOT_FOUND)
    else:
        product = products[id]
        out = f"""
        <head>
            <style>
            .product {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                bachground-color: lightblue;
                text-align: center;
            }}
            </style>
        </head>
        <div class="product">{product}</div>
        """
        return HTMLResponse(content=out, media_type="text/html")
