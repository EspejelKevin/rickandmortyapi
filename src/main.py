from fastapi import FastAPI
import uvicorn

from infrastructure import router, SQLite
from domain import (ResourceNotFoundError, resource_not_found_handler,
                    ResourceAlreadyExistsError, resource_already_exists_handler,
                    InternalServerError, internal_server_handler,
                    BadRequestError, bad_request_handler,
                    ResourceConflictError, resource_conflict_handler, get_settings, Base)
import container


settings = get_settings()

tags = [
    {
        'name': 'Health Checks',
        'description': 'Endpoints to check service availability.'
    },
    {
        'name': 'Episodes',
        'description': 'Endpoints to manage episodes.'
    }
]

def on_start_up() -> None:
    Base.metadata.create_all(bind=SQLite._engine)
    container.SingletonContainer.init()

app = FastAPI(
    title='Ticketing System',
    openapi_tags=tags,
    on_startup=[on_start_up]
)
app.add_exception_handler(BadRequestError, bad_request_handler)
app.add_exception_handler(ResourceConflictError, resource_conflict_handler)
app.add_exception_handler(ResourceNotFoundError, resource_not_found_handler)
app.add_exception_handler(ResourceAlreadyExistsError, resource_already_exists_handler)
app.add_exception_handler(InternalServerError, internal_server_handler)
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.HOST,
                port=settings.PORT, reload=settings.RELOAD)