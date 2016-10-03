var data_id = ""
$(document).ready(function(){
  data_id = $('.data-select:first-child').attr('data-val') ;

  call_data(data_id) ;

  $('.data-select').click(function(){
    data_id = $(this).attr('data-val') ;
    $('#q').html("") ;
    call_data(data_id) ;
  }) ;

  $('#answer').click(check_answer) ;
});

function call_data(data_id) {
  $.ajax({
    url: '/vocabulary/q/' + data_id,
    dataType: 'json'
  })
  .done(function(data){
    for (d in data) {
      tr = $('<tr />') ;
      td_q = $('<td />').text(data[d]) ;
      td_a = $('<td />').addClass('ans') ;
      td_t = $('<input type="text" />').addClass('form-control').attr('name', 'data[]');
      td_ca = $('<td />').addClass('cans') ;
      td_verify = $('<td />').addClass('vans').append($('<i />').addClass('glyphicon glyphicon-remove hide').css('color', 'red'));
      $('#q').append(tr.append(td_q).append(td_a.append(td_t)).append(td_ca).append(td_verify)) ;
    }
  }) ;
}

function check_answer() {
  if(!data_id)
    return;

  $.ajax({
    url: '/vocabulary/a/' + data_id,
    dataType: 'json'
  })
  .done(function(data){
    var correct = 0 ;

    // check answer
    $('input[name="data[]"]').each(function(index){
      $($('.cans')[index]).text(data[index]) ;
      $($('.vans i')[index]).removeClass('hide') ;
      if (data[index] == $(this).val().trim())
      {
        correct += 1 ;
        $($('.vans i')[index]).removeClass('glyphicon-remove').addClass('glyphicon-ok').css('color', 'green') ;
      }
    }) ;

    // compute score
    score = (correct * 100.0 / data.length).toFixed(2);
    swal("Good job!", "You get " + score + " / 100 points", "success") ;
  }) ;
}
