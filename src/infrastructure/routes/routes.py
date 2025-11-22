from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from domain import get_settings, EpisodeInput, EpisodeFavoriteInput
import container


settings = get_settings()
prefix = f'/{settings.NAMESPACE}/api/{settings.API_VERSION}/{settings.RESOURCE}'

router = APIRouter(prefix=prefix)


@router.get('/liveness', tags=['Health Checks'])
def liveness() -> dict:
    return {'status': 'success'}


@router.get('/episodes', tags=['Episodes'])
def get_episodes() -> JSONResponse:
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.get_episodes()
        response = use_case.execute()
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)


@router.post('/episodes', tags=['Episodes'])
def create_episode(episode: EpisodeInput) -> JSONResponse:
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.create_episode()
        response = use_case.execute(episode)
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)


@router.get('/episodes/{id}', tags=['Episodes'])
def get_episode(id: int) -> JSONResponse:
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.get_episode()
        response = use_case.execute(id)
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)


@router.patch('/episodes/{id}/favorite', tags=['Episodes'])
def update_episode(id: int, episode: EpisodeFavoriteInput) -> JSONResponse:
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.update_episode()
        response = use_case.execute(id, episode)
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)


@router.delete('/episodes/{id}', tags=['Episodes'])
def delete_episode(id: int) -> JSONResponse:
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.delete_episode()
        response = use_case.execute(id)
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)


@router.post('/episodes/sync', tags=['Episodes'])
def sync_episodes() -> JSONResponse:
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.sync_episodes()
        response = use_case.execute()
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)