import os
import sys
from xmlrpc.client import DateTime
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

from sqlalchemy import create_engine, Column, String, Integer, Date, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

people_films = Table('people_films', Base.metadata,
    Column('people_id', String, ForeignKey('people.url'), primary_key=True),
    Column('film_id', String, ForeignKey('films.url'), primary_key=True)
)

starships_films = Table('starships_films', Base.metadata,
    Column('starship_id', String, ForeignKey('starships.url'), primary_key=True),
    Column('film_id', String, ForeignKey('films.url'), primary_key=True)
)

people_starships = Table('people_starships', Base.metadata,
    Column('people_id', String, ForeignKey('people.url'), primary_key=True),
    Column('starship_id', String, ForeignKey('starships.url'), primary_key=True)
)

vehicles_films = Table('vehicles_films', Base.metadata,
    Column('vehicle_id', String, ForeignKey('vehicles.url'), primary_key=True),
    Column('film_id', String, ForeignKey('films.url'), primary_key=True)
)

people_vehicles = Table('people_vehicles', Base.metadata,
    Column('people_id', String, ForeignKey('people.url'), primary_key=True),
    Column('vehicle_id', String, ForeignKey('vehicles.url'), primary_key=True)
)

species_films = Table('species_films', Base.metadata,
    Column('species_id', String, ForeignKey('species.url'), primary_key=True),
    Column('film_id', String, ForeignKey('films.url'), primary_key=True)
)

species_people = Table('species_people', Base.metadata,
    Column('species_id', String, ForeignKey('species.url'), primary_key=True),
    Column('people_id', String, ForeignKey('people.url'), primary_key=True)
)

planets_films = Table('planets_films', Base.metadata,
    Column('planet_id', String, ForeignKey('planets.url'), primary_key=True),
    Column('film_id', String, ForeignKey('films.url'), primary_key=True)
)

planets_people = Table('planets_people', Base.metadata,
    Column('planet_id', String, ForeignKey('planets.url'), primary_key=True),
    Column('people_id', String, ForeignKey('people.url'), primary_key=True)
)

class People(Base):
    __tablename__ = 'people'
    name = Column(String, nullable=False)
    birth_year = Column(String)
    eye_color = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    mass = Column(String)
    skin_color = Column(String)
    homeworld = Column(String)
    url = Column(String, primary_key=True)
    created = Column(DateTime)
    edited = Column(DateTime)
    films = relationship('Film', secondary=people_films, back_populates='characters')
    starships = relationship('Starship', secondary=people_starships, back_populates='pilots')
    vehicles = relationship('Vehicle', secondary=people_vehicles, back_populates='pilots')
    species = relationship('Species', secondary=species_people, back_populates='people')
    planets = relationship('Planet', secondary=planets_people, back_populates='residents')

class Film(Base):
    __tablename__ = 'films'
    title = Column(String, nullable=False)
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(String)
    director = Column(String)
    producer = Column(String)
    release_date = Column(Date)
    species = relationship('Species', secondary=species_films, back_populates='films')
    starships = relationship('Starship', secondary=starships_films, back_populates='films')
    vehicles = relationship('Vehicle', secondary=vehicles_films, back_populates='films')
    characters = relationship('People', secondary=people_films, back_populates='films')
    planets = relationship('Planet', secondary=planets_films, back_populates='films')
    url = Column(String, primary_key=True)
    created = Column(DateTime)
    edited = Column(DateTime)

class Starship(Base):
    __tablename__ = 'starships'
    name = Column(String, nullable=False)
    model = Column(String)
    starship_class = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(String)
    crew = Column(String)
    passengers = Column(String)
    max_atmosphering_speed = Column(String)
    hyperdrive_rating = Column(String)
    MGLT = Column(String)
    cargo_capacity = Column(String)
    consumables = Column(String)
    films = relationship('Film', secondary=starships_films, back_populates='starships')
    pilots = relationship('People', secondary=people_starships, back_populates='starships')
    url = Column(String, primary_key=True)
    created = Column(DateTime)
    edited = Column(DateTime)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    name = Column(String, nullable=False)
    model = Column(String)
    vehicle_class = Column(String)
    manufacturer = Column(String)
    length = Column(String)
    cost_in_credits = Column(String)
    crew = Column(String)
    passengers = Column(String)
    max_atmosphering_speed = Column(String)
    cargo_capacity = Column(String)
    consumables = Column(String)
    films = relationship('Film', secondary=vehicles_films, back_populates='vehicles')
    pilots = relationship('People', secondary=people_vehicles, back_populates='vehicles')
    url = Column(String, primary_key=True)
    created = Column(DateTime)
    edited = Column(DateTime)

class Species(Base):
    __tablename__ = 'species'
    name = Column(String, nullable=False)
    classification = Column(String)
    designation = Column(String)
    average_height = Column(String)
    average_lifespan = Column(String)
    eye_colors = Column(String)
    hair_colors = Column(String)
    skin_colors = Column(String)
    language = Column(String)
    homeworld = Column(String)
    people = relationship('People', secondary=species_people, back_populates='species')
    films = relationship('Film', secondary=species_films, back_populates='species')
    url = Column(String, primary_key=True)
    created = Column(DateTime)
    edited = Column(DateTime)

class Planet(Base):
    __tablename__ = 'planets'
    name = Column(String, nullable=False)
    diameter = Column(String)
    rotation_period = Column(String)
    orbital_period = Column(String)
    gravity = Column(String)
    population = Column(String)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(String)
    residents = relationship('People', secondary=planets_people, back_populates='planets')
    films = relationship('Film', secondary=planets_films, back_populates='planets')
    url = Column(String, primary_key=True)
    created = Column(DateTime)
    edited = Column(DateTime)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
