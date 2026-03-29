var counter=document.querySelector(".counter")
let count=1;
setInterval(() => {
    count++;
    counter.innerText = count;
}, 10)
