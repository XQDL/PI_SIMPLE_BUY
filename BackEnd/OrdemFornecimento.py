class OrdemFornecimento:
    def __init__(self, id, itens, valorUnitario, icms, ipi, frete, fornecedor, contratante, dataEntrega, comprador):
        self.id = id
        self.itens = itens
        self.valorUnitario = valorUnitario
        self.icms = icms
        self.ipi = ipi
        self.frete = frete
        self.fornecedor = fornecedor
        self.contratante = contratante
        self.dataEntrega = dataEntrega
        self.comprador = comprador