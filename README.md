webrpc-gen Python templates
===============================

This repo contains the Go templates used by the `webrpc-gen` cli to code-generate
webrpc Python server and client code.


## Usage

```
webrpc-gen -schema=example.ridl -target=python -out=./example.gen.py -server -client

# or 
webrpc-gen -schema=example.ridl -target=github.com/webrpc/gen-python@v0.12.0 -out=./example.gen.py -server -client

# or
webrpc-gen -schema=example.ridl -target=./local-go-templates-on-disk -out=./example.gen.py -server -client
```

As you can see, the `-target` supports default `python`, any git URI, or a local folder :)

### Set custom template variables
Change any of the following values by passing `-option="Value"` CLI flag to `webrpc-gen`.

| webrpc-gen -option   | Description                             | Default value              | Added in |
|----------------------|-----------------------------------------|----------------------------|----------|
| `-client`            | generate client code                    | unset (`false`)            |          |
| `-server`            | generate server code                    | unset (`false`)            |          |

Example:
```
webrpc-gen -schema=./proto.json -target=python -out server.gen.py -server
```

## Set custom Go field meta tags in your RIDL file

| CLI option flag           | Description                                                      |
|---------------------------|------------------------------------------------------------------|
| `+ python.field.name = ID`    | Set custom field name                                            |
| `+ python.field.type = int64` | Set custom field type (must be able to JSON unmarshal the value) |

Example:
```ridl
message User
  - id: uint64
    + python.field.name = ID
```
will result in
```go
TODO
```

## Examples

See [_examples](./_examples)

## LICENSE

[MIT LICENSE](./LICENSE)
