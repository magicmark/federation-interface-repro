# Federation Interface Question Repro

**Instructions**

```bash
$ git clone git@github.com:magicmark/federation-interface-repro.git
$ cd federation-interface-repro
$ poetry install
$ make start # (or `poetry run supervisord`)
```

⚠️ If you're on a corporate VPN that intercepts DNS you may need to temporarily disconnect for `poetry install` to work.

### Playground

Once started up, you can access the playground here:

✨ [`http://localhost:4000/`](http://localhost:4000/) ✨

Copy and paste the above query to try it out:

```graphql
{
  helloWorld(barOrBaz: "baz") {
    qux
  }
}
```