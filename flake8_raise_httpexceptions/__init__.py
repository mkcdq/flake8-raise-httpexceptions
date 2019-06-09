import re
from typing import Dict, Iterator, Match, NewType, Tuple

from .metadata import NAME, VERSION
from .utils import Code, code_from

Flake8Message = NewType("Flake8Message", str)
Flake8Result = NewType("Flake8Result", Tuple[int, Flake8Message])

WORD_CODES: Dict[str, Code] = {
    "return exception_response": code_from("100"),  # noqa: X100
    "return HTTPOk": code_from("200"),  # noqa: X200
    "return HTTPCreated": code_from("201"),  # noqa: X201
    "return HTTPAccepted": code_from("202"),  # noqa: X202
    "return HTTPNonAuthoritativeInformation": code_from("203"),  # noqa: X203
    "return HTTPNoContent": code_from("204"),  # noqa: X204
    "return HTTPResetContent": code_from("205"),  # noqa: X205
    "return HTTPPartialContent": code_from("206"),  # noqa: X206
    "return HTTPMultipleChoices": code_from("300"),  # noqa: X300
    "return HTTPMovedPermanently": code_from("301"),  # noqa: X301
    "return HTTPFound": code_from("302"),  # noqa: X302
    "return HTTPSeeOther": code_from("303"),  # noqa: X303
    "return HTTPNotModified": code_from("304"),  # noqa: X304
    "return HTTPUseProxy": code_from("305"),  # noqa: X305
    "return HTTPTemporaryRedirect": code_from("307"),  # noqa: X307
    "return HTTPPermanentRedirect": code_from("308"),  # noqa: X308
    "return HTTPBadRequest": code_from("400"),  # noqa: X400
    "return HTTPUnauthorized": code_from("401"),  # noqa: X401
    "return HTTPPaymentRequired": code_from("402"),  # noqa: X402
    "return HTTPForbidden": code_from("403"),  # noqa: X403
    "return HTTPNotFound": code_from("404"),  # noqa: X404
    "return HTTPMethodNotAllowed": code_from("405"),  # noqa: X405
    "return HTTPNotAcceptable": code_from("406"),  # noqa: X406
    "return HTTPProxyAuthenticationRequired": code_from("407"),  # noqa: X407
    "return HTTPRequestTimeout": code_from("408"),  # noqa: X408
    "return HTTPConflict": code_from("409"),  # noqa: X409
    "return HTTPGone": code_from("410"),  # noqa: X410
    "return HTTPLengthRequired": code_from("411"),  # noqa: X411
    "return HTTPPreconditionFailed": code_from("412"),  # noqa: X412
    "return HTTPRequestEntityTooLarge": code_from("413"),  # noqa: X413
    "return HTTPRequestURITooLong": code_from("414"),  # noqa: X414
    "return HTTPUnsupportedMediaType": code_from("415"),  # noqa: X415
    "return HTTPRequestRangeNotSatisfiable": code_from("416"),  # noqa: X416
    "return HTTPExpectationFailed": code_from("417"),  # noqa: X417
    "return HTTPUnprocessableEntity": code_from("422"),  # noqa: X422
    "return HTTPLocked": code_from("423"),  # noqa: X423
    "return HTTPFailedDependency": code_from("424"),  # noqa: X424
    "return HTTPPreconditionRequired": code_from("428"),  # noqa: X428
    "return HTTPTooManyRequests": code_from("429"),  # noqa: X429
    "return HTTPRequestHeaderFieldsTooLarge": code_from("431"),  # noqa: X431
    "return HTTPInternalServerError": code_from("500"),  # noqa: X500
    "return HTTPNotImplemented": code_from("501"),  # noqa: X501
    "return HTTPBadGateway": code_from("502"),  # noqa: X502
    "return HTTPServiceUnavailable": code_from("503"),  # noqa: X503
    "return HTTPGatewayTimeout": code_from("504"),  # noqa: X504
    "return HTTPVersionNotSupported": code_from("505"),  # noqa: X505
    "return HTTPInsufficientStorage": code_from("507"),  # noqa: X507
}

# Find any one of the return statements definded above
RX_WORDS = re.compile("\\b({})\\b".format("|".join(WORD_CODES)))


def format_message(code: Code, word: str) -> Flake8Message:
    return Flake8Message("{} httpexception found ({})".format(code, word))


def match_to_flake8_result(match: Match[str]) -> Flake8Result:
    word = match.group(1)
    code = WORD_CODES[word]
    result = Flake8Result((match.start(), format_message(code, word)))
    return result


def check(physical_line: str) -> Iterator[Flake8Result]:
    matches = RX_WORDS.finditer(physical_line)
    results = map(match_to_flake8_result, matches)
    yield from results


check.name = NAME  # type: ignore
check.version = VERSION  # type: ignore
