import github3
import os
import sys
import argparse

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', dest='gh_user')
    parser.add_argument('--repo', dest='gh_repo')
    parser.add_argument('--tag', dest='gh_tag')
    parser.add_argument('files', nargs='+')
    args = parser.parse_args()
    return args


token = os.environ.get('GH_TOKEN', None)

if not token:
    sys.exit(1)
else:
    args = cli()
    gh = github3.login(token=token)
    repo = gh.repository(args.gh_user, args.gh_repo)
    release = repo.release_from_tag(args.gh_tag)
    for artifact in args.files:
        with open(artifact) as asset:
            release.upload_asset(content_type='text/plain', name='asset1',
                                 asset=asset)
