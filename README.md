# SimpleWebserviceMapper
The SimpleWebserviceMapper is an [interstate_love_song](https://github.com/ilpvfx/interstate_love_song) Plugin Mapper.  
It was devised in a hurry during the latest pandemic. It calls another webservice and uses that as the mapper.

## Settings

`base_url`: str; the url to the endpoint of the service, should preferably not end in "/".

`cookie_auth_url`: str; a url to an endpoint that accepts HTTP Basic Authentication and returns a token.

`cookie_name`: str; the name of the token to use.

`auth_username_suffix`: str; when sending the HTTP Basic auth, append this suffix to the username (`""`)

`domains`: Sequence[str]; list of available domains

The service must have two endpoints, fulfilling the requirements as described below.

### Example Config
```json
{
  ...
  "mapper": {
    "plugin": "SimpleWebserviceMapper",
    "settings": {
        "base_url": "http://resources.example.com",
        "cookie_auth_url": "http://resources.example.com/login",
        "cookie_name": "default_cookie_name",
        "auth_username_suffix": "",
        "domains": ["example.com"]
    }
  }
}
```

### Mapping endpoint

- The webservice must have an endpoint that either accepts the path "user=`<username>`" or the query param
    "user=`<username>`".

- The webservice shall return UTF-8 JSON of the following format:

```json
{
  "hosts": [
        {
            "name": "Bilbo Baggins",
            "hostname": "jrr.tolkien.com",
        },
        {
            "name": "Winston Smith",
            "hostname": "orwell.mil",
        }
    ]
}
```

- If everything works, Status 200. "No resources" should be indicated with an empty hosts list.

- Any other status codes (except redirects) are deemed as internal errors.

Thus if the `base_url` is `http://resources.example.com`, then it will do `GET` requests to
`http://resources.example.com/user=<username>`, with a `Authorization: Basic <b64>` header.

### Auth endpoint

- The webservice shall have an endpoint that matches <cookie_auth_endpoint>.

- This endpoint shall accept a HTTP Basic authentication header.

- On success, return Status 200 and set a cookie with name <cookie_name>.

- On auth failure, return Status 401.

- Any other status codes (except redirects) are deemed as internal errors.

The resources returned are presented to the PCOIP-client.
