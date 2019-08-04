import re

pattern = "((?P<login>\w+):(?P<password>\w+)@)?(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})(:(?P<port>\d+))?"

tests = [
	re.match(pattern, "12.34.56.789").groupdict(),
	re.match(pattern, "12.34.56.789:80").groupdict(),
	re.match(pattern, "john:pass@12.34.56.789:80").groupdict(),
]

print(tests)