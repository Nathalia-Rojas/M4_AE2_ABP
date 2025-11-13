
class TarjetaCredito:
    tarjetas = []

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas.append(self)  

    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self  

    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0  
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    @classmethod
    def mostrar_todas(cls):
        print("\nInformación de todas las tarjetas:")
        for i, tarjeta in enumerate(cls.tarjetas, start=1):
            print(f"Tarjeta {i} → Saldo: ${tarjeta.saldo_pagar:.2f} / Límite: ${tarjeta.limite_credito} / Interés: {tarjeta.intereses * 100}%")
        print("-" * 50)

tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.03)
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.05)

# Primera tarjeta: 
tarjeta1.compra(200).compra(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Segunda tarjeta: 
tarjeta2.compra(500).compra(700).compra(200).pago(300).pago(200).cobrar_interes().mostrar_info_tarjeta()

# Tercera tarjeta: 
tarjeta3.compra(100).compra(150).compra(100).compra(120).compra(80).mostrar_info_tarjeta()

TarjetaCredito.mostrar_todas()
