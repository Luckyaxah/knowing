from apiflask import APIFlask, Schema, input, output, abort
from apiflask.fields import Integer, String, DateTime
from apiflask.validators import Length, OneOf

from apiflask import APIBlueprint

from knowing.models import KnowledgeEntry
from knowing.extensions import db

knowledge_bp = APIBlueprint('knowledge', __name__)


class KnowledgeEntryInSchema(Schema):
    title = String(required=True, validate=Length(0, 254))
    content = String(required=True)

class KnowledgeEntryOutSchema(Schema):
    id = Integer()
    title = String()
    content = String()
    update_time = DateTime()

class PaginationInSchema(Schema):
    page = Integer(missing=1)
    per_page = Integer(missing=10)

@knowledge_bp.get('/knowledge_entries')
def get_knowledge_entries(page=1, pagination=10):
    kentries = KnowledgeEntry.query.paginate(page, pagination).items
    kentry_schema = KnowledgeEntryOutSchema(many=True)
    ret = kentry_schema.dump(kentries)
    return {"data": ret}

# another way to return many results

# @knowledge_bp.get('/knowledge_entries')
# @output(KnowledgeEntryOutSchema(many=True))
# def get_knowledge_entries():
#     kentries = KnowledgeEntry.query.all()
#     return kentries

@knowledge_bp.get('/knowledge_entry/<int:_id>')
@output(KnowledgeEntryOutSchema)
def get_knowledge_entry(_id):
    kentry = KnowledgeEntry.query.get(_id)
    return kentry


@knowledge_bp.post('/knowledge_entry')
@input(KnowledgeEntryInSchema)
@output(KnowledgeEntryOutSchema)
def create_knowledge_entry(data):
    kentry = KnowledgeEntry(**data)
    db.session.add(kentry)
    db.session.commit()
    return kentry

@knowledge_bp.patch('/knowledge_entry/<int:_id>')
@input(KnowledgeEntryInSchema)
@output(KnowledgeEntryOutSchema)
def patch_knowledge_entry(_id, data):
    kentry = KnowledgeEntry.query.get(_id)
    for attr, value in data.items():
        setattr(kentry, attr, value)
    db.session.add(kentry)
    db.session.commit()
    return kentry