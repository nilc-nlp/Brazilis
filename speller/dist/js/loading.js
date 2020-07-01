// Setup
this.$('.js-loading-bar').modal({
  backdrop: 'static',
  show: false
}).on('shown.bs.modal', function( event ) {

   var $bar = $(event.target).find('.progress-bar'),
       _wait = function() {       
            setTimeout(function() {
              if ( $bar.is(':visible')) { 
                   $bar.addClass('animate');
               } else {
                  console.log('not ready'); 
                  _wait();
               }
            }, 0);       
       };
   
   _wait();
   
});

$('#load').click(function() {
  var $modal = $('.js-loading-bar'),
      $bar = $modal.find('.progress-bar');
  
  $modal.modal('show');

  setTimeout(function() {
    $modal.modal('hide'); 
    $bar.removeClass('animate');
    //$modal.modal('hide');        
  }, 1500);
});