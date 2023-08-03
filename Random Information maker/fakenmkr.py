# pip install faker
import faker
from faker import Faker

fake = Faker()
fname = "Fake Name : " + fake.name() + "\n"
faddrs = "Fake Address : " + fake.address()

print(fname, faddrs)