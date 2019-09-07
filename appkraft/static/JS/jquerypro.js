  // calcular porcentagem por ganho e preencher fields
  // get custo = name:custo, id:id_custo
  $('#id_custo').on('input', function(){
    calcular();
});
//get ganho = name:ganho, id:id_ganho
$('#id_ganho').on('input', function(){
    // calcular();
});
//get valor = name:valor, id:id_valor
$('#id_valor').on('input', function(){
    calcular();
    // $('#id_ganho').attr('disabled','disabled');
});

function calcular(){

    valorCusto = parseFloat($('#id_custo').val()); // valor de custo
  valorPreco = parseFloat($('#id_valor').val()); // valor de preço
  valorGanho = parseFloat($('#id_ganho').val()); // percentual de ganho
  
  if(valorCusto > 0 && valorPreco > 0){
    $('#id_ganho').val(parseFloat(((valorPreco - valorCusto)/ valorCusto)*100).toFixed(2)+" %");
  }
  
}