from contentscanner.ContentScanner import ContentScanner
from .exceptions.exceptions import ExceptionUrl, ExceptionGetWordlist
from argparse import ArgumentParser
from
from asyncio import run
from sys import exit


async def __run(args):
    try:
        content_scanner = ContentScanner(args.url, r'' + args.path)
    except Exception as e:
        exit('Errore: {}'.format(e.with_traceback(None)))
    else:
        try:
            await content_scanner.scan()
        except ExceptionGetWordlist:
            exit("Something went wrong while opening wordlist file.")
        except ExceptionUrl:
            exit("Problem with given url.")


def main():
    parser = ArgumentParser(description='Web Content Scanner.')
    parser.add_argument("path", help="wordlist's path")
    parser.add_argument(
            '--path', default=False, action="store_true",
            required=True, help="wordlist's path"
        )
    parser.add_argument("url", help="website's url")
    parser.add_argument(
            '--url', default=False, action="store_true",
            required=True, help="website's url"
        )
    run(__run(parser.parse_args()))


if __name__ == '__main__':
    main()
