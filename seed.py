from models import Pet, db  
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

Ren = Pet(name='Ren', species='dog', photo_url='https://www.nicepng.com/png/detail/325-3255932_ren-hoek-ren-from-ren-and-stimpy.png', age=17, notes='short-tempered, psychotic chihuahua')
Stimpy = Pet(name='Stimpy', species='cat', photo_url='https://cdn2.myminifactory.com/assets/object-assets/5fa45c597500d/images/720X720-stimp.jpg', age=3, notes='dimwitted and happy-go-lucky')

db.session.add(Ren)
db.session.add(Stimpy)

db.session.commit()