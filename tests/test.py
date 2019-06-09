from flake8_raise_httpexceptions import check as _check

X100 = "X100 httpexception found (return exception_response)"
X200 = "X200 httpexception found (return HTTPOk)"
X304 = "X304 httpexception found (return HTTPNotModified)"
X400 = "X400 httpexception found (return HTTPBadRequest)"


def check(line):
    """Check, but return a list not an iterator"""
    return list(_check(line))


def test_raise_httpexceptions():
    assert check("return exception_response") == [(0, X100)]
    assert check("return exception_response(") == [(0, X100)]
    assert check("return HTTPOk") == [(0, X200)]
    assert check("# return HTTPNotModified") == [(2, X304)]
    assert check("  return HTTPBadRequest") == [(2, X400)]
