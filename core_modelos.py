class EstadoInvalidoError(Exception):
    pass


class TicketTecnico:
    ESTADOS = ["Abierto", "En Proceso", "Cerrado"]

    def __init__(self, ticket_id, titulo, prioridad):
        self._id = ticket_id
        self._titulo = titulo
        self._estado = "Abierto"
        self._prioridad = prioridad

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS:
            raise EstadoInvalidoError(f"Estado no válido: {nuevo_estado}")

        if self._estado == "Cerrado" and nuevo_estado == "En Proceso":
            raise EstadoInvalidoError("No se puede pasar de Cerrado a En Proceso")

        self._estado = nuevo_estado

    def calcular_sla(self):
        raise NotImplementedError("Debe implementarse en las clases hijas")

    def __str__(self):
        return f"Ticket {self._id} - {self._titulo} " f"({self._estado})"


class TicketHardware(TicketTecnico):

    def __init__(self, ticket_id, titulo, prioridad, componente):
        super().__init__(ticket_id, titulo, prioridad)
        self.componente = componente

    def calcular_sla(self):
        sla = {"Alta": 4, "Media": 8, "Baja": 24}
        return sla.get(self._prioridad, 24)


class TicketSoftware(TicketTecnico):

    def __init__(self, ticket_id, titulo, prioridad, sistema_operativo):
        super().__init__(ticket_id, titulo, prioridad)
        self.sistema_operativo = sistema_operativo

    def calcular_sla(self):
        sla = {"Alta": 2, "Media": 6, "Baja": 12}
        return sla.get(self._prioridad, 12)


if __name__ == "__main__":

    hw = TicketHardware(1, "Fallo de disco duro", "Alta", "Disco SSD")

    sw = TicketSoftware(2, "Error de aplicación", "Media", "Windows 11")

    print(hw)
    print("SLA:", hw.calcular_sla(), "horas")

    print(sw)
    print("SLA:", sw.calcular_sla(), "horas")

    hw.cambiar_estado("En Proceso")
    hw.cambiar_estado("Cerrado")

    try:
        hw.cambiar_estado("En Proceso")
    except EstadoInvalidoError as e:
        print("Error:", e)
