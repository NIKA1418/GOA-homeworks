let count = 0; 

let interval = setInterval(function() { 
    console.log("nika"); 
    count++; 

    if (count === 4) { 
        clearInterval(interval); 
    }
}, 5000); 

