from mathics.session import MathicsSession

session = MathicsSession(add_builtin=True, catch_interrupt=False)


def check_evaluation(str_expr: str, expected: str, message=""):
    """Helper function to test that a Mathics expression against
    its results"""
    result = session.evaluate(str_expr).value

    if message:
        assert result == expected, f"{message}: got: {result}"
    else:
        assert result == expected


def test_hello():
    session.evaluate('LoadModule["pymathics.hello"]') == "pymathics.hello"
    check_evaluation('Hello["World"]', "Hello, World!")
