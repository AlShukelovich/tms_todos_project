var counter = 0;
function handleClick() {
    alert("Вы нажали на кнопку");
    //counter += 1;
    //console.log("Мы нажали кнопку " + counter + " раз(а)");
    //document.getElementsByTagName("span")[0].textContent = counter;

};

window.onload = function() {
    //var buttons = document.getElementsByTagName('button').
   // for (var i; i < buttons.length; i++) {
   //      buttons[i].addEventListener("click", buttonClick)} ;
    //console.log('Задача завершена');

    //document.getElementById('button').addEventListener('click', handleClick);
    console.log('Задача завершена');

    document.getElementById('button').addEventListener('click', handleClick);
};