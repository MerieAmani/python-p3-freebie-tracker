#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data (optional, for repeatable seeding)
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()

# Create companies
c1 = Company(name="Google", founding_year=1998)
c2 = Company(name="Microsoft", founding_year=1975)
session.add_all([c1, c2])
session.commit()

# Create devs
d1 = Dev(name="Alice")
d2 = Dev(name="Bob")
session.add_all([d1, d2])
session.commit()

# Create freebies
f1 = Freebie(item_name="T-shirt", value=20, company=c1, dev=d1)
f2 = Freebie(item_name="Sticker", value=2, company=c1, dev=d2)
f3 = Freebie(item_name="Mug", value=10, company=c2, dev=d1)
session.add_all([f1, f2, f3])
session.commit()

print("Database seeded!")
