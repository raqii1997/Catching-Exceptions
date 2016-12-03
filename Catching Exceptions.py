import sys

try:
    f = open('Authority.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error ({0}): {1}".format(e.errno,e.strerror)
except ValueError:
    print "Could not convert the data to an integer"
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

while True:
    try:
        b = int(raw_input("What's your File name in Authority.txt: "))
        break
    except ValueError:
        print "Sorry, but that's not a Valid number."
