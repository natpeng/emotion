import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import *

class User(SQLAlchemyObjectType):

    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node, )

class Emotion(SQLAlchemyObjectType):
  
    class Meta:
        model = EmotionModel
        interfaces = (graphene.relay.Node, )
        
class Query(graphene.ObjectType):
    
    node = graphene.relay.Node.Field()
    user = graphene.Field(User, uid = graphene.String())
    date = graphene.Field(Emotion, date = graphene.String())
    
    def resolve_user(self, args, context, info):
        query = User.get_query(context)
        uid = args.get('uid')
        return query.get(uid)

    def resolve_emotion(self, args, context, info):
        query = Emotion.get_query(context)
        date = args.get('date')
        return query.get(date)

schema = graphene.Schema(query=Query, types=[User])