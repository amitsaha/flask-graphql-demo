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

p2.id = 2
p2.age = 31
p2.name = 'Adam'

persons = [p1, p2]

class Query(graphene.ObjectType):

    # Create a field on which we can query and the attributes
    # we allow to query on
    person = graphene.Field(Person, id=graphene.Int())
    def resolve_person(self, args, info):
        for p in persons:
            if p.id == args.get('id'):
                return p


class UpdatePerson(graphene.Mutation):
    # Result field
    person = graphene.Field(Person)

    # The input fields
    class Input:
        name = graphene.String()
        id = graphene.Int()

    @classmethod
    def mutate(cls, instance, args, info):
        name = args.get('name')
        for p in persons:
            if p.id == args.get('id'):
                p.name = name
                return UpdatePerson(person=p)

class UpdatePersonMutation(graphene.ObjectType):
    updatePerson = graphene.Field(UpdatePerson)

schema = graphene.Schema(query=Query, mutation=UpdatePersonMutation)
