onload=function(){
    contEmail=0
    this.document.getElementById('idEmail').addEventListener('click',addEmail);
}
function addEmail(){
    var tagDiv=document.createElement('div');
    var texto=document.createTextNode('e-mail:');
    tagDiv.appendChild(texto);
    var campoInput=document.createElement('input');
    campoInput.type='text';
    campoInput.name='email';
    campoInput.id='idEmail'+contEmail;
    tagDiv.appendChild(campoInput);

    var campoButton = document.createElement('input');
    campoButton.type='button';
    campoButton.value=' - ';
    campoButton.addEventListener('click',removeEmail);
    tagDiv.appendChild(campoButton);
    contEmail++;
    document.getElementById('iDivEmail').appendChild(tagDiv);
}
 function removeEmail(ev){
    var campoButton = ev.target;
    var tagDiv= campoButton.parentNode;
    document.getElementById('iDivEmail').removeChild(tagDiv);

}