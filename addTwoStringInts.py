def add_two_string_numbers(s1: str, s2: str) -> str:
    def _do_add(longer: str, shorter: str) -> str:
        ans = ''
        carry = 0
        longer_ix = shorter_ix = 0
        longer, shorter = longer[::-1], shorter[::-1]
        while longer_ix < len(longer):
            short_digit = 0 if shorter_ix >= len(shorter) else int(shorter[shorter_ix])
            addition = int(longer[longer_ix]) + short_digit + carry
            if addition < 10:
                ans += str(addition)
                carry = 0
            else:
                ans += str(addition)[-1]
                carry = 1

            longer_ix += 1
            shorter_ix += 1

        if carry:
            ans += '1'

        return ans[::-1]

    if len(s2) > len(s1):
        return _do_add(s2, s1)
    else:
        return _do_add(s1, s2)


print(add_two_string_numbers('12', '34'), '46')
print(add_two_string_numbers('99', '9'), '108')
print(add_two_string_numbers('109', '109'), '218')
print(add_two_string_numbers('100000000000000000000000000000000000', '1'), '100000000000000000000000000000000001')