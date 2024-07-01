import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from eralchemy2 import render_er
import datetime

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(50))
    eye_color = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(50))
    height = Column(String(50))
    mass = Column(String(50))
    skin_color = Column(String(50))
    homeworld = Column(String(250))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    films = relationship('Film', secondary='people_films', backref='characters')
    starships = relationship('Starship', secondary='people_starships', backref='pilots')
    vehicles = relationship('Vehicle', secondary='people_vehicles', backref='pilots')
    species = relationship('Species', secondary='species_people', backref='people')
    planets = relationship('Planet', secondary='planets_people', backref='residents')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_year': self.birth_year,
            'eye_color': self.eye_color,
            'gender': self.gender,
            'hair_color': self.hair_color,
            'height': self.height,
            'mass': self.mass,
            'skin_color': self.skin_color,
            'homeworld': self.homeworld,
            'created': self.created,
            'edited': self.edited,
        }

class Film(Base):
    __tablename__ = 'film'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(String)
    director = Column(String(250))
    producer = Column(String(250))
    release_date = Column(DateTime)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    species = relationship('Species', secondary='species_films', backref='films')
    starships = relationship('Starship', secondary='starships_films', backref='films')
    vehicles = relationship('Vehicle', secondary='vehicles_films', backref='films')
    planets = relationship('Planet', secondary='planets_films', backref='films')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'episode_id': self.episode_id,
            'opening_crawl': self.opening_crawl,
            'director': self.director,
            'producer': self.producer,
            'release_date': self.release_date,
            'created': self.created,
            'edited': self.edited,
        }

class Starship(Base):
    __tablename__ = 'starship'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(50))
    length = Column(String(50))
    crew = Column(String(50))
    passengers = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    hyperdrive_rating = Column(String(50))
    MGLT = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    films = relationship('Film', secondary='starships_films', backref='starships')
    pilots = relationship('Person', secondary='people_starships', backref='starships')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'starship_class': self.starship_class,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'crew': self.crew,
            'passengers': self.passengers,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'created': self.created,
            'edited': self.edited,
        }

class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    length = Column(String(50))
    cost_in_credits = Column(String(50))
    crew = Column(String(50))
    passengers = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    films = relationship('Film', secondary='vehicles_films', backref='vehicles')
    pilots = relationship('Person', secondary='people_vehicles', backref='vehicles')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'vehicle_class': self.vehicle_class,
            'manufacturer': self.manufacturer,
            'length': self.length,
            'cost_in_credits': self.cost_in_credits,
            'crew': self.crew,
            'passengers': self.passengers,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'created': self.created,
            'edited': self.edited,
        }

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250))
    designation = Column(String(250))
    average_height = Column(String(50))
    average_lifespan = Column(String(50))
    eye_colors = Column(String(250))
    hair_colors = Column(String(250))
    skin_colors = Column(String(250))
    language = Column(String(250))
    homeworld = Column(String(250))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    people = relationship('Person', secondary='species_people', backref='species')
    films = relationship('Film', secondary='species_films', backref='species')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'classification': self.classification,
            'designation': self.designation,
            'average_height': self.average_height,
            'average_lifespan': self.average_lifespan,
            'eye_colors': self.eye_colors,
            'hair_colors': self.hair_colors,
            'skin_colors': self.skin_colors,
            'language': self.language,
            'homeworld': self.homeworld,
            'created': self.created,
            'edited': self.edited,
        }

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(50))
    rotation_period = Column(String(50))
    orbital_period = Column(String(50))
    gravity = Column(String(50))
    population = Column(String(50))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(50))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    residents = relationship('Person', secondary='planets_people', backref='planets')
    films = relationship('Film', secondary='planets_films', backref='planets')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'diameter': self.diameter,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'gravity': self.gravity,
            'population': self.population,
            'climate': self.climate,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'created': self.created,
            'edited': self.edited,
        }
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
