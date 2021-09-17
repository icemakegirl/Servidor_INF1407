bonequinhos = [
    'saindo.gif',
    'dormindo.gif',
    'sentado.gif',
    'aplaudindoSentado.gif',
    'aplaudindoEmPe.gif',
    'festejando.gif',
    'idolatrando.gif'
]
bonequinhoAtual=4;
onload=function(){
    var btnmenos=document.getElementById("menosid");
    btnmenos.addEventListener('mouseover',diminuiCotacao);
    var btnmais=document.getElementById("maisid");
    btnmais.addEventListener('mouseover',aumentaCotacao);
    //resetar
    document.getElementById("boneco").addEventListener("click",resetarBoneco);
}
function diminuiCotacao(){
    console.log('diminui');
    bonequinhoAtual--;
    if(bonequinhoAtual<0) bonequinhoAtual=0;
    document.getElementById("boneco").src='imagens/'+bonequinhos[bonequinhoAtual];

}
function aumentaCotacao(){
    console.log('aumenta');
    bonequinhoAtual++;
    if(bonequinhoAtual>=bonequinhos.length) bonequinhoAtual=bonequinhos.length-1;
    document.getElementById("boneco").src='imagens/'+bonequinhos[bonequinhoAtual];
}
function resetarBoneco(){
    bonequinhoAtual=2;
    document.getElementById("boneco").src='imagens/'+bonequinhos[bonequinhoAtual];
}