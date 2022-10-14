from typing import Optional, List, Dict

from fastapi import APIRouter, Body, Query, Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog'],
)


class Image(BaseModel): url: str


alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'val1'}
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version,
    }


@router.post('/new/{id}/comment')
def create_comment(
        blog: BlogModel,
        id: int,
        comment_title: str = Query(
            title='Id of the comment',
            description="Some description for comment_id",
            alias='commentId',
        ),
        comment_id: int = Path(
            None,
            gt=5,
            le=10,
        ),
        content: str = Body(
            ...,
            min_length=10,
            max_length=50,
            regex='^[a-z\s]*$',
        ),
        v: Optional[List[str]] = Query(
            ['1.0', '1.1', '1.2']
        )
):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'comment_id': comment_id,
        'content': content,
        'v': v,
    }


def require_dependency():
    return {'message': 'this is a dependency'}
