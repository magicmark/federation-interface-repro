import typing
import strawberry
from strawberry.federation.schema_directives import Shareable, External, Requires


@strawberry.interface
class Foo:
    foo: str


@strawberry.type(directives=[Shareable()])
class Bar(Foo):
    bar: str


@strawberry.type(directives=[Shareable()])
class Baz(Foo):
    baz: str


@strawberry.federation.type(keys=["id"])
class HelloWorld:
    id: strawberry.ID
    child: Foo = strawberry.field(directives=[External()])

    @strawberry.field(
        directives=[
            Requires(
                fields="child { __typename foo ... on Bar { bar } ... on Baz { baz } }"
            )
        ]
    )
    def qux(self) -> str:
        # Developer wants to read `self.child`` here to discern if it's a Bar or Baz
        print(self.child)
        return "hello from bar"

    # ⬇️ Uncomment this to fix!
    # @classmethod
    # def resolve_reference(cls, id: strawberry.ID, child: Foo) -> "HelloWorld":
    #     return HelloWorld(id=id, child=child)


@strawberry.type
class Query:
    _hi: str = strawberry.field(resolver=lambda: "Hello World!")


schema = strawberry.federation.Schema(
    query=Query, types=[HelloWorld, Bar, Baz], enable_federation_2=True
)
