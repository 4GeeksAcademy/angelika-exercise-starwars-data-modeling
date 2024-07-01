import datetime
import os
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from eralchemy import render_er

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PeopleFilms(db.Model):
    __tablename__ = 'people_films'
    people_id = db.Column(db.String, db.ForeignKey('people.url'), primary_key=True)
    film_id = db.Column(db.String, db.ForeignKey('films.url'), primary_key=True)

class StarshipsFilms(db.Model):
    __tablename__ = 'starships_films'
    starship_id = db.Column(db.String, db.ForeignKey('starships.url'), primary_key=True)
    film_id = db.Column(db.String, db.ForeignKey('films.url'), primary_key=True)

class PeopleStarships(db.Model):
    __tablename__ = 'people_starships'
    people_id = db.Column(db.String, db.ForeignKey('people.url'), primary_key=True)
    starship_id = db.Column(db.String, db.ForeignKey('starships.url'), primary_key=True)

class VehiclesFilms(db.Model):
    __tablename__ = 'vehicles_films'
    vehicle_id = db.Column(db.String, db.ForeignKey('vehicles.url'), primary_key=True)
    film_id = db.Column(db.String, db.ForeignKey('films.url'), primary_key=True)

class PeopleVehicles(db.Model):
    __tablename__ = 'people_vehicles'
    people_id = db.Column(db.String, db.ForeignKey('people.url'), primary_key=True)
    vehicle_id = db.Column(db.String, db.ForeignKey('vehicles.url'), primary_key=True)

class SpeciesFilms(db.Model):
    __tablename__ = 'species_films'
    species_id = db.Column(db.String, db.ForeignKey('species.url'), primary_key=True)
    film_id = db.Column(db.String, db.ForeignKey('films.url'), primary_key=True)

class SpeciesPeople(db.Model):
    __tablename__ = 'species_people'
    species_id = db.Column(db.String, db.ForeignKey('species.url'), primary_key=True)
    people_id = db.Column(db.String, db.ForeignKey('people.url'), primary_key=True)

class PlanetsFilms(db.Model):
    __tablename__ = 'planets_films'
    planet_id = db.Column(db.String, db.ForeignKey('planets.url'), primary_key=True)
    film_id = db.Column(db.String, db.ForeignKey('films.url'), primary_key=True)

class PlanetsPeople(db.Model):
    __tablename__ = 'planets_people'
    planet_id = db.Column(db.String, db.ForeignKey('planets.url'), primary_key=True)
    people_id = db.Column(db.String, db.ForeignKey('people.url'), primary_key=True)

class People(db.Model):
    __tablename__ = 'people'
    url = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String)
    eye_color = db.Column(db.String)
    gender = db.Column(db.String)
    hair_color = db.Column(db.String)
    height = db.Column(db.String)
    mass = db.Column(db.String)
    skin_color = db.Column(db.String)
    homeworld = db.Column(db.String)
    created = db.Column(DateTime, default=datetime.datetime.utcnow)
    edited = db.Column(DateTime, default=datetime.datetime.utcnow)

    films = db.relationship('Film', secondary='people_films', backref=db.backref('characters', lazy='dynamic'))
    starships = db.relationship('Starship', secondary='starships_films', backref=db.backref('pilots', lazy='dynamic'))
    vehicles = db.relationship('Vehicle', secondary='vehicles_films', backref=db.backref('pilots', lazy='dynamic'))
    species = db.relationship('Species', secondary='species_people', backref=db.backref('people', lazy='dynamic'))
    planets = db.relationship('Planet', secondary='planets_people', backref=db.backref('residents', lazy='dynamic'))

    def to_dict(self):
        return {
            'url': self.url,
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

class Film(db.Model):
    __tablename__ = 'films'
    url = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    episode_id = db.Column(db.Integer, nullable=False)
    opening_crawl = db.Column(db.String)
    director = db.Column(db.String)
    producer = db.Column(db.String)
    release_date = db.Column(Date)
    created = db.Column(DateTime, default=datetime.datetime.utcnow)
    edited = db.Column(DateTime, default=datetime.datetime.utcnow)

    species = db.relationship('Species', secondary='species_films', backref=db.backref('films', lazy='dynamic'))
    starships = db.relationship('Starship', secondary='starships_films', backref=db.backref('films', lazy='dynamic'))
    vehicles = db.relationship('Vehicle', secondary='vehicles_films', backref=db.backref('films', lazy='dynamic'))
    planets = db.relationship('Planet', secondary='planets_films', backref=db.backref('films', lazy='dynamic'))

    def to_dict(self):
        return {
            'url': self.url,
            'title': self.title,
            'episode_id': self.episode_id,
            'opening_crawl': self.opening_crawl,
            'director': self.director,
            'producer': self.producer,
            'release_date': self.release_date,
            'created': self.created,
            'edited': self.edited,
        }

class Starship(db.Model):
    __tablename__ = 'starships'
    url = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    model = db.Column(db.String)
    starship_class = db.Column(db.String)
    manufacturer = db.Column(db.String)
    cost_in_credits = db.Column(db.String)
    length = db.Column(db.String)
    crew = db.Column(db.String)
    passengers = db.Column(db.String)
    max_atmosphering_speed = db.Column(db.String)
    hyperdrive_rating = db.Column(db.String)
    MGLT = db.Column(db.String)
    cargo_capacity = db.Column(db.String)
    consumables = db.Column(db.String)
    created = db.Column(DateTime, default=datetime.datetime.utcnow)
    edited = db.Column(DateTime, default=datetime.datetime.utcnow)

    films = db.relationship('Film', secondary='starships_films', backref=db.backref('starships', lazy='dynamic'))
    pilots = db.relationship('People', secondary='people_starships', backref=db.backref('starships', lazy='dynamic'))

    def to_dict(self):
        return {
            'url': self.url,
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

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    url = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    model = db.Column(db.String)
    vehicle_class = db.Column(db.String)
    manufacturer = db.Column(db.String)
    length = db.Column(db.String)
    cost_in_credits = db.Column(db.String)
    crew = db.Column(db.String)
    passengers = db.Column(db.String)
    max_atmosphering_speed = db.Column(db.String)
    cargo_capacity = db.Column(db.String)
    consumables = db.Column(db.String)
    created = db.Column(DateTime, default=datetime.datetime.utcnow)
    edited = db.Column(DateTime, default=datetime.datetime.utcnow)

    films = db.relationship('Film', secondary='vehicles_films', backref=db.backref('vehicles', lazy='dynamic'))
    pilots = db.relationship('People', secondary='people_vehicles', backref=db.backref('vehicles', lazy='dynamic'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
