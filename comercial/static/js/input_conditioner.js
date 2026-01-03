document.getElementById("id_tipo_pessoa").addEventListener('change', function(event){
    if (this.value == "PF"){
        fieldsForPF = document.getElementsByClassName("forPF");
        fieldsForPF.array.forEach(element => {
            element.classList.add("hidden")
        });
    }else if{
    }
})