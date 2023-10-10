if(!localStorage.getItem("basket")) {
    localStorage.setItem("basket", JSON.stringify([]));
}

const products = document.querySelector(".products-wrapper");

async function getData() {
await fetch("db.json")
.then(async function(response) { return await response.json() })
.then(data => {
    let html="";
    data.products.forEach(product => {
        html+=`
        <div class="product-item">
            <div class="product-img-div">
                <img src="${product.img}" alt="">
            </div>
            <div class="product-item-details">
                <h3>${product.name}</h3>
                <span>${product.price}$</span>
            </div>
            <div class="item-add-btn-div">
                <button data-id=${product.id} data-name="${product.name}" data-price="${product.price}" data-img="${product.img}" class="btn-add">Add to Cart</button>
            </div>
        </div>
        `
    });

    products.innerHTML = html;

    itemBtns = document.querySelectorAll(".btn-add");

    let basket = JSON.parse(localStorage.getItem("basket"));

    itemBtns.forEach(btn => {
        btn.addEventListener("click", function() {
            if(localStorage.getItem("basket") == null){
                localStorage.setItem("basket", JSON.stringify([]))
            }
    
            let data_id = this.getAttribute("data-id");
            let data_price = this.getAttribute("data-price");
            let data_name = this.getAttribute("data-name");
            let data_img = this.getAttribute("data-img");
    
            let exist = basket.find(a => {
                return a.id == data_id;
            })
    
            if(exist == undefined){
                let item = {
                    id: data_id,
                    price: data_price,
                    count: 1,
                    image: data_img,
                    name: data_name
                }
                basket.push(item);
            }else{
                exist.count++
            }
    
            localStorage.setItem("basket", JSON.stringify(basket));
    
            getBasket();
        })
    })

})
.catch(ex => console.log(ex));
}
getData();

function getBasket() {
    let basket = JSON.parse(localStorage.getItem('basket'))
    console.log(basket);
    const products = document.querySelector(".cart-products-wrapper");

    let html = "";

    basket.forEach(item => {
        html+= `
        <div class="cart-product">
            <div class="product-image-div">
                <img src="${item.image}" alt="">
            </div>
            <div>
                <h4>
                    <a href="#">${item.name}</a>
                </h4>
                <h4>
                    <span>${item.price}$</span>
                    <span style="color: blue">count: ${item.count}</span>
                </h4>
            </div>
            <div>
                <img width="15x" src="./icons8-close.svg" alt="remove-item-svg">
            </div>
        </div>
        `
    })

    products.innerHTML = html;

}
getBasket();

        // If you don't want to use get all btns in fetch, you can use this version
        // let basket = localStorage.getItem("basket");
        // let res = JSON.parse(basket).find(prod => {
        //     return prod.id == btnId;
        // })
        // console.log(res);

