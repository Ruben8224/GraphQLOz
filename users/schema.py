from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        matricula = graphene.String(required=True)
        carrera = graphene.String(required=True)

    def mutate(self, info, username, password, email, matricula, carrera):
        user = get_user_model()(
            username=username,
            email=email,
            matricula=carrera,
            carrera=carrera
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        matricula = graphene.String(required=True)
        carrera = graphene.String(required=True)

    def mutate(self, info, username, password, email, matricula, carrera):
        user = get_user_model()(
            username=username,
            email=email,
            matricula=matricula,
            carrera=carrera
        )
        user.set_password(password)
        user.save()

        return UpdateUser(user=user)


class Query(graphene.AbstractType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user
