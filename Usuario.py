#!/usr/bin/python
#-*- coding: utf-8 -*-
from clip import clip
import random
class Usuario:
    def __init__(self):
        self.correoElectronico = None
        self.contraseña = None
        self.Telefono = None

    def ingresarPaginaclip(self, ):
        print('Ingresaste a la pagina')
        self.solicitarCuenta()

    def solicitarCuenta(self, ):
        print('Solicitud enviada')
        cl=clip()
        cl.direcFormSol()
        self.llenarFormSol()
        aleat=random.randint(0,10)
        if aleat<=5:
            cl.mandarConf()
            print('Correo confirmado')
            self.llenarFormPer()
            cl.dircFormPer()
            self.llenarFormNeg()
            cl.direcFormNeg()
        else:
            cl.negarCuenta()

    def llenarFormSol(self, ):
        self.correoElectronico=input('Ingresa tu correo: ')
        self.contraseña=input('Ingresa tu contraseña: ')
        self.Telefono=input('Ingresa tu telefono: ')

    def llenarFormPer(self, ):
        print('Llena el diguiente formulario.')

    def llenarFormNeg(self, ):
        print('Llena el diguiente formulario.')
