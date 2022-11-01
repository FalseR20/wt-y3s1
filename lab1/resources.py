from http import HTTPStatus

from flask_restful import Resource
from flask import request
from sqlalchemy.orm import Session
from typing import List

import db


class ArgsResource(Resource):
    @staticmethod
    def get():
        with db.Session() as session:
            session: Session
            all_employees: List[db.Employee] = session.query(db.Employee).all()
            data = {employee.name: employee.place for employee in all_employees}
            return data, HTTPStatus.OK

    # noinspection DuplicatedCode
    @staticmethod
    def post():
        if db.Employee.name.key not in request.args:
            return f"No `{db.Employee.name.key}`", HTTPStatus.BAD_REQUEST
        if db.Employee.place.key not in request.args:
            return f"No `{db.Employee.place.key}`", HTTPStatus.BAD_REQUEST
        with db.Session() as session:
            session: Session
            new_employee = db.Employee(name=request.args[db.Employee.name.key],
                                       place=request.args[db.Employee.place.key])
            session.add(new_employee)
            session.commit()
        return "", HTTPStatus.OK


class ParamsResource(Resource):
    @staticmethod
    def post(name, place):
        with db.Session() as session:
            session: Session
            new_employee = db.Employee(name=name, place=place)
            session.add(new_employee)
            session.commit()
        return "", HTTPStatus.OK


class FormResource(Resource):
    # noinspection DuplicatedCode
    @staticmethod
    def post():
        if db.Employee.name.key not in request.form:
            return f"No `{db.Employee.name.key}`", HTTPStatus.BAD_REQUEST
        if db.Employee.place.key not in request.form:
            return f"No `{db.Employee.place.key}`", HTTPStatus.BAD_REQUEST
        with db.Session() as session:
            session: Session
            new_employee = db.Employee(name=request.form[db.Employee.name.key],
                                       place=request.form[db.Employee.place.key])
            session.add(new_employee)
            session.commit()
        return "", HTTPStatus.OK
