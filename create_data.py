from capp import db
db.create_all()

from capp.models import User
user1=User(username='Bjørk', email='bjørk@demo.com', password='regn')
db.session.add(user1)
user2=User(username='Fjell', email='fjell@demo.com', password='regn')
db.session.add(user2)
db.session.commit()

from capp.models import Transport 
transport1 = Transport(kms=10, transport='Car', fuel='Gasoline Small', co2=0.050, ch4=0, total=10 * 0.050, user_id=user1.id)
transport2 = Transport(kms=15, transport='Bus', fuel='Diesel', co2=0.030, ch4=0, total=15 * 0.030, user_id=user1.id)
db.session.add(transport1) 
db.session.add(transport2)
transport3 = Transport(kms=5, transport='Train', fuel='Electric Nordic', co2=0.007, ch4=0, total=5 * 0.007, user_id=user2.id)
transport4 = Transport(kms=7, transport='Plane', fuel='Economy', co2=7 * 0.127, ch4=0, total=7 * 0.127, user_id=user2.id)
db.session.add(transport3) 
db.session.add(transport4) 
db.session.commit()

#Some basic queries
user1 = User.query.get(1)
user2 = User.query.get(2)
transport1 = Transport.query.first()
transport1.user_id
transport1.author
transport1.author.username
