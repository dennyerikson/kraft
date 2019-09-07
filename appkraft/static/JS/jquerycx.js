
    $('#mesaModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var pk = button.data('pk')

    document.getElementById("idmesa").innerHTML = pk;
    var btnmesa = document.getElementById("btnmesa");
    btnmesa.setAttribute("onclick","selectMs("+pk+");" );
    var modal = $(this)
    // modal.find('#imagens').attr("src", button.data('whateverimagem'))
    })

//<!-- SCRIPT MODAL IMG -->


$(document).ready(function(){
    var id = $("#numero").val();
    
    if(id == ""){
        // alert(id);
        $("#btnfinalizar").prop("disabled", true);
    }
});


//<!-- SCRIPT MODAL FinalVenda -->

    $('#finalVendaModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var valor = button.data('valor')
    var pk = button.data('pk')
    document.getElementById("finalizar-").id = "finalizar-" + pk;
    document.getElementById("totallabel").innerHTML = valor;
    $('#total').val(valor);
    $('#dinheiro').val("");
    $('#cartao').val("");
    $('#credito').val("");
    var modal = $(this)
    // modal.find('#total').attr("value", valor)
    })

//<!-- SCRIPT MODAL FinalVenda -->

//<!-- SCRIPT MODAL IMG -->

    $('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var recipientdetalhes = button.data('whateverdetalhes')
    var recipientimagem = button.data('whateverimagem')
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    document.getElementById("name").innerHTML = recipientdetalhes;
    var modal = $(this)
    modal.find('#imagens').attr("src", button.data('whateverimagem'))
    })

//<!-- SCRIPT MODAL IMG -->

//<!-- SCRIPT MODAL CLIENTE -->
                                              
    $("#btaddcliente").on('click', function () {
    $('#addcliente').modal('show');              
    });                  

//<!-- SCRIPT MODAL CLIENTE -->

//<!-- SCRIPT TABELA VENDAS -->

function Submits(){
    var search_form = document.getElementById("search_form");
    var venda_form = document.getElementById("venda_form");
    setTimeout(function(){
        venda_form.submit();
    }, 50);  
    search_form.submit();
}

//<!-- SCRIPT TABELA VENDAS -->


    $(document).ready(function() {
        $("#comanda a").click(function() {
            //Do stuff when clicked
            var primary_key = $(this).attr('id')
            // alert(primary_key)
            if(primary_key.includes('finalizar')){
                alert(primary_key.split('-')[1])
                
                $('#comanda').on('show.bs.modal', function (event) {
                    // var button = $(event.relatedTarget) // Button that triggered the modal
                    // var recipientid = button.data('whateverid')
                    // var recipientnome = button.data('whatevernome')
                    // // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
                    // // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
                    // document.getElementById("id").innerHTML = recipientid;
                    // document.getElementById("nome").innerHTML = recipientnome; 
                    // document.getElementById("id_").setAttribute("value", recipientid); 
                
                    var modal = $(this)

                                    
                    
                })

            }
            else{
                $('#numero').val(primary_key)
                Submits();
            }
        });
    });


       $(document).ready(function(){

            $("#dinheiro").on('blur', function() {
                calcular("#dinheiro", "#cartao", "#credito", "#total", "troco","pago");
            });

            $("#cartao").on('blur', function() {
                calcular("#dinheiro", "#cartao", "#credito", "#total", "troco","pago");
            });  

            $("#credito").on('blur', function() {
                calcular("#dinheiro", "#cartao", "#credito", "#total", "troco","pago");
            });    

            $("#dinheiro_").on('blur', function() {
                calcular("#dinheiro_", "#cartao_", "#credito_", "#total_", "troco_","pago_");
            });

            $("#cartao_").on('blur', function() {
                calcular("#dinheiro_", "#cartao_", "#credito_", "#total_", "troco_","pago_");
            });  

            $("#credito_").on('blur', function() {
                calcular("#dinheiro_", "#cartao_", "#credito_", "#total_", "troco_","pago_");
            });        

        });

       function calcular(dinheiro, cartao, credito, total, troco, pago){
            // var elvisLives = Math.PI > 4 ? "Yep" : "Nope";
           valorDinheiro = parseFloat($(dinheiro).val().replace(",", ".")); 
           valorCartao = parseFloat($(cartao).val() ? $(cartao).val().replace(",", "."):0); 
           valorCredito = parseFloat($(credito).val() ? $(credito).val().replace(",", "."):0); 
           valorTotal = parseFloat($(total).val().replace(",", "."));
           valorTroco = parseFloat(((valorDinheiro + valorCartao + valorCredito) - valorTotal)).toFixed(2).replace(".", ",");
           valorPago = parseFloat(((valorDinheiro + valorCartao + valorCredito))).toFixed(2).replace(".", ",");
           
            // alert(valorTroco);                                                                                                                                               
            document.getElementById(troco).innerHTML = valorTroco;
            document.getElementById(pago).innerHTML = valorPago;
            // $('#troco').val(valorTroco);
                
       }



       // Finalizar on click
       $("#finalizar").on('click', 'a[id^=finalizar-]', function(){
            var post_primary_key = $(this).attr('id').split('-')[1];
            var id = $(this).attr('data-url');
            // alert(post_primary_key); // sanity check
            finaliza_venda(post_primary_key);
        });

        $("#finalVendaModal").on('click', 'a[id^=finalizar-]', function(){
            var post_primary_key = $(this).attr('id').split('-')[1];
            var id = $(this).attr('data-url');
            // alert(post_primary_key); // sanity check
            finaliza_venda(post_primary_key);
        });
            
       function finaliza_venda(post_primary_key){

           if (confirm('Deseja finalizar essa venda?')==true){
               $.ajax({
                   url : "finalizar_venda/", // the endpoint
                   type : "POST", // http method
                   data : { postpk : post_primary_key }, // data sent with the delete request
                   beforeSend: function (xhr) {
                       xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
                   },
                   success : function(json) {
                       // hide the post
                   $('#post-'+post_primary_key).hide(); // hide the post on success
                //    alert("Venda finalizada!");
                    window.location.replace("/caixa/");
                   },

                   error : function(xhr,errmsg,err) {
                       // Show an error
                       $('#results').html("<div class='alert-box alert radius' data-alert>"+
                       "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                       alert(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                   }
               });
           } else {
               return false;
           }
       };
       // Finalizar on click


    // Finalizar on click

//<!-- SCRIPT FIM-->

function selectMs(pk){
    var e = document.getElementById("selectmesa");
    var mesa = parseInt(e.options[e.selectedIndex].value);
    // alert("mesa:"+mesa+" id:"+pk);
    if(mesa>0){
        uppost(parseInt(pk), mesa);
    }
}; 

function uppost(pk, mesa){

    $.ajax({
        url : "setarmesa/", // the endpoint ex- "finalizar_venda/"
        type : "POST", // http method ex- "POST"
        data : { postpk : pk, postmesa : mesa }, // data sent 
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
        },
        success : function(json) {
            // hide the post
        $('#post-'+pk).hide(); // hide the post on success
        //    alert("Venda finalizada!");
            window.location.replace("/caixa/");
        },

        error : function(xhr,errmsg,err) {
            // Show an error
            $('#results').html("<div class='alert-box alert radius' data-alert>"+
            "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
            alert(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
    
};


