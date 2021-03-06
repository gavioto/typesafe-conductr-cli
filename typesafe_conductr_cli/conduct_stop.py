from typesafe_conductr_cli import bundle_utils, conduct_url, conduct_logging
import json
import requests


@conduct_logging.handle_connection_error
@conduct_logging.handle_http_error
def stop(args):
    """`conduct stop` command"""

    path = 'bundles/{}?scale=0'.format(args.bundle)
    url = conduct_url.url(path, args)
    response = requests.put(url)
    conduct_logging.raise_for_status_inc_3xx(response)

    if (args.verbose):
        conduct_logging.pretty_json(response.text)

    response_json = json.loads(response.text)
    bundleId = response_json['bundleId'] if args.long_ids else bundle_utils.short_id(response_json['bundleId'])

    print('Bundle stop request sent.')
    print('Unload bundle with: conduct unload{} {}'.format(args.cli_parameters, bundleId))
    print('Print ConductR info with: conduct info{}'.format(args.cli_parameters))
