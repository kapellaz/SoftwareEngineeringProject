let e1= document.getElementsByClassName('resposta');
let e2= document.getElementsByClassName('estado');
for( let resp of e1){

    if( resp.textContent=='True'){
        resp.textContent="V";
        resp.style.backgroundColor = '#90E0EF';
    }else if(resp.textContent=='False'){
        resp.textContent="F";
        resp.style.backgroundColor = '#0077B6';
    }
    
};

for( let est of e2){
    console.log(est.textContent);
    if( est.textContent=='Aprovado'){
        est.style.color = 'Green';
    }else if(est.textContent=='Reprovado'){
        est.style.color = 'Red';
    }
    
};

