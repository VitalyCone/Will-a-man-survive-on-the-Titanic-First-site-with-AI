const rang = document.querySelector('.range')
const outp = document.querySelector('.outp')
const subm = document.querySelector('#submit')

let Age = 1
let Sex
let Pclass
outp.textContent = rang.value

values = {
    '1':'male',
    '2':'female',
    '3':'1',
    '4':'2',
    '5':'3',
}

function onClick(elem){
    elem.value === '1' || elem.value === '2'
    ?Sex = values[elem.value]
    :Pclass = values[elem.value]
    console.log(Sex,Pclass)
}

rang.addEventListener("input", (event) => {
    outp.textContent = event.target.value
    Age = event.target.value
});

subm.addEventListener('click',()=>{
    if(Pclass && Age && Sex){
        let xhr = new XMLHttpRequest();
        xhr.open("POST", "/request", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                res = JSON.parse(xhr.responseText).data
                document.getElementById("result").innerHTML =
                    `<p>Результат: У ${Sex === 'male' ?'мужчины' :'женщины'} 
                    ${Pclass} класса следования, возрастом 
                    ${Age} лет, шанс выжить
                    ${res}%<p>`
            }
            if (this.status != 200) {
                alert('Ошибка: '+(this.status ? this.statusText : 'запрос не удался'))
            }}
        xhr.send(JSON.stringify({data:{Pclass,Sex,Age}}))
    }else alert('Заполните все поля')
})
