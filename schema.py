import graphene


class Person(graphene.ObjectType):

    name = graphene.String()
    age = graphene.Float()
    id = graphene.Int()

# Database of Person(s)
p1 = Person()
p2 = Person()


p1.id = 1
p1.age = 34
p1.name = 'Jack'

persons = [p1, p2]

class Query(graphene.ObjectType):

    person = graphene.Field(Person, id=graphene.Int())
    def resolve_person(self, args, info):
        for p in persons:
            if p.id == args.get('id'):
                return p

schema = graphene.Schema(query=Query)
