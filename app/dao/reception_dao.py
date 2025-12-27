from app.models import ReceptionSlip, Car
from app import db
from sqlalchemy import func
from datetime import datetime, date


def get_all_slips():
    return db.session.query(ReceptionSlip, Car)\
        .join(Car, ReceptionSlip.car_id == Car.id)\
        .order_by(ReceptionSlip.reception_date.desc())\
        .all()


def get_slip_by_id(slip_id):
    return db.session.query(ReceptionSlip, Car)\
        .join(Car, ReceptionSlip.car_id == Car.id)\
        .filter(ReceptionSlip.id == slip_id)\
        .first()


def get_slip_only_by_id(slip_id):
    return ReceptionSlip.query.get(slip_id)


def create_slip(car_id, description=None, status='pending'):
    slip = ReceptionSlip(
        car_id=car_id,
        description=description,
        status=status,
        reception_date=datetime.now()
    )
    db.session.add(slip)
    db.session.commit()
    return slip


def update_slip(slip_id, car_id=None, description=None, status=None):
    slip = ReceptionSlip.query.get(slip_id)
    if slip:
        if car_id is not None:
            slip.car_id = car_id
        if description is not None:
            slip.description = description
        if status is not None:
            slip.status = status
        db.session.commit()
    return slip


def update_slip_status(slip_id, status):
    slip = ReceptionSlip.query.get(slip_id)
    if slip:
        slip.status = status
        db.session.commit()
    return slip


def count_today_slips():
    today = date.today()
    return ReceptionSlip.query.filter(
        func.date(ReceptionSlip.reception_date) == today
    ).count()


def get_slips_by_status(statuses):
    return db.session.query(ReceptionSlip, Car)\
        .join(Car, ReceptionSlip.car_id == Car.id)\
        .filter(ReceptionSlip.status.in_(statuses))\
        .order_by(ReceptionSlip.reception_date.asc())\
        .all()
