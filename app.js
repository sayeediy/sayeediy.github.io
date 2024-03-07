
let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let item = "";

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");
let btn5 = document.getElementById("btn5");
let btn6 = document.getElementById("btn6");

btn1.addEventListener("click", function () {
    handleButtonClick("1");
});

btn2.addEventListener("click", function () {
    handleButtonClick("2");
});

btn3.addEventListener("click", function () {
    handleButtonClick("3");
});

btn4.addEventListener("click", function () {
    handleButtonClick("4");
});

btn5.addEventListener("click", function () {
    handleButtonClick("5");
});

btn6.addEventListener("click", function () {
    handleButtonClick("6");
});

function handleButtonClick(selectedItem) {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    } else {
        tg.MainButton.setText(`Вы выбрали товар ${selectedItem}!`);
        item = selectedItem;
        tg.MainButton.show();

        // Your logic to handle the invoice details here
        // For example, you can open a payment modal or update the UI
        // You can use the 'item' variable to get the selected item details
        console.log("Selected Item:", item);
    }
}

Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);
});

let usercard = document.getElementById("usercard");

let p = document.createElement("p");

p.innerText = `${tg.initDataUnsafe.user.first_name}
${tg.initDataUnsafe.user.last_name}`;

usercard.appendChild(p);
