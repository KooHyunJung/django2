from typing import Tuple

from django.http import HttpRequest
from ninja import Router

from tabom.apis.v1.schemas.like_request import LikeRequest
from tabom.apis.v1.schemas.like_response import LikeResponse
from tabom.models import Like
from tabom.services.like_service import do_like, undo_like

router = Router()

@router.post("/", response={201: LikeResponse})
def post_like(request: HttpRequest, like_request: LikeRequest) -> Tuple[int, Like]:
    like = do_like(user_id=like_request.user_id, article_id=like_request.article_id)
    return 201, like



@router.delete("/", response={204: None})
def delate_like(request: HttpRequest, user_id: int, article_id: int) -> Tuple[int, None]:
    undo_like(user_id, article_id)
    # delate 동작은 바디를 안 쓰는 것이 표준. 안전한 방법.
    # 204: 노 콘텐츠. 성공한 것만 알려주고 아무것도 리턴하지 않는다.
    return 204, None