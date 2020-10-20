""" This modules provides parsers to the different jobs enqueuing. These parsers control
the expected input for the API's endpoints"""
from flask_restx import Namespace
from flask_restx import inputs
from flask_restx.reqparse import RequestParser


def tag_search_parser(api: Namespace) -> RequestParser:
    """
    Controls the expected input for the tag search jobs
    """
    parser = api.parser()
    parser.add_argument(
        "start_date",
        type=inputs.date_from_iso8601,
        required=True,
        help="Starting date for topic search. (Expected string format: dd/mm/AAAA)",
        location="json",
    )
    parser.add_argument(
        "end_date",
        type=inputs.date_from_iso8601,
        required=True,
        help="Ending date for topic search. (Expected string format: dd/mm/AAAA)",
        location="json",
    )
    parser.add_argument("tag", type=str, location="json", required=True)
    return parser


def keywords_search_parser(api: Namespace) -> RequestParser:
    """
    Controls the expected input for the keywords search jobs
    """
    parser = api.parser()
    parser.add_argument(
        "start_date",
        type=inputs.date_from_iso8601,
        required=True,
        help="Starting date for keywords search. (Expected string format: dd/mm/AAAA)",
        location="json",
    )
    parser.add_argument(
        "end_date",
        type=inputs.date_from_iso8601,
        required=True,
        help="Ending date for keywords search. (Expected string format: dd/mm/AAAA)",
        location="json",
    )
    parser.add_argument("keywords", type=str, location="json", required=True)
    return parser


def url_search_parser(api: Namespace) -> RequestParser:
    """
    Controls the expected input for the url search jobs
    """
    parser = api.parser()
    # Add 'url' query param. Accepts multiple instances
    parser.add_argument(
        "url",
        type=list,
        help="News URL(s) to extract info.",
        location="json",
        required=True,
    )

    return parser
