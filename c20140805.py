import json

data = [{'a':'A', 'b':(2,4), 'c':3.0}]

print 'DATA:', repr(data)

data_string = json.dumps(data, sort_keys=True, indent=2)

print 'JSON:', data_string

print 'ENCODED:', data_string

decoded = json.loads(data_string)
print 'DECODED:', decoded

print 'ORIGINAL:', type(data[0]['b'])
print 'DECODED :', type(decoded[0]['b'])


