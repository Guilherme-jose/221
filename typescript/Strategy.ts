interface DescontoStrategy {
    calculaDescontoTotal(itens: { item: string; preco: number}[]): number;
}

class CinquentaPorcentoDescontoStrategy implements DescontoStrategy {
    public calculaDescontoTotal(itens: { item: string; preco: number}[]): number {
        return (
            itens.reduce((soma, object) => {
                return soma + object.preco;
            }, 0) / 2
        );
    }
}

class PrimeiroItemDescontoStrategy implements DescontoStrategy {
    public calculaDescontoTotal(itens: { item: string; preco: number}[]): number {
        return (
            itens.reduce((soma, object) => {
                return soma + object.preco;
            }, 0) - itens[0].preco / 2
        );
    }
}

class Venda {

    private descontoStrategy: DescontoStrategy;

    constructor(descontoStrategy: DescontoStrategy) {
        this.descontoStrategy = descontoStrategy;
    }

    public setStrategy(descontoStrategy: DescontoStrategy) {
        this.descontoStrategy = descontoStrategy;
    }

    public getDescontoTotal(itens: { item: string; preco: number}[]): void {
        const total = this.descontoStrategy.calculaDescontoTotal(itens);
        console.log(total);
    }
} 

const carrinho = [
    { item: "Smartphone", preco: 1000},
    { item: "Notebook", preco: 2000}
]

const vendaBlackFriday = new Venda(new PrimeiroItemDescontoStrategy());
vendaBlackFriday.getDescontoTotal(carrinho);

vendaBlackFriday.setStrategy(new CinquentaPorcentoDescontoStrategy());
vendaBlackFriday.getDescontoTotal(carrinho);

const vendaNatal = new Venda(new CinquentaPorcentoDescontoStrategy());
vendaNatal.getDescontoTotal(carrinho);