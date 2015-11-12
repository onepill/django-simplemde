django.jQuery(function(){
  django.jQuery.each(django.jQuery('.simplemde-box'), function(i, elem){
    var options = JSON.parse(django.jQuery(elem).attr('data-simplemde-options'));
    options['element'] = elem;
    new SimpleMDE( options );
  });
  var simplemde = new SimpleMDE({ element: document.getElementById("simplemde_box") });
});