from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor, last_name):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE last_name=%(last_name)s
        ORDER BY first_name"""
    cursor.execute(query, {"last_name":last_name})
    return cursor.fetchall()

@database_common.connection_handler
def get_distinc_cities(cursor):
    query = """
        SELECT DISTINCT city
        FROM mentor
    """
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def get_mentors_by_city_name(cursor, city_name):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city=%(city_name)s
        ORDER BY first_name 
    """
    cursor.execute(query, {"city_name":city_name})
    return cursor.fetchall()


@database_common.connection_handler
def get_applicants_by_name(cursor, applicant_name):
    query = """
        SELECT CONCAT(first_name, ' ', last_name) as full_name, phone_number
        FROM applicant WHERE first_name ILIKE %(name)s;
    """
    cursor.execute(query, {"name": applicant_name})
    return cursor.fetchall()

@database_common.connection_handler
def add_applicant(cursor, applicant_first_name, applicant_last_name, applicant_phone, applicant_email):
    query = """
        INSERT INTO applicant(first_name, last_name, phone_number, email, application_code) 
        VALUES (%(first_name)s, %(last_name)s, %(phone_number)s, %(email)s, '1234');
    """
    cursor.execute(query, {
        "first_name" : applicant_first_name,
        "last_name": applicant_last_name,
        "phone_number" : applicant_phone,
        "email" : applicant_email
    })
    return None