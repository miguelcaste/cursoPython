# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
  
##
## Definición y creación de la base de datos
##
Base = declarative_base()
  
class Departamento(Base):
    # tabla
    __tablename__ = 'departmento'
    
    #columnas
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
 
class Empleado(Base):
    # tabla
    __tablename__ = 'empleado'
    
    # columnas
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    
    # cada empleado está relacionado con un departamento
    departmento = relationship(
        Departmento,
        backref=backref('empleados',
                         uselist=True,
                         cascade='delete,all'))
##
## Creación del gestor de base de datos tipo SQLite
##
from sqlalchemy import create_engine
motor = create_engine('sqlite:///miempresa.sqlite')

# Creamos un gestor de conexiones (sesión)
from sqlalchemy.orm import sessionmaker
sesion = sessionmaker()
sesion.configure(bind=motor)
Base.metadata.create_all(motor)

##
## Ejemplos de trabajo con la base de datos anterior
##
d = Departmento(name="Informática")
emp1 = Empleado(name="Alan Turing", departmento=d)
s = session()
s.add(d)
s.add(emp1)
s.commit() 
resultado = s.query(Employee).all()
print(resultado)
s.delete(d)  
s.commit()
resultado = s.query(Employee).all()
print(resultado)