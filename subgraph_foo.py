import typing
import strawberry
from strawberry.federation.schema_directives import Shareable


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
    child: Foo


@strawberry.type
class Query:
    @strawberry.field
    def helloWorld(self, bar_or_baz: str) -> HelloWorld:
        if bar_or_baz == "bar":
            child = (Bar(foo="foo", bar="bar!"),)
        elif bar_or_baz == "baz":
            child = Baz(foo="foo", baz="baz!")
        else:
            raise ValueError("with_foo_or_bar may only be foo or bar.")

        return HelloWorld(id=1, child=child)


schema = strawberry.federation.Schema(
    query=Query, types=[HelloWorld, Foo, Bar, Baz], enable_federation_2=True
)
