"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example:

    >>> reverseInParentheses("(bar)")
    'rab'

    >>> reverseInParentheses("foo(bar)baz")
    'foorabbaz'

    >>> reverseInParentheses("foo(bar)baz(blim)")
    'foorabbazmilb'

    >>> reverseInParentheses("foo(bar(baz))blim")
    'foobazrabblim'

    Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

"""

from collections import deque

def reverseInParentheses(inputString):

    st = []
    q = deque()
    
    for char in inputString:
        if char == ')':
            st_char = st.pop()
            while st_char != '(':
                q.append(st_char)
                st_char = st.pop()
            while q:
                st.append(q.popleft())
        else:
            st.append(char)
            
    return "".join(st)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
