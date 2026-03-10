from fastapi import APIRouter
from .schemas import (
    EventSchema,
    EventListSchema,
    EventCreateSchema,
    EventUpdateSchema
)

router = APIRouter()

# List View
# GET /api/events


@router.get("/")
def read_events() -> EventListSchema:
    # a bunch of items in a table
    return {
        "items": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ],
        "count": 3
    }

# SEND DATA
# POST /api/events


@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    # a bunch of items in a table
    data = payload.model_dump()
    return {"id": 123, **data}


# GET /api/events/12
@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # a single row
    return {"id": event_id}


# PUT /api/events
@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    # a single row
    data = payload.model_dump()
    return {"id": event_id, **data}
