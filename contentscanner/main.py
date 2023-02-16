from contentscanner.ContentScanner import ContentScanner
from .exceptions.exceptions import ExceptionUrl, ExceptionGetWordlist
from argparse import ArgumentParser
from dotenv import load_dotenv
from asyncio import run
from sys import exit

import os


async def __run(args):
    if not args.path and os.getenv('WORDLIST'):
        load_dotenv()
        path = os.getenv('WORDLIST')
    else:
        path = ''
    try:
        content_scanner = ContentScanner(args.url, r'' + path)
    except ExceptionUrl:
        exit("Problem with given url.")
    else:
        try:
            await content_scanner.scan()
        except ExceptionGetWordlist:
            exit("Something went wrong while opening wordlist file.")


def main():
    parser = ArgumentParser(description='Web Content Scanner.')
    parser.add_argument(
            '--url', required=True, help="website's url"
        )
    parser.add_argument(
            '--path', required=False, help="wordlist's path"
        )
    args = parser.parse_args()
    run(__run(args))


if __name__ == '__main__':
    main()
