async function mostrar_carrinho(){
    const resposta = await fetch("cardapio2")

    if (!resposta.ok){
        alert("ERRO AO CARREGAR O CARRINHO!")
    }else{
        const dados = await resposta.json()

        const preco_total = document.querySelector(".cart__total")

        const carrinho = document.querySelector(".cart__items")
        carrinho.innerHTML="";
        let total = 0
        for (let item of dados) {
            let linha =`<div class="cart__item">
                                    <img src=${item.foto}>
                                    <div class="container_info">
                                        <h1>${item.produto}</h1>
                                        <p>R$ ${item.preco}</p>
                                    </div>
                                    
                                </div>`
            total = total + item.preco
            carrinho.innerHTML += linha;
        }
        preco_total.textContent = `Total: R$ ${total}.00`
    };
}

mostrar_carrinho()