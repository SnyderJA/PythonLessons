import string
import random
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(random.randint(8, 16))))
