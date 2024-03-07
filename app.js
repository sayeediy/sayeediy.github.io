let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let products = [
    { id: 1, name: 'Товар 1', count: 0 },
    { id: 2, name: 'Товар 2', count: 0 },
    { id: 3, name: 'Товар 3', count: 0 },
    { id: 4, name: 'Товар 4', count: 0 },
    { id: 5, name: 'Товар 5', count: 0 },
    { id: 6, name: 'Товар 6', count: 0 }
];

function updateCounter(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        product.count++;
        tg.MainButton.setText(`Вы выбрали ${product.name}! Количество: ${product.count}`);
        tg.MainButton.show();
    }
}

function setupButtonClickEvent(button, productId) {
    button.addEventListener("click", function () {
        if (tg.MainButton.isVisible) {
            tg.MainButton.hide();
        } else {
            updateCounter(productId);
        }
    });
}

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");
let btn5 = document.getElementById("btn5");
let btn6 = document.getElementById("btn6");

setupButtonClickEvent(btn1, 1);
setupButtonClickEvent(btn2, 2);
setupButtonClickEvent(btn3, 3);
setupButtonClickEvent(btn4, 4);
setupButtonClickEvent(btn5, 5);
setupButtonClickEvent(btn6, 6);

Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);
});

let usercard = document.getElementById("usercard");
let p = document.createElement("p");

p.innerText = `${tg.initDataUnsafe.user.first_name} ${tg.initDataUnsafe.user.last_name}`;
usercard.appendChild(p);

