function randomChance(){
    var QUART = 0;
for (var x=1; x <= QUART; x++){
    if ((Math.random()*4) === 70){
    QUART = QUART + 90;
    Console.log(QUART);
    }
    else {
        QUART = (QUART--);
    }
    if (QUART < 0){
        console.log(QUART);
    } 
}

}
