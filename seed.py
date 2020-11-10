"""seed file to make sample data"""

from models import Pet, db
from app import app

def drop_everything():
    """(On a live db) drops all foreign key constraints before dropping all tables.
    Workaround for SQLAlchemy not doing DROP ## CASCADE for drop_all()
    (https://github.com/pallets/flask-sqlalchemy/issues/722)
    """
    from sqlalchemy.engine.reflection import Inspector
    from sqlalchemy.schema import DropConstraint, DropTable, MetaData, Table

    con = db.engine.connect()
    trans = con.begin()
    inspector = Inspector.from_engine(db.engine)

    # We need to re-create a minimal metadata with only the required things to
    # successfully emit drop constraints and tables commands for postgres (based
    # on the actual schema of the running instance)
    meta = MetaData()
    tables = []
    all_fkeys = []

    for table_name in inspector.get_table_names():
        fkeys = []

        for fkey in inspector.get_foreign_keys(table_name):
            if not fkey["name"]:
                continue

            fkeys.append(db.ForeignKeyConstraint((), (), name=fkey["name"]))

        tables.append(Table(table_name, meta, *fkeys))
        all_fkeys.extend(fkeys)

    for fkey in all_fkeys:
        con.execute(DropConstraint(fkey))

    for table in tables:
        con.execute(DropTable(table))

    trans.commit()

#create all tables
drop_everything()
#db.drop_all()
db.create_all()

#if table isn't empty, empty it
Pet.query.delete()


#add pets
p1 = Pet(name='Leo', species='Lion', photo_url='https://images.unsplash.com/photo-1573725342230-178c824a10f2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=951&q=80', age=3, notes='A big lion', is_available=True)
p2 = Pet(name='Carole B', species='Tiger', photo_url='https://images.unsplash.com/photo-1551972251-12070d63502a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80', age=2, notes='A tiger rescued from Joe', is_available=True)
p3 = Pet(name='Fergus', species='Pig', photo_url='https://images.unsplash.com/photo-1583205188670-ce90796eb01c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=975&q=80', age=31, notes='A particularly dirty pig', is_available=True)
p4 = Pet(name='Pat', species='Pig', photo_url='https://images.unsplash.com/photo-1591175660774-2a59438ceaf5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1494&q=80', age=1, notes='A cute teacup pig', is_available=False)
p5 = Pet(name='Cookie', species='Cat', photo_url='https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80', age=1, is_available=False)
p6 = Pet(name='Smurf', species='Cat', photo_url='https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1454&q=80', age=4, is_available=False)

#add new objects to session, so they persist
db.session.add_all([p1, p2, p3, p4, p5, p6])

#commit otherwise this won't save
db.session.commit()



