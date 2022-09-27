#!/usr/bin/python
#-*- coding: utf-8 -*-

class clip:
    def __init__(self):
        self.nombreUs = None
        self.apPat = None
        self.curp = None
        self.nombNeg = None
        self.calleNeg = None

    def dircFormPer(self, ):
        self.nombreUs=input('Ingresa tu Nombre: ')
        self.apPat=input('Ingresa tu apellido paterno: ')
        self.curp=input('Ingresa tu curp: ')

    def direcFormNeg(self, ):
        self.nombNeg=input('Ingresa el nombre de tu negocio: ')
        self.calleNeg=input('Ingresa la calle de tu negocio: ')
        self.crearCuenta()

    def direcFormSol(self, ):
        print('Formulario de solicitud.')


    def mandarConf(self, ):
        print('Correo de confirmacion mandado')

    def crearCuenta(self, ):
        print('Cuenta creada satisfactoriamente.')

    def negarCuenta(self,):
        print('Ya existe una cuenta con esos datos')
