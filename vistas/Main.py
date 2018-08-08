# coding=utf-8
from PyQt4.QtGui import QHBoxLayout, QApplication, QVBoxLayout

from libs.Botones import BotonMain
from libs.Etiquetas import EtiquetaTitulo
from libs.Utiles import LeerIni
from vistas.VistaBase import VistaBase


class MainView(VistaBase):

    def initUi(self):
        self.setGeometry(150, 150, 500, 150)
        self.setWindowTitle('Factura Electronica')
        self.layoutPpal = QVBoxLayout(self)
        self.lblTitulo = EtiquetaTitulo(texto="{}-{}".format(
            LeerIni(clave="nombre_sistema"), LeerIni(clave='EMPRESA', key='FACTURA')))
        self.layoutPpal.addWidget(self.lblTitulo)

        self.layoutBotones = QHBoxLayout()

        self.btnClientes = BotonMain(texto='&Clientes', imagen='imagenes/if_kuser_1400.png')
        self.layoutBotones.addWidget(self.btnClientes)

        self.btnFactura = BotonMain(texto='&Facturacion', imagen='imagenes/if_bill_416404.png')
        self.layoutBotones.addWidget(self.btnFactura)

        self.btnArticulo = BotonMain(texto='&Articulos', imagen='imagenes/if_product-sales-report_49607.png')
        self.layoutBotones.addWidget(self.btnArticulo)

        self.btnAFIP = BotonMain(texto='A&FIP', imagen='imagenes/logoafipfondoblanco.png')
        self.layoutBotones.addWidget(self.btnAFIP)

        self.btnCompras = BotonMain(texto='Compras', imagen='imagenes/compras.png')
        self.layoutBotones.addWidget(self.btnCompras)

        self.btnSeteo = BotonMain(texto='&Configuracion', imagen='imagenes/if_Settings-2_379349.png')
        self.layoutBotones.addWidget(self.btnSeteo)

        self.btnSalir = BotonMain(texto='&Salir', imagen='imagenes/if_Log Out_27856.png')
        self.layoutBotones.addWidget(self.btnSalir)

        self.layoutPpal.addLayout(self.layoutBotones)