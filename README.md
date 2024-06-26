<a href="https://fonolo.com" target="_blank">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://cdn.fonolo.com/assets/github/logo_dark.svg">
  <img alt="Fonolo" src="https://cdn.fonolo.com/assets/github/logo_light.svg" width="400">
</picture>
</a>

# Python Client Library

The official Python binding for the Fonolo Call-Back Service.

## Prerequisites

Before using this library, you must have:

* A Fonolo Account; visit [fonolo.com](https://fonolo.com/) for more details.
* a valid Fonolo Account SID and Auth Token, available from the [Fonolo Portal](https://portal.fonolo.com/)
* Works with [ 2.6 / 2.7 / 3.2 / 3.3 ]

## Installation

```
pip install fonolo
```

## Quickstart

### Start a new Fonolo Call-Back:

    import fonolo

    try:
        client = fonolo.Client(<account sid>, <auth token>)

        res = client.callback().start({

            "fc_number": "14163662500",
            "fc_option": "CO529c5278b2cefeabc984506e785d8cb0"
        });

        print(res);

    except fonolo.FonoloException as err:
        print(err)


## Documentation

Full API documentation is available from the [Fonolo developer site.][fonolo dev site]

## Release History

### v1.0.2
* Added support for the /optin and /optins endpoints for viewing call-back opt-in requests.

### v1.0.1
* Added support for the pending call-backs view (/pending endpoint)
* Fixed a bug in the /calls endpoint when passing URL arguments.

### v1.0.0
* Added support for the realtime and scheduled call-backs view.
* Added support for the timezones endpoint.
* Initial release.

[fonolo dev site]:  https://fonolo.com/help/api/
